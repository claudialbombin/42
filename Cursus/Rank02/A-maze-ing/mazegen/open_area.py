"""Rule of the subject: corridors can't be wider than 2 cells.

So a 3x3 block without any wall inside is forbidden. A perfect maze can
never have one (it would have loops), so this is only needed when
walls are removed to build the Pac-Man board.
"""

from mazegen.constants import EAST, SOUTH
from mazegen.grid import MazeGrid


def try_open(grid: MazeGrid, x: int, y: int, direction: int) -> bool:
    """Open a wall only if it does not create a 3x3 open area.

    I open the wall first and then look if a big area appeared. If it
    did, I close the wall again. It is easier than guessing before.

    Args:
        grid: Grid of the maze.
        x: Column of the cell.
        y: Row of the cell.
        direction: Wall to open (the neighbour must be inside).

    Returns:
        True if the wall was opened, False if it was left closed.
    """
    grid.set_wall(x, y, direction, False)
    if makes_big_area(grid, x, y):
        grid.set_wall(x, y, direction, True)
        return False
    if grid.on_step is not None:
        grid.on_step()
    return True


def makes_big_area(grid: MazeGrid, x: int, y: int) -> bool:
    """Look for a 3x3 open area around a wall that was just opened.

    The opened wall is between (x, y) and one neighbour, so any 3x3
    block containing it starts at most 3 cells before. I check all the
    blocks that start between x - 3 and x + 1 (same for y).

    Args:
        grid: Grid of the maze.
        x: Column of the cell whose wall was opened.
        y: Row of the cell whose wall was opened.

    Returns:
        True if one of those blocks is fully open.
    """
    for top in range(y - 3, y + 2):
        for left in range(x - 3, x + 2):
            if is_open_block(grid, left, top):
                return True
    return False


def is_open_block(grid: MazeGrid, left: int, top: int) -> bool:
    """Tell if the 3x3 block starting at (left, top) has no inner wall.

    Inside a 3x3 block there are 12 walls: the EAST walls of the first
    two columns and the SOUTH walls of the first two rows. If all of
    them are open, the block is a big open area.

    Args:
        grid: Grid of the maze.
        left: Column of the top left cell of the block.
        top: Row of the top left cell of the block.

    Returns:
        True if the block is inside the grid and fully open.
    """
    if not grid.inside(left, top) or not grid.inside(left + 2, top + 2):
        return False
    for y in range(top, top + 3):
        for x in range(left, left + 3):
            if x < left + 2 and not grid.is_open(x, y, EAST):
                return False
            if y < top + 2 and not grid.is_open(x, y, SOUTH):
                return False
    return True
