"""Read the configuration file and split it in KEY=VALUE pairs.

This file does not convert anything, it only checks the syntax of the
lines. The values are converted later in converters.py.
"""

from typing import Dict, List, Tuple

from parsing.errors import ConfigError
from parsing.maze_config import MANDATORY_KEYS, OPTIONAL_KEYS


def read_pairs(path: str) -> Dict[str, str]:
    """Read the file and return its KEY=VALUE pairs.

    Empty lines and lines starting with '#' are ignored. A key can
    only appear once, otherwise we would not know which value to use.

    Args:
        path: Path of the configuration file.

    Returns:
        A dict KEY -> VALUE, the values are still text.

    Raises:
        ConfigError: If the file can't be read or a line is wrong.
    """
    values: Dict[str, str] = {}
    for number, line in enumerate(_read_lines(path), start=1):
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        key, value = _split_line(line, number)
        if key in values:
            raise ConfigError(f"line {number}: key '{key}' is repeated")
        values[key] = value
    return values


def _read_lines(path: str) -> List[str]:
    """Read all the lines of the file.

    The file is opened with "with" so it is always closed, even if
    something fails. Each possible error gets its own message.

    Args:
        path: Path of the configuration file.

    Returns:
        The lines of the file (with their '\\n').

    Raises:
        ConfigError: If the file does not exist, is a directory, can't
            be read or is not a text file.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        raise ConfigError(f"config file '{path}' not found")
    except IsADirectoryError:
        raise ConfigError(f"'{path}' is a directory, not a config file")
    except PermissionError:
        raise ConfigError(f"no permission to read '{path}'")
    except UnicodeDecodeError:
        raise ConfigError(f"'{path}' is not a text file")
    except OSError as error:
        raise ConfigError(f"can't read '{path}': {error.strerror}")


def _split_line(line: str, number: int) -> Tuple[str, str]:
    """Split one "KEY=VALUE" line and check it.

    I split only on the first '=' so a value could contain another
    one. The key is put in uppercase so "width=10" also works.

    Args:
        line: The line, already stripped and not a comment.
        number: Line number in the file (for the error message).

    Returns:
        The tuple (KEY, VALUE).

    Raises:
        ConfigError: If there is no '=', the key is unknown or the
            value is empty.
    """
    if "=" not in line:
        raise ConfigError(f"line {number}: expected KEY=VALUE, "
                          f"got '{line}'")
    key, value = line.split("=", 1)
    key = key.strip().upper()
    value = value.strip()
    if key not in MANDATORY_KEYS and key not in OPTIONAL_KEYS:
        raise ConfigError(f"line {number}: unknown key '{key}'")
    if value == "":
        raise ConfigError(f"line {number}: '{key}' has no value")
    return key, value
