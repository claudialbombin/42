# Only the factories are exposed here: concrete Creature classes
# (Flameling, Pyrodon...) stay internal to the package.
from .factory import AquaFactory, CreatureFactory, FlameFactory

__all__ = ["AquaFactory", "CreatureFactory", "FlameFactory"]
