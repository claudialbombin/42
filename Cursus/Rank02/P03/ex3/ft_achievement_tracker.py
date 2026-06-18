import random


ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements():
    achievement_count = random.randint(6, 9)
    return set(random.sample(ACHIEVEMENTS, achievement_count))


def main():
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    print("=== Achievement Tracker System ===")

    for player, achievements in players.items():
        print(f"Player {player}: {achievements}")

    all_distinct = set().union(*players.values())
    common_achievements = set.intersection(*players.values())

    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common_achievements}")

    for player, achievements in players.items():
        other_achievements = set().union(
            *(value for name, value in players.items() if name != player)
        )
        only_player = achievements - other_achievements
        missing = all_distinct - achievements
        print(f"Only {player} has: {only_player}")
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
