*This project has been created as part of the 42 curriculum by clopez-b.*

# Born2beRoot

## Table of contents

- [Description](#description)
  - [Goal of the project](#goal-of-the-project)
  - [Final configuration at a glance](#final-configuration-at-a-glance)
- [Instructions](#instructions)
  - [Repository contents](#repository-contents)
  - [Checking the signature](#checking-the-signature)
  - [Running the virtual machine](#running-the-virtual-machine)
  - [Building the machine from scratch](#building-the-machine-from-scratch)
  - [Verification commands](#verification-commands)
- [Project description](#project-description)
  - [Design choices](#design-choices)
    - [Partitioning and encryption](#partitioning-and-encryption)
    - [Users and groups](#users-and-groups)
    - [Password policy](#password-policy)
    - [The sudo configuration](#the-sudo-configuration)
    - [SSH](#ssh)
    - [Firewall](#firewall)
    - [Hostname](#hostname)
    - [AppArmor](#apparmor)
    - [Installed services](#installed-services)
  - [Monitoring script](#monitoring-script)
    - [What it displays](#what-it-displays)
    - [The script](#the-script)
    - [How it works](#how-it-works)
    - [Running it with cron](#running-it-with-cron)
  - [Comparisons](#comparisons)
    - [Debian vs Rocky Linux](#debian-vs-rocky-linux)
    - [AppArmor vs SELinux](#apparmor-vs-selinux)
    - [UFW vs firewalld](#ufw-vs-firewalld)
    - [VirtualBox vs UTM](#virtualbox-vs-utm)
    - [apt vs aptitude](#apt-vs-aptitude)
- [Resources](#resources)
  - [References](#references)
  - [Use of AI](#use-of-ai)

---

## Description

### Goal of the project

Born2beRoot is a system administration project. The goal is to build a small
but secure server from scratch inside a virtual machine, and to understand
each piece of it well enough to explain and modify it live during the defense.

The virtual machine runs **Debian (stable)** with no graphical interface. It
has an encrypted disk managed with LVM, a strict password policy, a
restricted `sudo` configuration, a firewall, an SSH server, and a monitoring
script that reports the state of the machine to every terminal at boot and
every 10 minutes.

Working on it covers the basic building blocks of a Linux server: how a disk
is partitioned and encrypted, how users, groups and permissions work, how
authentication is enforced with PAM, how a service is exposed (or hidden)
with a firewall and an SSH configuration, and how routine tasks are
automated with cron and shell scripts.

Only two files are submitted in the Git repository: this `README.md` and
`signature.txt`, which contains the SHA-1 hash of the virtual machine disk
(`.vdi`). The virtual machine itself is **never** pushed to the repository.

### Final configuration at a glance

| Item | Value |
| --- | --- |
| Operating system | Debian (latest stable, 64-bit, no GUI) |
| Hypervisor | VirtualBox |
| Hostname | `clopez-b42` |
| Users | `root` and `clopez-b` (member of `user42` and `sudo`) |
| Partitioning | Encrypted LVM (LUKS), separate unencrypted `/boot` |
| SSH | Port `4242`, root login disabled |
| Firewall | UFW enabled at boot, only port `4242` open |
| Mandatory access control | AppArmor, active at boot |
| Password expiry | 30 days maximum, 2 days minimum, 7 days warning |
| Password complexity | `pam_pwquality`, minimum 10 characters, see [Password policy](#password-policy) |
| sudo | 3 attempts, custom error message, input/output logging, TTY required |
| Monitoring | `/root/monitoring.sh` via cron (`@reboot` and every 10 minutes) |

## Instructions

### Repository contents

```
.
├── README.md
└── signature.txt
```

`signature.txt` holds the SHA-1 hash of the `.vdi` disk. Because the hash
changes every time the virtual machine is powered on, the VM must be shut down
before the hash is recomputed, and the file must be updated before each
evaluation.

### Checking the signature

With the virtual machine powered off, compute the hash of the disk and compare
it with the one stored in the repository:

```bash
# Linux
sha1sum born2beroot.vdi
# macOS
shasum born2beroot.vdi
# Windows
certUtil -hashfile born2beroot.vdi sha1

# Compare with the repository (no output means they are identical)
diff <(sha1sum born2beroot.vdi | awk '{print $1}') signature.txt
```

### Running the virtual machine

1. Install VirtualBox.
2. Create a new virtual machine (type Linux, version Debian 64-bit) and choose
   "Use an existing virtual hard disk file", selecting the `.vdi` file.
3. Start the machine. The first screen asks for the **LUKS passphrase** to
   unlock the encrypted disk.
4. Log in with the `clopez-b` user (passwords are not stored in this
   repository).
5. To connect over SSH, add a port forwarding rule in the VirtualBox network
   settings (Settings, Network, Advanced, Port Forwarding: host port `2222`
   to guest port `4242`) and run:

   ```bash
   ssh -p 2222 clopez-b@127.0.0.1
   ```

   Logging in as `root` over SSH is refused on purpose.

### Building the machine from scratch

This is a summary of the steps followed to build the machine. The reasons
behind each configuration are explained in [Design choices](#design-choices).

1. **Create the virtual machine.** Download the Debian stable `netinst` ISO
   from `debian.org` and create a VirtualBox machine (type Linux, Debian
   64-bit) with 1 GB of RAM, one or two CPUs, an 8 to 10 GB dynamically
   allocated VDI disk and the network adapter in NAT mode. Mount the ISO on
   the virtual optical drive.

2. **Install Debian in text mode.** Choose "Install" (not "Graphical
   install"), keep the default network configuration (DHCP) and set any
   temporary hostname, since it is changed later. Every password set during
   the installation is replaced later, once the password policy is active.

3. **Partition the disk.** Choose "Guided - use entire disk and set up
   encrypted LVM", select the disk, use the "All files in one partition"
   scheme and confirm the changes. The installer asks for the LUKS
   passphrase at this point. Finish partitioning and write the changes.

4. **Select the software.** In the software selection screen, uncheck
   everything except `SSH server` and `standard system utilities`. No
   desktop environment is installed. Install GRUB on the main disk.

5. **First boot.** Unlock the disk with the LUKS passphrase, log in as
   `root`, update the system and install the needed packages:

   ```bash
   apt update && apt upgrade -y
   apt install -y sudo vim ufw libpam-pwquality apparmor apparmor-utils
   ```

6. **Create the group and the user.**

   ```bash
   groupadd user42
   adduser clopez-b
   usermod -aG user42,sudo clopez-b
   ```

7. **Password policy.** Edit `/etc/login.defs` and
   `/etc/pam.d/common-password`, apply the expiry rules to the existing
   users with `chage`, and set the final passwords with `passwd`.

8. **sudo.** Create `/var/log/sudo` and add the rules with `visudo`.

9. **SSH.** Set `Port 4242` and `PermitRootLogin no` in
   `/etc/ssh/sshd_config`, then `systemctl restart ssh`.

10. **Firewall.** `ufw allow 4242`, `ufw enable`, `systemctl enable ufw`.

11. **Hostname.** `hostnamectl set-hostname clopez-b42` and update the
    `127.0.1.1` line in `/etc/hosts`.

12. **Monitoring.** Create `/root/monitoring.sh`, make it executable and add
    the two lines to root's crontab.

13. **Signature.** Shut the machine down completely, compute the SHA-1 of
    the `.vdi` file and write it into `signature.txt`.

### Verification commands

These are the commands used to check that each requirement is met:

```bash
lsblk                              # partitions, encrypted volume and LVM
aa-status                          # AppArmor is loaded and enforcing
systemctl status ufw               # firewall is active
sudo ufw status numbered           # only port 4242 (v4 and v6) is open
systemctl status ssh               # SSH server is running
ss -tulnp | grep 4242              # SSH is listening on port 4242
hostnamectl                        # hostname is clopez-b42
getent group sudo user42           # members of the sudo and user42 groups
chage -l clopez-b                  # password expiry information
sudo cat /var/log/sudo/sudo.log    # sudo command history
sudo crontab -l                    # cron entries of root
```

## Project description

### Design choices

#### Partitioning and encryption

The disk is encrypted with **LUKS** and managed with **LVM**. The layout is:

- A small unencrypted `/boot` partition. It stays outside the encryption
  because the bootloader (GRUB) has to read the kernel from it before it can
  even ask for the passphrase.
- A second partition that holds the encrypted container (`sda5_crypt`).
- Inside that container, one LVM volume group with the logical volumes
  `root` and `swap`.

```
sda
├─sda1            /boot                (not encrypted)
├─sda2            (extended partition)
└─sda5            LUKS container
  └─sda5_crypt    LVM volume group
    ├─...-root    /
    └─...-swap    [SWAP]
```

Encryption protects the data at rest: if someone copies the virtual disk,
nothing can be read without the passphrase. LVM was chosen over fixed
partitions because logical volumes can be resized, added or moved later
without touching the physical disk, which is what makes it useful on
servers. The simplest scheme ("all files in one partition") was chosen for
the mandatory part because nothing in the subject requires separate `/home`,
`/var` or `/tmp` volumes.

#### Users and groups

Besides `root`, there is a user named after my login (`clopez-b`) that
belongs to both the `user42` and `sudo` groups. Working as a normal user and
elevating with `sudo` when needed is safer than logging in as root: the root
password is never shared, and every privileged command is logged. The
`user42` group has no special permissions; it is a requirement of the
subject.

Commands used to manage users and groups (also useful during the defense):

```bash
sudo adduser <name>                 # create a user
sudo groupadd <group>               # create a group
sudo usermod -aG <group> <name>     # add a user to a group
sudo deluser <name> <group>         # remove a user from a group
groups <name>                       # groups of a user
```

`adduser` is Debian's interactive and friendlier wrapper (it creates the home
directory and asks for the password), while `useradd` is the lower-level
command that exists on every Linux distribution.

#### Password policy

Two files are involved, and the policy applies to all users, `root` included.

**Expiry rules** in `/etc/login.defs`:

```
PASS_MAX_DAYS   30
PASS_MIN_DAYS   2
PASS_WARN_AGE   7
```

A password expires after 30 days, cannot be changed again before 2 days have
passed, and the user is warned 7 days before it expires. These values only
affect users created afterwards, so the existing accounts were updated
manually:

```bash
chage -M 30 -m 2 -W 7 root
chage -M 30 -m 2 -W 7 clopez-b
```

**Complexity rules** in `/etc/pam.d/common-password`, using the
`libpam-pwquality` module:

```
password requisite pam_pwquality.so retry=3 minlen=10 ucredit=-1 lcredit=-1 dcredit=-1 maxrepeat=3 reject_username difok=7 enforce_for_root
```

| Option | Effect |
| --- | --- |
| `retry=3` | The user gets 3 attempts to enter a valid password |
| `minlen=10` | At least 10 characters |
| `ucredit=-1` | At least one uppercase letter |
| `lcredit=-1` | At least one lowercase letter |
| `dcredit=-1` | At least one digit |
| `maxrepeat=3` | No more than 3 identical consecutive characters |
| `reject_username` | The password cannot contain the username |
| `difok=7` | At least 7 characters must differ from the previous password (does not apply to root) |
| `enforce_for_root` | The rules are also enforced when root changes a password |

**Advantages and disadvantages.** Long, complex and frequently renewed
passwords are much harder to guess with brute force or dictionary attacks,
and a leaked password stays valid only for a limited time. On the other hand,
rules that are too strict push people to write passwords down or to reuse
predictable variations (for example `January2026!`, `February2026!`), which
can weaken security in practice, and they increase lockouts and support work.

#### The sudo configuration

`sudo` lets an authorized user run a command with root privileges without
knowing the root password or logging in as root. For example, installing a
package is done with `sudo apt install <package>`. The rules were added with
`visudo`, which checks the syntax before saving (a mistake in
`/etc/sudoers` can lock everyone out of `sudo`).

```
Defaults        passwd_tries=3
Defaults        badpass_message="<custom error message>"
Defaults        logfile="/var/log/sudo/sudo.log"
Defaults        log_input,log_output
Defaults        iolog_dir="/var/log/sudo"
Defaults        requiretty
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
```

| Rule | Purpose |
| --- | --- |
| `passwd_tries=3` | Maximum of 3 password attempts per command |
| `badpass_message` | Custom message shown when the password is wrong |
| `logfile` | Every sudo command is appended to this log file |
| `log_input,log_output` | Both what is typed and what is printed are archived |
| `iolog_dir` | Directory where the input/output archives are stored |
| `requiretty` | sudo only works from a real terminal, not from scripts without a TTY |
| `secure_path` | sudo only searches for executables in this fixed list of directories, which prevents running a malicious program placed in a user-controlled `PATH` |

The directory has to exist beforehand (`mkdir -p /var/log/sudo`). The log can
be checked after running any `sudo` command with
`sudo cat /var/log/sudo/sudo.log`.

#### SSH

The SSH server is configured in `/etc/ssh/sshd_config` with two changes:

```
Port 4242
PermitRootLogin no
```

Changing the default port 22 reduces the amount of automated scanning and
brute-force attempts the server receives. It is not real protection by
itself, but it removes a lot of noise. Disabling root login over SSH means an
attacker would need to know a valid username as well as its password, and
every remote action is tied to a real user that can be traced in the logs.

After editing the file the service is restarted (`systemctl restart ssh`) and
the port can be verified with `ss -tulnp | grep 4242`. Connecting as root
(`ssh root@localhost -p 4242`) must be refused.

#### Firewall

The firewall is **UFW** (Uncomplicated Firewall). The default policy denies
all incoming connections, and a single rule opens the SSH port:

```bash
ufw allow 4242
ufw enable
systemctl enable ufw
```

The firewall is active from boot, and `sudo ufw status numbered` lists only
the rule for port 4242 (IPv4 and IPv6). A rule can be added and removed with
`ufw allow <port>` and `ufw delete allow <port>`.

#### Hostname

The hostname is my login followed by `42` (`clopez-b42`). It is set with
`hostnamectl set-hostname clopez-b42`, and the `127.0.1.1` line of
`/etc/hosts` is updated so the machine can still resolve its own name.

#### AppArmor

AppArmor is the Mandatory Access Control system that Debian ships and loads at
boot. It confines each program to the files and capabilities its profile
allows, even if the program runs as root, which limits the damage of a
compromised service. Its state is checked with `aa-status` and
`systemctl status apparmor` (the service shows `active (exited)` because it
only loads the profiles at boot and then finishes).

#### Installed services

Only what the subject requires is installed: `sudo`, `ufw`,
`libpam-pwquality`, `apparmor` with its utilities, the OpenSSH server and
`cron` (part of a standard Debian installation). Every extra service is one
more attack surface, so nothing else was added, and no graphical environment
is installed.

### Monitoring script

#### What it displays

`/root/monitoring.sh` is a Bash script that collects information with
standard Linux commands and broadcasts it to every open terminal using
`wall`. It shows:

- The system architecture and kernel version
- The number of physical CPUs and virtual CPUs
- The available RAM and its utilization rate as a percentage
- The available storage and its utilization rate as a percentage
- The current CPU utilization rate as a percentage
- The date and time of the last reboot
- Whether LVM is active or not
- The number of active connections
- The number of users using the server
- The IPv4 address and the MAC address
- The number of commands executed with `sudo`

#### The script

```bash
#!/bin/bash
# monitoring.sh
# Collects the state of the server and sends it to all terminals with wall.
# It runs at boot and every 10 minutes from root's crontab.

# --- CPU ---
architecture=$(uname -a)
pcpu=$(lscpu | grep "^Socket(s):" | awk '{print $2}')
vcpu=$(nproc)
cpu_load=$(vmstat 1 2 | tail -1 | awk '{print 100 - $15}')

# --- Memory (in MB) ---
mem_total=$(free -m | awk '$1=="Mem:" {print $2}')
mem_used=$(free -m | awk '$1=="Mem:" {print $3}')
mem_percent=$(awk -v u="$mem_used" -v t="$mem_total" 'BEGIN{printf "%.2f", u*100/t}')

# --- Disk (all real partitions, tmpfs excluded) ---
disk_total=$(df -BM --total 2>/dev/null | grep total | awk '{print $2}' | tr -d 'M')
disk_used=$(df -BM --total 2>/dev/null | grep total | awk '{print $3}' | tr -d 'M')
disk_percent=$(df --total 2>/dev/null | grep total | awk '{print $5}')

# --- Last boot ---
last_boot=$(who -b | awk '{print $3" "$4}')

# --- Is LVM active? ---
if [ "$(lsblk | grep -c lvm)" -gt 0 ]; then
	lvm_use="yes"
else
	lvm_use="no"
fi

# --- Network and users ---
tcp_count=$(ss -ta | grep -c ESTAB)
users_log=$(who | wc -l)
ip_addr=$(hostname -I | awk '{print $1}')
mac_addr=$(ip link | awk '/link\/ether/ {print $2; exit}')

# --- sudo ---
sudo_count=$(grep -c COMMAND /var/log/sudo/sudo.log 2>/dev/null)

wall "
	Architecture: $architecture
	Physical CPU: $pcpu
	vCPU: $vcpu
	Memory Usage: $mem_used/${mem_total}MB ($mem_percent%)
	Disk Usage: $disk_used/${disk_total}MB ($disk_percent)
	CPU load: $cpu_load%
	Last boot: $last_boot
	LVM use: $lvm_use
	TCP Connections: $tcp_count ESTABLISHED
	User log: $users_log
	Network: IP $ip_addr ($mac_addr)
	Sudo: $sudo_count cmd"
```

#### How it works

Each value is stored in a variable with command substitution (`$(...)`), and
everything is printed in a single `wall` call at the end.

| Value | Command | Idea |
| --- | --- | --- |
| Architecture and kernel | `uname -a` | Prints the kernel name, version and architecture |
| Physical CPUs | `lscpu` | The `Socket(s)` line gives the number of physical processors |
| Virtual CPUs | `nproc` | Number of processing units available |
| CPU usage | `vmstat 1 2` | Takes two one-second samples; the last line, column 15, is the idle percentage, so `100 - idle` is the usage |
| Memory | `free -m` | Total and used memory in MB, the percentage is calculated with `awk` |
| Disk | `df -BM --total` | The `total` line adds up all the file systems |
| Last boot | `who -b` | Date and time of the last system boot |
| LVM | `lsblk` | If any device has type `lvm`, LVM is in use |
| Connections | `ss -ta` | Counts the TCP sockets in `ESTAB` state |
| Users | `who` | One line per logged-in session |
| IP and MAC | `hostname -I`, `ip link` | First IPv4 address and the `link/ether` address |
| sudo commands | `grep -c COMMAND` | Every sudo execution writes one `COMMAND=` line in the sudo log |

The script prints no error to the screen (errors that could appear are
redirected with `2>/dev/null`), and it is placed in `/root` because only root
needs to run it.

#### Running it with cron

`cron` is the Linux task scheduler: a daemon that reads a table of
scheduled commands (the crontab) and runs each one at the time it specifies.
The entries were added with `crontab -e` as root:

```
@reboot /root/monitoring.sh
*/10 * * * * /root/monitoring.sh
```

`@reboot` runs the script every time the system starts. In `*/10 * * * *` the
five fields are minute, hour, day of the month, month and day of the week,
and `*/10` in the first field means "every 10 minutes".

To change the interval (for example to 1 minute for testing) the crontab is
edited with `crontab -u root -e` and `*/10` is replaced by `*/1`. To stop the
script from running **without modifying the file or the crontab**, the cron
service is disabled with:

```bash
systemctl disable --now cron
```

and it is enabled again with `systemctl enable --now cron`.

### Comparisons

#### Debian vs Rocky Linux

Debian is a community-driven distribution that uses `.deb` packages and the
`apt` tools. Its stable release favors reliability over new features, so
package versions are conservative. Rocky Linux is a community rebuild that is
binary-compatible with Red Hat Enterprise Linux; it uses `.rpm` packages and
`dnf`, is aimed at enterprise environments with long support cycles, and
comes with SELinux and firewalld by default.

I chose Debian because the subject recommends it for a first system
administration project: the installation is simpler, the documentation and
community help are abundant, and AppArmor and UFW are easier to configure
than their Red Hat counterparts.

#### AppArmor vs SELinux

Both are Mandatory Access Control systems that restrict what each program can
do, even when it runs as root. **AppArmor** attaches profiles to **file
paths**, which makes the rules easier to read and write. **SELinux** attaches
**labels** (security contexts) to processes, files and ports, which allows
much finer control but is considerably harder to configure. Debian and Ubuntu
use AppArmor by default; the Red Hat family uses SELinux.

#### UFW vs firewalld

Both manage the packet filtering of the Linux kernel. **UFW** is a simple
front end with short commands such as `ufw allow 4242`, which is why it is
the default on Debian and Ubuntu. **firewalld** works with **zones** and
applies changes at runtime without dropping existing connections; it is the
default on the Red Hat family and suits more complex network setups.

#### VirtualBox vs UTM

**VirtualBox** is a free hypervisor that virtualizes x86/amd64 machines and
runs on Linux, Windows and Intel-based Macs. **UTM** is a macOS application
built on QEMU and Apple's virtualization framework, which makes it the option
for Apple Silicon Macs (it can also emulate other architectures, but more
slowly). I used VirtualBox.

#### apt vs aptitude

Both manage Debian packages. `apt` is the standard command-line tool and
handles installing, updating and removing packages. `aptitude` is a
higher-level front end with an interactive text interface and a more
elaborate dependency resolver that can suggest alternative solutions when
there are conflicts.

## Resources

### References

- Born2beRoot subject (42 curriculum)
- Debian documentation: <https://www.debian.org/doc/>
- Debian installation guide: <https://www.debian.org/releases/stable/installmanual>
- Debian Wiki on AppArmor: <https://wiki.debian.org/AppArmor>
- Ubuntu documentation on UFW: <https://help.ubuntu.com/community/UFW>
- Arch Wiki on LVM: <https://wiki.archlinux.org/title/LVM>
- Arch Wiki on dm-crypt (LUKS): <https://wiki.archlinux.org/title/Dm-crypt>
- VirtualBox manual: <https://www.virtualbox.org/manual/>
- Manual pages: `sudoers`, `sshd_config`, `crontab`, `pam_pwquality`,
  `login.defs`, `ufw`, `chage`, `wall`

### Use of AI

AI (Claude) was used as a study and drafting aid during this project:

- To help read the subject and turn it into a step-by-step checklist.
- To explain concepts I needed to understand for the defense: LVM and LUKS,
  AppArmor vs SELinux, PAM and `pam_pwquality`, `sudo` configuration, UFW,
  SSH and cron.

All configuration was carried out and tested by me on the virtual machine,
and I reviewed the script line by line so that I can explain it during the
evaluation. The passwords and the encryption passphrase were chosen by me and
are not stored anywhere in the repository.
