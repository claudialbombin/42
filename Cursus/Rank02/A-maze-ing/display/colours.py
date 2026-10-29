"""Colours and ANSI codes used by the display.

The numbers are colours of the 256 colour ANSI palette.
"""

from typing import List, Optional

RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

# The user can rotate through these two lists with the menu
WALL_COLOURS: List[int] = [252, 39, 114, 214, 170, 196]
PATTERN_COLOURS: List[int] = [245, 220, 51, 201, 118]

PATH_COLOUR = 44
ENTRY_COLOUR = 201
EXIT_COLOUR = 160


def block(colour: Optional[int]) -> str:
    """Build the text of one pixel of the drawing.

    A pixel is two spaces with a background colour. Two spaces because
    a character is about twice as tall as wide, so this way the pixels
    look square. RESET is added after, so the colour does not "leak"
    to the next characters.

    Args:
        colour: Colour of the 256 colour palette, or None for an empty
            pixel (the background of the terminal).

    Returns:
        The string to print for this pixel.
    """
    if colour is None:
        return "  "
    return f"\033[48;5;{colour}m  {RESET}"
