"""Interactive menu shown under the maze."""

import random

from app.messages import MENU, info_text
from app.session import MazeSession


def run_menu(session: MazeSession) -> None:
    """Show the maze and the menu until the user wants to quit.

    Each turn the maze is drawn again with the menu under it, then
    the choice is read. Ctrl-C or Ctrl-D also quit, without any
    traceback.

    Args:
        session: The config, the maze and the display.

    Raises:
        OutputError: If the output file can't be written.
    """
    while True:
        session.display.draw(session.maze,
                             info_text(session.maze) + "\n\n" + MENU)
        try:
            choice = input("Choice? (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if choice == "5":
            return
        _do_choice(session, choice)


def _do_choice(session: MazeSession, choice: str) -> None:
    """Do the action of one menu option.

    A wrong choice does nothing: the menu is simply shown again. Option
    5 (quit) is handled in run_menu() because it has to stop the loop.

    Args:
        session: The config, the maze and the display.
        choice: What the user typed, without spaces.

    Raises:
        OutputError: If option 1 can't write the output file.
    """
    if choice == "1":
        # new random seed, it is printed so the maze can be made again
        session.new_maze(random.randint(0, 999999))
    elif choice == "2":
        session.display.show_path = not session.display.show_path
    elif choice == "3":
        session.display.next_wall_colour()
    elif choice == "4":
        session.display.next_pattern_colour()
