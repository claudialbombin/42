"""MazeGenerator: the class to use from outside the package.

It does not do the work itself, it calls the other files:
    checks.py     -> check the parameters
    pattern.py    -> place the "42"
    algorithms/   -> carve a perfect maze
    braid.py      -> turn it into a Pac-Man board (PERFECT=False)
    solver.py     -> find the shortest path
"""

import random
from typing import Callable, List, Optional, Set

from mazegen import checks
from mazegen.algorithms import carve_backtracker, carve_prim
from mazegen.braid import add_loops, braid
from mazegen.constants import Cell
from mazegen.grid import MazeGrid
from mazegen.pattern import pattern_cells
from mazegen.solver import find_path, path_to_letters


class MazeGenerator:
    """Generate a random maze with a "42" drawn in the middle.

    With perfect=True the maze is a perfect maze (only one path between
    any two cells). With perfect=False it is a board for a Pac-Man like
    game: fully connected, with loops and no dead-ends.

    Attributes:
        width: Number of columns.
        height: Number of rows.
        entry_pos: Entry cell as (x, y).
        exit_pos: Exit cell as (x, y).
        perfect: True for a perfect maze, False for a Pac-Man board.
        seed: Seed of the last generation (same seed = same maze).
        algorithm: "backtracker" or "prim".
        pattern: Set of (x, y) cells used to draw the "42".
        has_pattern: False when the maze is too small for the "42".
        path: Cells of the shortest path from entry to exit.
    """

    def __init__(self, width: int, height: int,
                 entry_pos: Cell = (0, 0),
                 exit_pos: Optional[Cell] = None,
                 perfect: bool = True,
                 seed: Optional[int] = None,
                 algorithm: str = "backtracker") -> None:
        """Save and check the parameters of the maze.

        Args:
            width: Number of columns (between 2 and 200).
            height: Number of rows (between 2 and 200).
            entry_pos: Entry cell (x, y). Top left corner by default.
            exit_pos: Exit cell (x, y). Bottom right corner by default.
            perfect: If True, only one path between entry and exit.
            seed: Seed for the random generator. Random if None.
            algorithm: "backtracker" (default) or "prim".

        Raises:
            ValueError: If the parameters can't give a valid maze.
        """
        checks.check_size(width, height)
        checks.check_algorithm(algorithm)
        if exit_pos is None:
            exit_pos = (width - 1, height - 1)
        if seed is None:
            seed = random.randint(0, 999999)
        self.width = width
        self.height = height
        self.entry_pos = entry_pos
        self.exit_pos = exit_pos
        self.perfect = perfect
        self.seed = seed
        self.algorithm = algorithm
        self.pattern: Set[Cell] = pattern_cells(width, height)
        self.has_pattern = len(self.pattern) > 0
        self.path: List[Cell] = []
        self._grid = MazeGrid(width, height, self.pattern)
        checks.check_cells(self._grid, entry_pos, exit_pos)
        if not perfect:
            checks.check_loops_possible(self._grid)

    def generate(self, seed: Optional[int] = None,
                 on_step: Optional[Callable[[], None]] = None) -> None:
        """Generate a new maze and its shortest path.

        A new empty grid is created every time, then the algorithm
        carves a perfect maze. For a non perfect maze the dead-ends are
        removed after. At the end the shortest path is saved in path.

        Args:
            seed: New seed to use. If None the saved seed is used again,
                so calling generate() twice gives the same maze.
            on_step: Optional function called each time a wall is
                opened. The display uses it to animate the generation.

        Raises:
            ValueError: If a non perfect maze can't get enough loops
                (should not happen, it is checked in __init__).
        """
        if seed is not None:
            self.seed = seed
        rng = random.Random(self.seed)
        self._grid = MazeGrid(self.width, self.height, self.pattern)
        self._grid.on_step = on_step
        if self.algorithm == "prim":
            carve_prim(self._grid, self.entry_pos, rng)
        else:
            carve_backtracker(self._grid, self.entry_pos, rng)
        if not self.perfect:
            braid(self._grid, rng)
            add_loops(self._grid, rng)
        self._grid.on_step = None
        self.path = find_path(self._grid, self.entry_pos, self.exit_pos)

    @property
    def grid(self) -> List[List[int]]:
        """Give access to the walls of the maze.

        It is a property so the user can write maze.grid[y][x] without
        knowing that the real data is inside a MazeGrid object.

        Returns:
            The grid as a list of rows, grid[y][x] being an int with
            the closed walls of the cell (1 N, 2 E, 4 S, 8 W).
        """
        return self._grid.cells

    def is_open(self, x: int, y: int, direction: int) -> bool:
        """Return True if you can go from (x, y) in that direction.

        Args:
            x: Column of the cell.
            y: Row of the cell.
            direction: NORTH, EAST, SOUTH or WEST.

        Returns:
            True if the wall is open, False if it is closed.
        """
        return self._grid.is_open(x, y, direction)

    def count_loops(self) -> int:
        """Count the independent loops of the maze.

        Useful to check the mode: a perfect maze has 0 loops and a
        Pac-Man board has at least MIN_LOOPS.

        Returns:
            The number of independent loops.
        """
        return self._grid.count_loops()

    def get_solution(self) -> str:
        """Give the shortest path from the entry to the exit.

        The path is computed in generate(), here it is only converted
        to letters, like in the output file.

        Returns:
            A string of N, E, S, W.
        """
        return path_to_letters(self.path)

    def to_hex_lines(self) -> List[str]:
        """Convert the grid to the text format of the output file.

        Each cell is written as one uppercase hexadecimal digit (its
        value is between 0 and 15).

        Returns:
            One string per row of the maze.
        """
        lines = []
        for row in self._grid.cells:
            lines.append("".join(format(cell, "X") for cell in row))
        return lines
