"""MazeSession: everything needed while the program is running.

It keeps together the config, the generator and the display, so the
menu only has to call new_maze() without knowing the details.
"""

from display import TerminalDisplay, animate
from mazegen import MazeGenerator
from output import write_maze
from parsing import MazeConfig


class MazeSession:
    """The config, the maze and the display of one run of the program.

    Attributes:
        config: Options read from the config file.
        maze: The maze generator.
        display: The terminal display.
    """

    def __init__(self, config: MazeConfig) -> None:
        """Create the generator and the display from the config.

        The maze is not generated here, only created and checked, so
        a wrong config fails before anything is shown.

        Args:
            config: Options read from the config file.

        Raises:
            ValueError: If the options can't give a valid maze.
        """
        self.config = config
        self.maze = MazeGenerator(config.width, config.height,
                                  config.entry, config.exit,
                                  config.perfect, config.seed,
                                  config.algorithm)
        self.display = TerminalDisplay()

    def new_maze(self, seed: int) -> None:
        """Generate a maze (animated or not) and save it in the file.

        The file is written again every time, so it always matches
        what is on the screen.

        Args:
            seed: Seed of the new maze.

        Raises:
            OutputError: If the output file can't be written.
        """
        if self.config.animation:
            animate(self.display, self.maze, seed)
        else:
            self.maze.generate(seed)
        write_maze(self.maze, self.config.output_file)
