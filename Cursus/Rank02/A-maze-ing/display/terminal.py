"""TerminalDisplay: remember the display options and print the maze."""

import sys
from typing import Set, Tuple

from display.colours import CLEAR, PATTERN_COLOURS, WALL_COLOURS, block
from display.pixels import Palette, pixel_colour
from mazegen import MazeGenerator


class TerminalDisplay:
    """Print the maze and keep the options chosen in the menu.

    Attributes:
        wall_index: Current colour of the walls in WALL_COLOURS.
        pattern_index: Current colour of the "42" in PATTERN_COLOURS.
        show_path: True if the shortest path has to be drawn.
    """

    def __init__(self) -> None:
        """Start with the first colours of the lists and the path hidden.

        The path is hidden at the start so the user can try to solve
        the maze first.
        """
        self.wall_index = 0
        self.pattern_index = 0
        self.show_path = False

    def next_wall_colour(self) -> None:
        """Change the walls to the next colour of WALL_COLOURS.

        The modulo makes it go back to the first colour after the last
        one, so the user can rotate forever.
        """
        self.wall_index = (self.wall_index + 1) % len(WALL_COLOURS)

    def next_pattern_colour(self) -> None:
        """Change the "42" to the next colour of PATTERN_COLOURS.

        Same as next_wall_colour(), with its own list and index.
        """
        self.pattern_index = (self.pattern_index + 1) % len(PATTERN_COLOURS)

    def draw(self, maze: MazeGenerator, info: str = "") -> None:
        """Clear the terminal and print the maze.

        Everything is joined in one string and printed at once, so the
        screen does not blink (important for the animation).

        Args:
            maze: The maze to draw.
            info: Optional text printed under the maze.
        """
        palette = Palette(WALL_COLOURS[self.wall_index],
                          PATTERN_COLOURS[self.pattern_index])
        path_cells: Set[Tuple[int, int]] = set()
        if self.show_path:
            path_cells = set(maze.path)
        lines = []
        for py in range(2 * maze.height + 1):
            line = ""
            for px in range(2 * maze.width + 1):
                line += block(pixel_colour(maze, px, py, path_cells,
                                           palette))
            lines.append(line)
        text = CLEAR + "\n".join(lines) + "\n"
        if info:
            text += info + "\n"
        sys.stdout.write(text)
        sys.stdout.flush()
