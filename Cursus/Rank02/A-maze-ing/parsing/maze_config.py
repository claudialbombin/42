"""The options of the configuration file, already converted."""

from dataclasses import dataclass
from typing import Optional, Tuple

MANDATORY_KEYS: Tuple[str, ...] = (
    "WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT",
)
# Extra keys I added (the subject allows it)
OPTIONAL_KEYS: Tuple[str, ...] = ("SEED", "ALGORITHM", "ANIMATION")


@dataclass
class MazeConfig:
    """All the options read from the configuration file."""

    width: int
    height: int
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    output_file: str
    perfect: bool
    seed: Optional[int] = None
    algorithm: str = "backtracker"
    animation: bool = False
