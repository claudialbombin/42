"""Algorithms that carve a perfect maze in a MazeGrid."""

from mazegen.algorithms.backtracker import carve_backtracker
from mazegen.algorithms.prim import carve_prim

__all__ = ["carve_backtracker", "carve_prim"]
