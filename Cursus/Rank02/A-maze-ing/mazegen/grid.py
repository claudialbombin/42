"""MazeGrid: the walls of the maze and the basic operations on them.

This file only knows about walls and cells. It does not know how a maze
is generated or solved, the other files of the package do that using
the methods of this class.
"""

from typing import Callable, List, Optional, Set, Tuple

from mazegen.constants import ALL_WALLS, EAST, MOVES, OPPOSITE, SOUTH, Cell


class MazeGrid:
    """Grid of cells where every cell starts with its four walls closed.

    Attributes:
        width: Number of columns.
        height: Number of rows.
        cells: cells[y][x] is an int with the closed walls of the cell.
        pattern: Cells of the "42", they are never opened.
        on_step: Optional function called every time a wall is opened
            (used to animate the generation).
    """

    def __init__(self, width: int, height: int, pattern: Set[Cell]) -> None:
        """Create a grid with every wall of every cell closed.

        All the cells start at ALL_WALLS (15), so the algorithms only
        have to open walls, never close them.

        Args:
            width: Number of columns.
            height: Number of rows.
            pattern: Cells of the "42" (they will never be opened).
        """
        self.width = width
        self.height = height
        self.pattern = pattern
        self.on_step: Optional[Callable[[], None]] = None
        self.cells: List[List[int]] = []
        for _ in range(height):
            self.cells.append([ALL_WALLS] * width)

    def inside(self, x: int, y: int) -> bool:
        """Tell if a position is inside the grid.

        Used before touching a neighbour, so we never go out of the
        list (Python would not crash with -1, it would take the last
        element, which is even worse).

        Args:
            x: Column of the position.
            y: Row of the position.

        Returns:
            True if (x, y) is inside the grid, False otherwise.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, x: int, y: int) -> bool:
        """Tell if a cell can be used by the maze.

        A cell is free when it is inside the grid and it is not one of
        the closed cells that draw the "42".

        Args:
            x: Column of the cell.
            y: Row of the cell.

        Returns:
            True if the cell is inside and not part of the "42".
        """
        return self.inside(x, y) and (x, y) not in self.pattern

    def is_open(self, x: int, y: int, direction: int) -> bool:
        """Tell if one wall of a cell is open.

        A wall is open when its bit is 0, so I check the bit with an
        "and" between the cell and the direction.

        Args:
            x: Column of the cell.
            y: Row of the cell.
            direction: NORTH, EAST, SOUTH or WEST.

        Returns:
            True if the wall is open, False if it is closed.
        """
        return not self.cells[y][x] & direction

    def set_wall(self, x: int, y: int, direction: int, closed: bool) -> None:
        """Open or close a wall on both sides, so the data stays coherent.

        If I only changed one cell, the neighbour would still have its
        wall and the output file would be wrong. The neighbour must be
        inside the grid (the callers check it before).

        Args:
            x: Column of the cell.
            y: Row of the cell.
            direction: Wall to change (NORTH, EAST, SOUTH or WEST).
            closed: True to close the wall, False to open it.
        """
        dx, dy = MOVES[direction]
        other = OPPOSITE[direction]
        if closed:
            self.cells[y][x] |= direction
            self.cells[y + dy][x + dx] |= other
        else:
            self.cells[y][x] &= ~direction
            self.cells[y + dy][x + dx] &= ~other

    def carve(self, x: int, y: int, direction: int) -> None:
        """Open a wall for good and tell the display.

        It is the same as set_wall(..., False) but it also calls
        on_step (if there is one), which is what makes the animation.

        Args:
            x: Column of the cell.
            y: Row of the cell.
            direction: Wall to open (NORTH, EAST, SOUTH or WEST).
        """
        self.set_wall(x, y, direction, False)
        if self.on_step is not None:
            self.on_step()

    def count_openings(self, x: int, y: int) -> int:
        """Count the open walls of a cell.

        A cell with only one opening is a dead-end, this is used by
        braid.py to find them.

        Args:
            x: Column of the cell.
            y: Row of the cell.

        Returns:
            The number of open walls, between 0 and 4.
        """
        count = 0
        for direction in MOVES:
            if self.is_open(x, y, direction):
                count += 1
        return count

    def free_neighbours(self, x: int, y: int) -> List[Tuple[int, int, int]]:
        """List the neighbours of a cell that can be used by the maze.

        The border and the "42" cells are skipped, so the algorithms
        never open a wall towards them.

        Args:
            x: Column of the cell.
            y: Row of the cell.

        Returns:
            A list of (direction, nx, ny): the direction to go there and
            the position of the neighbour.
        """
        result = []
        for direction, (dx, dy) in MOVES.items():
            if self.is_free(x + dx, y + dy):
                result.append((direction, x + dx, y + dy))
        return result

    def count_loops(self) -> int:
        """Count the independent loops of the maze.

        In a connected graph: loops = edges - cells + 1. A perfect maze
        is a tree (edges = cells - 1), so it has 0 loops. I only look at
        the EAST and SOUTH walls so every passage is counted once.

        Returns:
            The number of independent loops (0 for a perfect maze).
        """
        cells = 0
        edges = 0
        for y in range(self.height):
            for x in range(self.width):
                if not self.is_free(x, y):
                    continue
                cells += 1
                if x + 1 < self.width and self.is_open(x, y, EAST):
                    edges += 1
                if y + 1 < self.height and self.is_open(x, y, SOUTH):
                    edges += 1
        return edges - cells + 1
