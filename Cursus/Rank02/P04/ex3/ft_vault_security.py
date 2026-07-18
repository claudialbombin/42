def secure_archive(file_name, action="r", content=""):
    try:
        if action == "r":
            with open(file_name, "r") as file:
                return True, file.read()

        with open(file_name, "w") as file:
            file.write(content)
        return True, "Content successfully written to file"
    except Exception as error:
        return False, str(error)


def create_demo_archive(file_name):
    content = [
        "[FRAGMENT 001] Digital preservation protocols established 2087",
        "[FRAGMENT 002] Knowledge must survive the entropy wars",
        "[FRAGMENT 003] Every byte saved is a victory against oblivion",
    ]

    with open(file_name, "w") as file:
        for line in content:
            file.write(f"{line}\n")


def main():
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive'to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive'to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    demo_file = "ancient_fragment.txt"
    create_demo_archive(demo_file)

    print("Using 'secure_archive'to read from a regular file:")
    regular_result = secure_archive(demo_file)
    print(regular_result)

    print("Using 'secure_archive'to write previous content to a new file:")
    write_result = secure_archive(
        "preserved_fragment.txt",
        "w",
        regular_result[1],
    )
    print(write_result)


if __name__ == "__main__":
    main()
