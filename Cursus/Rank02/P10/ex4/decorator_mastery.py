import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[-1] if args else kwargs.get("power")
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char == " " for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def cursed_spell() -> str:
    raise RuntimeError("The spell backfires!")


@retry_spell(3)
def orc_battle_cry() -> str:
    return "Waaaaaaagh spelled !"


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    print(cursed_spell())
    print(orc_battle_cry())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X7"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fizzle", 5))


if __name__ == "__main__":
    main()
