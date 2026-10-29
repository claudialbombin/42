"""Constants shared by every file of the mazegen package.

Each wall of a cell is one bit of an integer, with the same values as
in the output file of the subject:

    bit 0 (1) = North, bit 1 (2) = East, bit 2 (4) = South, bit 3 (8) = West

So 15 (0b1111) is a cell with its four walls closed.
"""

from typing import Dict, List, Tuple

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8
ALL_WALLS = NORTH | EAST | SOUTH | WEST

# How to move (dx, dy) to reach the neighbour behind each wall
MOVES: Dict[int, Tuple[int, int]] = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0),
}
# The same wall seen from the neighbour
OPPOSITE: Dict[int, int] = {NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST}
# Letters used to write the solution
LETTERS: Dict[int, str] = {NORTH: "N", EAST: "E", SOUTH: "S", WEST: "W"}

# The "42" drawn in the middle of the maze. "#" is a fully closed cell.
PATTERN_42: List[str] = [
    "#.#.###",
    "#.#...#",
    "###.###",
    "..#.#..",
    "..#.###",
]

ALGORITHMS: Tuple[str, ...] = ("backtracker", "prim")
MIN_SIZE = 2
MAX_SIZE = 200
# A Pac-Man board needs at least this number of independent routes
MIN_LOOPS = 2

# A cell is always written as (x, y): x = column, y = row
Cell = Tuple[int, int]
