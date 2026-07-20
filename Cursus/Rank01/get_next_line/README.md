*This project was created as part of the 42 curriculum by clopez-b.*

## Description 📚

`get_next_line` is a function that reads a text file (or any file descriptor) line by line, one call at a time, without loading the whole file into memory. The challenge behind it is not the reading itself, but keeping track of what has already been read between calls using a `static` variable, and handling buffers that don't line up neatly with the newline characters in the file.

This project is a direct continuation of Libft: it reuses the same reasoning about memory management and string handling, but applied to `read()` and file descriptors instead of plain strings.

## How it works

Each call to `get_next_line(fd)`:

1. Reads from `fd` in chunks of `BUFFER_SIZE` bytes and appends them to a `static` buffer until a `'\n'` is found or `read` reaches the end of the file.
2. Extracts the first line (up to and including the `'\n'`, or up to the end of the data if there is no more file left) and returns it as a newly allocated string.
3. Saves whatever is left after that line in the `static` buffer, ready for the next call.
4. Returns `NULL` once there is nothing left to read.

The mandatory part keeps one `static char *` per program, which works correctly as long as `get_next_line` is always called on the same file descriptor. The bonus part replaces it with a `static` array indexed by file descriptor (still a single static variable, as required by the subject), so several files can be read line by line at the same time without mixing up their contents.

## What is turned in

Only the following files are submitted for correction:

- `get_next_line.h`, `get_next_line.c`, `get_next_line_utils.c` — mandatory part.
- `get_next_line_bonus.h`, `get_next_line_bonus.c`, `get_next_line_utils_bonus.c` — bonus part.
- This `README.md`.

**No Makefile and no `main` function are part of the submission.** The subject states the project will be compiled directly by the corrector, for example (using a buffer size of 42 as an example):

```bash
cc -Wall -Werror -Wextra -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c
```

The corrector supplies its own `main`, so `get_next_line.c` / `get_next_line_utils.c` (and their bonus equivalents) must compile cleanly on their own with any `BUFFER_SIZE`, without ever defining `main`. That's exactly what's verified below.

## Files kept for local development only (not submitted)

- `Makefile` — convenience only, to build a local test binary. Not part of the mandatory turn-in and not used by the corrector.
- `mains/main_test.c` / `mains/main_test_bonus.c` — small `main` programs, kept ready so a main can be dropped in immediately if asked for during the defense, without ever being part of what gets pushed.
- `tests/` — sample `.txt` files used by those test programs.

## Instructions (local testing only)

### Build the mandatory test binary

```bash
make
./gnl_test tests/test1.txt
```

### Build the bonus test binary

```bash
make bonus
./gnl_test_bonus tests/test1.txt tests/test2.txt
```

### Clean

```bash
make clean   # removes object files
make fclean  # removes object files and binaries
make re      # fclean + all
```

### Reproducing the exact correction compile line

```bash
cc -Wall -Werror -Wextra -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c mains/main_test.c -o gnl_check
./gnl_check tests/test1.txt
```

Swap `42` for `1` or another small value to stress-test the buffer edge cases (a line split across many reads, a read landing exactly on a `'\n'`, etc.).

### Using it in another project

Copy the mandatory files (or the bonus ones) into your project, include the header, and compile with a custom `BUFFER_SIZE` if you want to test edge cases:

```bash
cc -D BUFFER_SIZE=1 -Wall -Wextra -Werror your_files.c get_next_line.c get_next_line_utils.c -o program
```

```bash
cc -Wall -Werror -Wextra -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c main_test.c -o gnl_test ./gnl_test tests/test1.txt
```

## Resources

- `man 2 read` for the behaviour of `read()` and file descriptors.
- The 42 `get_next_line` subject documentation.
- The C Handbook by Flavio Copes.

### Use of AI

AI was only used to write the `main_test` files in order to save time. It was not used to implement `get_next_line` itself or to design the buffering strategy.

## Additional Notes

Just like Libft, this project reimplements its own small string helpers (`gnl_strlen`, `gnl_strchr`, `gnl_strjoin`, `gnl_substr`) instead of depending on Libft directly, since the 42 subject requires `get_next_line` to be self-contained.
