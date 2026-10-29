"""Draw the maze while it is being generated (bonus)."""

import time
from typing import Optional

from display.terminal import TerminalDisplay
from mazegen import MazeGenerator

# Time between two frames (seconds)
ANIMATION_DELAY = 0.01
# Maximum number of frames, so big mazes don't take forever
MAX_FRAMES = 300


def animate(display: TerminalDisplay, maze: MazeGenerator,
            seed: Optional[int] = None) -> None:
    """Generate the maze and draw a frame every few opened walls.

    The generator calls on_step() every time it opens a wall. Drawing
    after every single wall is too slow for big mazes, so I only draw
    one frame every "every" steps.

    Args:
        display: Where the frames are drawn.
        maze: The maze to generate.
        seed: New seed, or None to keep the one of the maze.
    """
    every = max(1, (maze.width * maze.height) // MAX_FRAMES)
    steps = [0]
    # the old path does not match the new maze, so hide it for now
    old_show_path = display.show_path
    display.show_path = False

    def on_step() -> None:
        """Count one opened wall and draw a frame if it is time.

        steps is a list and not an int so this inner function can
        change it (an int would need "nonlocal").
        """
        steps[0] += 1
        if steps[0] % every == 0:
            display.draw(maze, "Generating...")
            time.sleep(ANIMATION_DELAY)

    maze.generate(seed, on_step)
    display.show_path = old_show_path
