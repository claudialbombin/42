import random
import typing


PLAYER_NAMES = [
    "alice",
    "bob",
    "charlie",
    "dylan"
]
EVENT_ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(PLAYER_NAMES), random.choice(EVENT_ACTIONS)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event_index = random.randrange(len(events))
        event = events[event_index]
        del events[event_index]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()
    for event_index in range(1000):
        name, action = next(event_stream)
        print(f"Event {event_index}: Player {name} did action {action}")

    event_stream = gen_event()
    event_list = [next(event_stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
