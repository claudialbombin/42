from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is used on an incompatible Creature."""


class BattleStrategy(ABC):
    """A way for a Creature to act during one tournament battle."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if creature is suitable for this strategy."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Make creature act according to this strategy."""


class NormalStrategy(BattleStrategy):
    """Suitable for any Creature: just attack."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Suitable for Creature with transform capabilities."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    """Suitable for Creature with healing capabilities."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
