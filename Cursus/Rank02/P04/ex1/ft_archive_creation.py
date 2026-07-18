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


def create_archive(file_path: str, lines: typing.Iterable[str]) -> None:
    file = None
    try:
        file = open(file_path, "w")
        for line in lines:
            file.write(f"{line}\n")
    except Exception as error:
        print(f"Error occurred while creating archive: {error}")
        sys.exit(1)
    finally:
        if file is not None:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ft_archive_creation.py <archive.txt>")
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

    new_content = [f"{line}#" for line in archive_lines]

    print("Transform data:")
    print("---")

    for line in new_content:
        print(line)

    print("---")
    save_path = input("Enter new file name (or empty): ")

    if save_path:
        print(f"Saving data to '{save_path}'")
        create_archive(save_path, new_content)
        print(f"Data saved in file '{save_path}'.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
