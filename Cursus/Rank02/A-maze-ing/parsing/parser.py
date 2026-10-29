"""Build a MazeConfig from the configuration file.

This is the only function the rest of the program needs:
reader.py gives the pairs, converters.py converts the values.
"""

from parsing.converters import to_bool, to_coords, to_int
from parsing.errors import ConfigError
from parsing.maze_config import MANDATORY_KEYS, MazeConfig
from parsing.reader import read_pairs


def read_config(path: str) -> MazeConfig:
    """Read the configuration file and return its options.

    First the file is split in pairs (reader.py), then I check that
    every mandatory key is there and convert the values
    (converters.py). The optional keys keep their default value if
    they are not in the file.

    Args:
        path: Path of the configuration file.

    Returns:
        A MazeConfig with every value already converted.

    Raises:
        ConfigError: If the file can't be read or a value is wrong.
    """
    values = read_pairs(path)
    for key in MANDATORY_KEYS:
        if key not in values:
            raise ConfigError(f"missing mandatory key '{key}'")
    config = MazeConfig(
        width=to_int("WIDTH", values["WIDTH"]),
        height=to_int("HEIGHT", values["HEIGHT"]),
        entry=to_coords("ENTRY", values["ENTRY"]),
        exit=to_coords("EXIT", values["EXIT"]),
        output_file=values["OUTPUT_FILE"],
        perfect=to_bool("PERFECT", values["PERFECT"]),
    )
    if "SEED" in values:
        config.seed = to_int("SEED", values["SEED"])
    if "ALGORITHM" in values:
        config.algorithm = values["ALGORITHM"].lower()
    if "ANIMATION" in values:
        config.animation = to_bool("ANIMATION", values["ANIMATION"])
    if config.output_file == path:
        raise ConfigError("OUTPUT_FILE can't be the config file itself")
    return config
