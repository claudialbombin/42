"""The program itself: glue between config, generator, file and display."""

from app.menu import run_menu
from app.session import MazeSession

__all__ = ["MazeSession", "run_menu"]
