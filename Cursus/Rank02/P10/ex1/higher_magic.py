from collections.abc import Callable

Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(spell1: Spell, spell2: Spell) -> Callable[
    [str, int], tuple[str, str]
]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast


def spell_sequence(
    spells: list[Spell]
) -> Callable[[str, int], list[str]]:
    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return cast_all


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def is_powerful(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    fire_msg, heal_msg = combined("Dragon", 10)
    print(f"Combined spell result: {fire_msg}, {heal_msg}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(is_powerful, fireball)
    print(safe_fireball("Dragon", 25))
    print(safe_fireball("Dragon", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    for message in sequence("Dragon", 15):
        print(message)


if __name__ == "__main__":
    main()
