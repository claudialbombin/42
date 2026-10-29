"""Build the text of the output file (without writing it).

Format:
    - one line per row, one hexadecimal digit per cell
    - an empty line
    - entry "x,y", exit "x,y" and the shortest path (N, E, S, W)
Every line ends with a '\\n'.
"""

from mazegen import MazeGenerator
from typing import Any


def maze_to_text(maze: MazeGenerator) -> str | Any:
    """Build the full content of the output file for this maze.

    I build all the text first and write it after, so if something
    fails the file is not left half written.

    Args:
        maze: A maze that has already been generated.

    Returns:
        The text of the file, every line ending with '\\n'.
    """
    entry_x, entry_y = maze.entry_pos
    exit_x, exit_y = maze.exit_pos
    text = ""
    for line in maze.to_hex_lines():
        text += line + "\n"
    text += "\n"
    text += f"{entry_x},{entry_y}\n"
    text += f"{exit_x},{exit_y}\n"
    text += maze.get_solution() + "\n"
    return text
