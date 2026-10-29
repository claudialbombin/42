"""Everything related to the configuration file."""

from parsing.errors import ConfigError
from parsing.maze_config import MazeConfig
from parsing.parser import read_config

__all__ = ["ConfigError", "MazeConfig", "read_config"]
