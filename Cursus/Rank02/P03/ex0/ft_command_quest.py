
import sys


def main() -> None:
    arguments = sys.argv[1:]

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0].split('/')[-1]}")

    if arguments:
        print(f"Arguments received: {len(arguments)}")
        for index, argument in enumerate(arguments, start=1):
            print(f"Argument {index}: {argument}")
    else:
        print("No arguments provided!")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
