import sys


def main() -> None:
    arguments = sys.argv[1:]
    scores = []

    print("=== Player Score Analytics ===")

    for argument in arguments:
        try:
            scores.append(int(argument))
        except ValueError:
            print(f"Invalid parameter: '{argument}'")

    if not scores:
        print('No scores provided.')
        print('Usage: python3 ft_score_analytics.py <score1> <score2> ...')
        return

    total_score = sum(scores)
    average_score = total_score / len(scores)
    high_score = max(scores)
    low_score = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
