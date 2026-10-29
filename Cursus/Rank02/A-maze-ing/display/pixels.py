"""Decide the colour of every "pixel" of the drawing.

The maze is drawn on a grid of (2 * width + 1) x (2 * height + 1)
pixels:
    - odd px and odd py    -> a cell
    - even px and even py  -> a corner, always a wall
    - the rest             -> a wall, or the gap between two open cells
"""

from dataclasses import dataclass
from typing import Optional, Set, Tuple

from display.colours import ENTRY_COLOUR, EXIT_COLOUR, PATH_COLOUR
from mazegen import EAST, SOUTH, MazeGenerator

Cell = Tuple[int, int]


@dataclass
class Palette:
    """The colours chosen by the user for one drawing.

    Attributes:
        wall: Colour of the walls.
        pattern: Colour of the "42" cells.
    """

    wall: int
    pattern: int


def pixel_colour(maze: MazeGenerator, px: int, py: int,
                 path_cells: Set[Cell], palette: Palette) -> Optional[int]:
    """Decide the colour of the pixel (px, py) of the drawing.

    It only looks at the parity of px and py to know if the pixel is a
    corner, a cell or a wall, and calls the right function.

    Args:
        maze: The maze being drawn.
        px: Column of the pixel.
        py: Row of the pixel.
        path_cells: Cells of the path to draw (empty if hidden).
        palette: Colours of the walls and of the "42".

    Returns:
        The colour of the pixel, or None if it is empty.
    """
    if px % 2 == 0 and py % 2 == 0:
        return palette.wall
    if px % 2 == 1 and py % 2 == 1:
        return _cell_colour(maze, (px // 2, py // 2), path_cells, palette)
    if px % 2 == 0:
        return _vertical_wall(maze, px // 2, py // 2, path_cells, palette)
    return _horizontal_wall(maze, px // 2, py // 2, path_cells, palette)


def _cell_colour(maze: MazeGenerator, cell: Cell, path_cells: Set[Cell],
                 palette: Palette) -> Optional[int]:
    """Decide the colour of the inside of a cell.

    The order of the checks matters: entry and exit go first so they
    stay visible even when the path is drawn over them.

    Args:
        maze: The maze being drawn.
        cell: The cell (x, y).
        path_cells: Cells of the path to draw (empty if hidden).
        palette: Colours of the walls and of the "42".

    Returns:
        The colour of the cell, or None if it is an empty corridor.
    """
    if cell == maze.entry_pos:
        return ENTRY_COLOUR
    if cell == maze.exit_pos:
        return EXIT_COLOUR
    if cell in maze.pattern:
        return palette.pattern
    if cell in path_cells:
        return PATH_COLOUR
    return None


def _vertical_wall(maze: MazeGenerator, x: int, y: int,
                   path_cells: Set[Cell], palette: Palette) -> Optional[int]:
    """Decide the colour of the wall between (x - 1, y) and (x, y).

    x == 0 and x == width are the left and right borders, they are
    always walls. If the wall is open and both cells are on the path,
    the gap is painted with the path colour so the path is continuous.

    Args:
        maze: The maze being drawn.
        x: Column of the cell on the right of the wall.
        y: Row of the two cells.
        path_cells: Cells of the path to draw (empty if hidden).
        palette: Colours of the walls and of the "42".

    Returns:
        The colour of the wall, or None if it is open.
    """
    if x == 0 or x == maze.width or not maze.is_open(x - 1, y, EAST):
        return palette.wall
    # two neighbour cells of a shortest path are always consecutive
    if (x - 1, y) in path_cells and (x, y) in path_cells:
        return PATH_COLOUR
    return None


def _horizontal_wall(maze: MazeGenerator, x: int, y: int,
                     path_cells: Set[Cell],
                     palette: Palette) -> Optional[int]:
    """Decide the colour of the wall between (x, y - 1) and (x, y).

    Same idea as _vertical_wall(), but for the walls between a cell and
    the one above it. y == 0 and y == height are the borders.

    Args:
        maze: The maze being drawn.
        x: Column of the two cells.
        y: Row of the cell under the wall.
        path_cells: Cells of the path to draw (empty if hidden).
        palette: Colours of the walls and of the "42".

    Returns:
        The colour of the wall, or None if it is open.
    """
    if y == 0 or y == maze.height or not maze.is_open(x, y - 1, SOUTH):
        return palette.wall
    if (x, y - 1) in path_cells and (x, y) in path_cells:
        return PATH_COLOUR
    return None
