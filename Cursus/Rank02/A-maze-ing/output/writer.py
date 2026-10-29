"""Write the output file, with a clear error if it fails."""

from mazegen import MazeGenerator
from output.errors import OutputError
from output.formatter import maze_to_text


def write_maze(maze: MazeGenerator, path: str) -> None:
    """Write the maze, the entry, the exit and the solution in path.

    The text comes from formatter.py, this function only opens the
    file (with "with", so it is always closed) and turns every
    possible error into an OutputError with a clear message.

    Args:
        maze: A maze that has already been generated.
        path: Name of the output file.

    Raises:
        OutputError: If the file can't be written.
    """
    text = maze_to_text(maze)
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)
    except IsADirectoryError:
        raise OutputError(f"'{path}' is a directory")
    except PermissionError:
        raise OutputError(f"no permission to write '{path}'")
    except OSError as error:
        raise OutputError(f"can't write '{path}': {error.strerror}")
