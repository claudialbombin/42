from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    print(" base:")
    _demo_heal(factory.create_base())

    print(" evolved:")
    _demo_heal(factory.create_evolved())


def _demo_heal(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()

    print(" base:")
    _demo_transform(factory.create_base())

    print(" evolved:")
    _demo_transform(factory.create_evolved())


def _demo_transform(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    test_healing()
    test_transform()


if __name__ == "__main__":
    main()
