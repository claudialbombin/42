"""Texts shown to the user."""

from mazegen import MazeGenerator

MENU = """=== A-Maze-ing ===
1. Re-generate a new maze
2. Show / Hide the shortest path
3. Rotate the wall colours
4. Rotate the "42" colours
5. Quit"""

USAGE = "Usage: python3 a_maze_ing.py <config_file>"

NO_PATTERN = ("Error: the maze is too small to draw the '42' pattern, "
              "it was omitted.")


def info_text(maze: MazeGenerator) -> str:
    """Build the information printed under the maze.

    It shows the seed (so a maze can be generated again), the size,
    the mode, the algorithm and the length of the shortest path. If
    the "42" did not fit, the error is added here too.

    Args:
        maze: The maze that is shown.

    Returns:
        The text to print, one or two lines.
    """
    mode = "perfect" if maze.perfect else "Pac-Man board"
    text = (f"Seed: {maze.seed} | {maze.width}x{maze.height} | {mode} | "
            f"algorithm: {maze.algorithm} | path: {len(maze.path) - 1} steps")
    # the error has to stay visible, the screen is cleared at every draw
    if not maze.has_pattern:
        text += "\n" + NO_PATTERN
    return text
