from typing import Any


def artifact_sorter(
    artifacts: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(
        sum(mage["power"] for mage in mages) / len(mages), 2
    )
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Ice Wand", "power": 78, "type": "weapon"},
    ]
    mages = [
        {"name": "Alex", "power": 65, "element": "fire"},
        {"name": "Riley", "power": 90, "element": "ice"},
        {"name": "Sage", "power": 40, "element": "earth"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 60)
    names = [mage["name"] for mage in strong_mages]
    print(f"Mages with power >= 60: {names}")

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
