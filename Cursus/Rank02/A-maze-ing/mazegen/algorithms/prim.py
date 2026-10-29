"""Randomized Prim algorithm (bonus: second generation algorithm)."""

import random
from typing import List, Set, Tuple

from mazegen.constants import MOVES, Cell
from mazegen.grid import MazeGrid

# A wall of the frontier: (x, y, direction)
Wall = Tuple[int, int, int]


def carve_prim(grid: MazeGrid, start: Cell, rng: random.Random) -> None:
    """Carve a perfect maze growing it from start, one wall at a time.

    The frontier is the list of walls between a visited cell and a cell
    that is not visited yet. Each turn I take one of them at random: if
    the cell behind it is still not visited, I open the wall.
    It gives shorter corridors and more branches than the backtracker.

    Args:
        grid: Grid with every wall closed.
        start: Cell where the maze starts to grow.
        rng: Random generator (created from the seed).
    """
    visited: Set[Cell] = {start}
    frontier: List[Wall] = []
    _add_frontier(grid, start, frontier)
    while frontier:
        # swap with the last one so pop() is fast
        index = rng.randrange(len(frontier))
        frontier[index], frontier[-1] = frontier[-1], frontier[index]
        x, y, direction = frontier.pop()
        dx, dy = MOVES[direction]
        if (x + dx, y + dy) in visited:
            continue
        grid.carve(x, y, direction)
        visited.add((x + dx, y + dy))
        _add_frontier(grid, (x + dx, y + dy), frontier)


def _add_frontier(grid: MazeGrid, cell: Cell, frontier: List[Wall]) -> None:
    """Add the walls around a newly visited cell to the frontier.

    I add all its free neighbours, even the visited ones: carve_prim()
    skips them later, it is simpler than checking here.

    Args:
        grid: Grid of the maze.
        cell: Cell that was just visited.
        frontier: List of walls, modified in place.
    """
    x, y = cell
    for direction, _, _ in grid.free_neighbours(x, y):
        frontier.append((x, y, direction))
