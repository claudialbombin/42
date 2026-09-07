from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    factory1: CreatureFactory, factory2: CreatureFactory
) -> None:
    print("\nTesting battle")
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()
    print(fighter1.describe())
    print(" vs.")
    print(fighter2.describe())
    print(" fight!")
    print(fighter1.attack())
    print(fighter2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)

    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
