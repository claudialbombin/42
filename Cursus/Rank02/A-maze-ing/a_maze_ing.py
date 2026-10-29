"""A-Maze-ing: generate a maze from a config file and show it.

Usage:
    python3 a_maze_ing.py config.txt

This file only calls the other parts of the project:
    parsing/  -> read the config file
    mazegen/  -> generate the maze (reusable package)
    output/   -> write the output file
    display/  -> draw the maze in the terminal
    app/      -> the menu and the session
"""

import sys

from app import MazeSession, run_menu
from app.messages import NO_PATTERN, USAGE
from output import OutputError
from parsing import ConfigError, read_config


def main() -> int:
    """Read the config, generate the maze and start the menu.

    Returns:
        0 if everything went well, 1 if there was an error.
    """
    if len(sys.argv) != 2:
        print(USAGE)
        return 1
    try:
        config = read_config(sys.argv[1])
        session = MazeSession(config)
        if not session.maze.has_pattern:
            print(NO_PATTERN)
        session.new_maze(session.maze.seed)
        run_menu(session)
    except ConfigError as error:
        print(f"Error in config file: {error}")
        return 1
    except ValueError as error:
        print(f"Error: impossible maze: {error}")
        return 1
    except OutputError as error:
        print(f"Error: {error}")
        return 1
    except KeyboardInterrupt:
        print("\nBye!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
