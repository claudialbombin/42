"""Recursive backtracker (random depth first search)."""

import random
from typing import List, Set

from mazegen.constants import Cell
from mazegen.grid import MazeGrid


def carve_backtracker(grid: MazeGrid, start: Cell,
                      rng: random.Random) -> None:
    """Carve a perfect maze with a random depth first search.

    1. Start at start and mark it as visited.
    2. Pick a random neighbour not visited yet, open the wall and go
       there.
    3. If there is none, go back to the previous cell.

    I use a list as a stack instead of real recursion, because with a
    200x200 maze Python would hit the recursion limit.

    Args:
        grid: Grid with every wall closed.
        start: Cell where the search starts.
        rng: Random generator (created from the seed).
    """
    visited: Set[Cell] = {start}
    stack: List[Cell] = [start]
    while stack:
        x, y = stack[-1]
        options = []
        for direction, nx, ny in grid.free_neighbours(x, y):
            if (nx, ny) not in visited:
                options.append((direction, nx, ny))
        if not options:
            stack.pop()
            continue
        direction, nx, ny = rng.choice(options)
        grid.carve(x, y, direction)
        visited.add((nx, ny))
        stack.append((nx, ny))
