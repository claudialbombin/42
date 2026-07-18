import sys
import typing


def read_archive(file_path: str) -> typing.Generator[str, None, None]:
    file = None
    try:
        file = open(file_path, "r")
        for line in file:
            yield line.strip()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)
    finally:
        if file is not None:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ft_ancient_text.py <archive.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    for line in read_archive(file_path):
        print(line)
    print(f"Finished reading archive: {file_path}")


if __name__ == "__main__":
    main()

# The type of data open() returns is TextIOWrapper, which is a IOBase subclass.
# It represents a text stream.
