"""mazegen - reusable maze generator made for the A-Maze-ing project.

Basic use:

    from mazegen import MazeGenerator

    maze = MazeGenerator(20, 15, seed=42)
    maze.generate()
    print(maze.get_solution())
"""

from mazegen.constants import ALGORITHMS, EAST, NORTH, SOUTH, WEST
from mazegen.generator import MazeGenerator

__all__ = ["MazeGenerator", "ALGORITHMS", "NORTH", "EAST", "SOUTH", "WEST"]
__version__ = "1.0.0"
