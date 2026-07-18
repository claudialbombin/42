import sys
import typing


def print_stderr(message: str) -> None:
    sys.stderr.write(f"[STDERR] {message}\n")


def read_archive(file_path: str) -> typing.Generator[str, None, None]:
    file = None
    try:
        file = open(file_path, "r")
        for line in file:
            yield line.strip()
    except Exception as error:
        print_stderr(f"Error opening file '{file_path}': {error}")
        sys.exit(1)
    finally:
        if file is not None:
            file.close()


def create_archive(file_path: str, lines: typing.Iterable[str]) -> bool:
    file = None
    try:
        file = open(file_path, "w")
        for line in lines:
            file.write(f"{line}\n")
    except Exception as error:
        print_stderr(f"Error opening file '{file_path}': {error}")
        return False
    finally:
        if file is not None:
            file.close()

    return True


def read_user_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readline().strip()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ft_stream_management.py <archive.txt>")
        sys.exit(1)

    source_path = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{source_path}'")
    print("---")

    archive_lines = list(read_archive(source_path))

    for line in archive_lines:
        print(line)

    print("---")
    print(f"File '{source_path}'closed.")

    transformed_lines = [f"{line}#" for line in archive_lines]

    print("Transform data:")
    print("---")

    for line in transformed_lines:
        print(line)

    print("---")
    save_path = read_user_input("Enter new file name (or empty): ")

    if save_path:
        print(f"Saving data to '{save_path}'")
        if create_archive(save_path, transformed_lines):
            print(f"Data saved in file '{save_path}'.")
        else:
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
