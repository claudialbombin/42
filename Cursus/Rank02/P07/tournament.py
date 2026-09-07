from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i, (factory1, strategy1) in enumerate(opponents):
        for factory2, strategy2 in opponents[i + 1:]:
            fight_one(factory1, strategy1, factory2, strategy2)


def fight_one(
    factory1: CreatureFactory,
    strategy1: BattleStrategy,
    factory2: CreatureFactory,
    strategy2: BattleStrategy,
) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("\n* Battle *")
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" now fight!")

    try:
        strategy1.act(creature1)
        strategy2.act(creature2)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle(
        [(aqua, normal), (healing, defensive), (transform, aggressive)]
    )


if __name__ == "__main__":
    main()
