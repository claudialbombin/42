"""Place the "42" pattern in the middle of the maze."""

from typing import Set

from mazegen.constants import PATTERN_42, Cell


def pattern_fits(width: int, height: int) -> bool:
    """Tell if the "42" fits in the maze with one free cell around it.

    The free border is needed so the cells around the "42" can still
    be reached from the rest of the maze. The pattern is 7x5, so the
    maze needs to be at least 9x7.

    Args:
        width: Number of columns of the maze.
        height: Number of rows of the maze.

    Returns:
        True if the "42" fits, False if the maze is too small.
    """
    return width >= len(PATTERN_42[0]) + 2 and height >= len(PATTERN_42) + 2


def pattern_cells(width: int, height: int) -> Set[Cell]:
    """Compute the cells of the "42", centered in the maze.

    The middle column of the pattern is empty, and it always lands on
    the centre of the maze, so the centre stays a corridor (needed for
    the Pac-Man board, the player starts there).

    Args:
        width: Number of columns of the maze.
        height: Number of rows of the maze.

    Returns:
        The set of (x, y) cells of the "42". Empty if it does not fit.
    """
    cells: Set[Cell] = set()
    if not pattern_fits(width, height):
        return cells
    left = (width - len(PATTERN_42[0])) // 2
    top = (height - len(PATTERN_42)) // 2
    for row, line in enumerate(PATTERN_42):
        for col, char in enumerate(line):
            if char == "#":
                cells.add((left + col, top + row))
    return cells
