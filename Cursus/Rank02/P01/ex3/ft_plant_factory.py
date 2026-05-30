class Plant:
    def __init__(self, name: str, height: float, days_old: int) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old

    def show(self) -> None:
        print(f'{self.name}: {self.height:.1f}cm, {self.days_old} days old')


def main() -> None:
    print('=== Plant Factory Output ===')

    plants = [
        Plant('Rose', 25.0, 30),
        Plant('Oak', 200.0, 365),
        Plant('Cactus', 5.0, 90),
        Plant('Sunflower', 80.0, 45),
        Plant('Fern', 15.0, 120),
    ]

    for plant in plants:
        print('Created:', end=' ')
        plant.show()


if __name__ == '__main__':
    main()
