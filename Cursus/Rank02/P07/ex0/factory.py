from abc import ABC, abstractmethod

from .creature import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """Builds the base and evolved Creature of one family."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base Creature of this family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved Creature of this family."""


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
