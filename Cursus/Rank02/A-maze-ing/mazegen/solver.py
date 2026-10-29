"""Find the shortest path between two cells of the maze."""

from collections import deque
from typing import Deque, Dict, List, Optional

from mazegen.constants import LETTERS, MOVES, Cell
from mazegen.grid import MazeGrid


def find_path(grid: MazeGrid, start: Cell, end: Cell) -> List[Cell]:
    """Find the shortest path from start to end with a BFS.

    BFS visits the cells by distance, so the first time we reach end it
    is with the shortest path. I save where every cell comes from and
    then walk back from end to start.

    Args:
        grid: Grid of the maze, already generated.
        start: First cell of the path (the entry).
        end: Last cell of the path (the exit).

    Returns:
        The list of cells, start and end included. Empty if there is no
        path (it can't happen in a valid maze).
    """
    came_from: Dict[Cell, Optional[Cell]] = {start: None}
    queue: Deque[Cell] = deque([start])
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for direction, (dx, dy) in MOVES.items():
            nxt = (x + dx, y + dy)
            if grid.is_open(x, y, direction) and nxt not in came_from:
                came_from[nxt] = (x, y)
                queue.append(nxt)
    if end not in came_from:
        return []
    path: List[Cell] = []
    current: Optional[Cell] = end
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


def path_to_letters(path: List[Cell]) -> str:
    """Convert a list of cells into the letters of the output file.

    For each pair of consecutive cells I look which move goes from the
    first one to the second one and write its letter.

    Args:
        path: Cells of the path, in order.

    Returns:
        A string of N, E, S, W (empty if the path has 0 or 1 cell).
    """
    letters = []
    for i in range(len(path) - 1):
        x, y = path[i]
        nx, ny = path[i + 1]
        for direction, (dx, dy) in MOVES.items():
            if (x + dx, y + dy) == (nx, ny):
                letters.append(LETTERS[direction])
    return "".join(letters)
