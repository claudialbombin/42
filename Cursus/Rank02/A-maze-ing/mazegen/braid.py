"""Turn a perfect maze into a Pac-Man board (PERFECT=False).

Starting from a perfect maze:
    1. braid(): open one more wall in every dead-end (bonus: none left).
    2. add_loops(): make sure there are at least MIN_LOOPS loops.
The only dead-ends that stay are the ones closed by the "42" and the
border, because those walls can't be opened.
"""

import random
from typing import List, Tuple

from mazegen.constants import EAST, MIN_LOOPS, MOVES, SOUTH, Cell
from mazegen.grid import MazeGrid
from mazegen.open_area import try_open


def braid(grid: MazeGrid, rng: random.Random) -> None:
    """Remove the dead-ends of the maze by opening one wall in each.

    The dead-ends are visited in a random order. For each one I try to
    open a wall towards a neighbour that is also a dead-end first,
    because it removes two dead-ends at once. If no wall can be opened
    (3x3 rule, "42" or border) the dead-end stays.

    Args:
        grid: Grid with a perfect maze already carved.
        rng: Random generator (created from the seed).
    """
    dead_ends = _find_dead_ends(grid)
    rng.shuffle(dead_ends)
    for x, y in dead_ends:
        # it may have been fixed already by a neighbour
        if grid.count_openings(x, y) != 1:
            continue
        best = []
        others = []
        for direction, nx, ny in grid.free_neighbours(x, y):
            if grid.is_open(x, y, direction):
                continue
            if grid.count_openings(nx, ny) == 1:
                best.append(direction)
            else:
                others.append(direction)
        rng.shuffle(best)
        rng.shuffle(others)
        for direction in best + others:
            if try_open(grid, x, y, direction):
                break


def add_loops(grid: MazeGrid, rng: random.Random) -> None:
    """Open random walls until the maze has at least MIN_LOOPS loops.

    After braid() this is almost always true already, but on very small
    mazes it may not be. I go through all the inner walls in a random
    order and open them (respecting the 3x3 rule) until it is enough.

    Args:
        grid: Grid of the maze, already braided.
        rng: Random generator (created from the seed).

    Raises:
        ValueError: If it is impossible (should not happen after the
            checks done before generating).
    """
    walls = _inner_walls(grid)
    rng.shuffle(walls)
    for x, y, direction in walls:
        if grid.count_loops() >= MIN_LOOPS:
            return
        if not grid.is_open(x, y, direction):
            try_open(grid, x, y, direction)
    if grid.count_loops() < MIN_LOOPS:
        raise ValueError("could not create enough loops in this maze")


def _find_dead_ends(grid: MazeGrid) -> List[Cell]:
    """Find all the dead-ends of the maze.

    A dead-end is a free cell with only one open wall.

    Args:
        grid: Grid of the maze.

    Returns:
        The list of the (x, y) dead-end cells.
    """
    dead_ends = []
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.is_free(x, y) and grid.count_openings(x, y) == 1:
                dead_ends.append((x, y))
    return dead_ends


def _inner_walls(grid: MazeGrid) -> List[Tuple[int, int, int]]:
    """List every wall between two free cells.

    I only take the EAST and SOUTH walls of each cell, so each wall
    appears only once in the list (the WEST wall of a cell is the EAST
    wall of the one on its left).

    Args:
        grid: Grid of the maze.

    Returns:
        A list of (x, y, direction), one for each inner wall.
    """
    walls = []
    for y in range(grid.height):
        for x in range(grid.width):
            for direction in (EAST, SOUTH):
                dx, dy = MOVES[direction]
                if grid.is_free(x, y) and grid.is_free(x + dx, y + dy):
                    walls.append((x, y, direction))
    return walls
