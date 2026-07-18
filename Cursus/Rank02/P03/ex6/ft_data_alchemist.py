import random


def main():
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    all_players = [name.capitalize() for name in players]
    capitalized_players = [name for name in players if name[0].isupper()]
    score_dict = {name: random.randint(0, 999) for name in all_players}
    average_score = round(sum(score_dict.values()) / len(score_dict), 2)
    high_scores = {
        name: score_dict[name]
        for name in score_dict
        if score_dict[name] > average_score
    }

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_players}")
    print(f"New list of capitalized names only: {capitalized_players}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {average_score}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
