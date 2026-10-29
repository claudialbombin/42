"""Checks done before generating, so a wrong maze is never created.

Every function raises a ValueError with a clear message. The message
is printed by main() as it is, so it has to be understandable.
"""

from mazegen.constants import ALGORITHMS, MAX_SIZE, MIN_LOOPS, MIN_SIZE, Cell
from mazegen.grid import MazeGrid


def check_size(width: int, height: int) -> None:
    """Check that the width and the height are in the allowed range.

    Less than 2 makes no sense (entry and exit must be different) and
    more than 200 would not fit in any terminal.

    Args:
        width: Number of columns asked.
        height: Number of rows asked.

    Raises:
        ValueError: If one of them is outside MIN_SIZE..MAX_SIZE.
    """
    for name, value in (("width", width), ("height", height)):
        if value < MIN_SIZE or value > MAX_SIZE:
            raise ValueError(f"{name} must be between {MIN_SIZE} and "
                             f"{MAX_SIZE} (got {value})")


def check_algorithm(algorithm: str) -> None:
    """Check that the algorithm asked exists.

    Args:
        algorithm: Name of the algorithm ("backtracker" or "prim").

    Raises:
        ValueError: If the name is not in ALGORITHMS.
    """
    if algorithm not in ALGORITHMS:
        raise ValueError(f"unknown algorithm '{algorithm}' "
                         f"(choose one of: {', '.join(ALGORITHMS)})")


def check_cells(grid: MazeGrid, entry: Cell, exit_cell: Cell) -> None:
    """Check that entry and exit are two different free cells.

    They must be inside the maze, not on the "42" (those cells are
    fully closed, nobody could go in or out) and not the same cell.

    Args:
        grid: Grid of the maze (with the "42" already placed).
        entry: Entry cell (x, y).
        exit_cell: Exit cell (x, y).

    Raises:
        ValueError: If one of the rules above is broken.
    """
    for name, (x, y) in (("entry", entry), ("exit", exit_cell)):
        if not grid.inside(x, y):
            raise ValueError(f"{name} ({x},{y}) is outside the maze "
                             f"({grid.width}x{grid.height})")
        if (x, y) in grid.pattern:
            raise ValueError(f"{name} ({x},{y}) is on the '42' pattern")
    if entry == exit_cell:
        raise ValueError("entry and exit must be different cells")


def check_loops_possible(grid: MazeGrid) -> None:
    """Check that a non perfect board can have MIN_LOOPS loops.

    I count the loops the maze would have with every wall open. If even
    that is not enough, the maze is just too small (a 2x2 maze can only
    have one loop, for example).

    Args:
        grid: Grid of the maze (with the "42" already placed).

    Raises:
        ValueError: If the maze can't have MIN_LOOPS loops.
    """
    cells = 0
    edges = 0
    for y in range(grid.height):
        for x in range(grid.width):
            if not grid.is_free(x, y):
                continue
            cells += 1
            if grid.is_free(x + 1, y):
                edges += 1
            if grid.is_free(x, y + 1):
                edges += 1
    if edges - cells + 1 < MIN_LOOPS:
        raise ValueError("maze too small for a non perfect board "
                         f"(it needs at least {MIN_LOOPS} loops)")
