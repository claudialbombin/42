import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "ice"),
        "lightning": functools.partial(
            base_enchantment, 50, "lightning"
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def _dispatch_spell(value: Any) -> str:
    return "Unknown spell type"


@_dispatch_spell.register
def _dispatch_int(value: int) -> str:
    return f"Damage spell: {value} damage"


@_dispatch_spell.register
def _dispatch_str(value: str) -> str:
    return f"Enchantment: {value}"


@_dispatch_spell.register(list)
def _dispatch_list(value: list[Any]) -> str:
    return f"Multi-cast: {len(value)} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    return _dispatch_spell


def enchant_item(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} enchantment (power {power}) on " \
           f"{target}"


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(enchant_item)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
