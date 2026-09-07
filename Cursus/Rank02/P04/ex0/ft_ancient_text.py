import sys
import typing


def read_archive(file_path: str) -> typing.Generator[str, None, None]:
    with open(file_path, "r") as file:
        for line in file:
            yield line.rstrip("\n")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_path}'")

    try:
        print("---")
        for index, line in enumerate(read_archive(file_path), start=1):
            print(f"[FRAGMENT {index:03d}] {line}")
        print("---")
        print(f"File '{file_path}' closed.")
    except OSError as error:
        print(f"Error opening file '{file_path}': {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# The type of data open() returns is TextIOWrapper, which is a IOBase subclass.
# It represents a text stream.
