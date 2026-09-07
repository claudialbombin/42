from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Standalone capability: healing does not depend on Creature."""

    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        """Return a message describing the healing performed."""


class TransformCapability(ABC):
    """Standalone capability: transforming keeps a persistent state
    that impacts the attack of the Creature using it."""

    def __init__(self) -> None:
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Return a message describing the transformation."""

    @abstractmethod
    def revert(self) -> str:
        """Return a message describing reverting to normal form."""
