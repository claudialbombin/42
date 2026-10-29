"""Convert the text values of the config file to Python types."""

from typing import Tuple

from parsing.errors import ConfigError


def to_int(key: str, text: str) -> int:
    """Convert a value of the config file to an int.

    int() already accepts spaces and a sign, so "-3" or " 20 " work.
    The key is only used to write a clear error message.

    Args:
        key: Name of the key (for the error message).
        text: Value to convert.

    Returns:
        The value as an int.

    Raises:
        ConfigError: If the text is not an integer.
    """
    try:
        return int(text)
    except ValueError:
        raise ConfigError(f"{key} must be an integer (got '{text}')")


def to_coords(key: str, text: str) -> Tuple[int, int]:
    """Convert a value like "x,y" to a tuple (x, y).

    The value is split on the comma and each part is converted with
    to_int(). If they are not inside the maze it is checked later by
    the generator, here I only check the format.

    Args:
        key: Name of the key (for the error message).
        text: Value to convert, for example "19,14".

    Returns:
        The tuple (x, y).

    Raises:
        ConfigError: If there are not exactly two integers.
    """
    parts = text.split(",")
    if len(parts) != 2:
        raise ConfigError(f"{key} must look like x,y (got '{text}')")
    x = to_int(key, parts[0].strip())
    y = to_int(key, parts[1].strip())
    return (x, y)


def to_bool(key: str, text: str) -> bool:
    """Convert "True" or "False" (any case) to a bool.

    I don't use bool(text) because bool("False") is True in Python.

    Args:
        key: Name of the key (for the error message).
        text: Value to convert.

    Returns:
        True or False.

    Raises:
        ConfigError: If the text is not true or false.
    """
    if text.lower() == "true":
        return True
    if text.lower() == "false":
        return False
    raise ConfigError(f"{key} must be True or False (got '{text}')")
