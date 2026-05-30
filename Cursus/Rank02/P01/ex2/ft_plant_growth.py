class Plant:
    def __init__(self, name: str, height: float, age: int, rt: float) -> None:
        self.name = name
        self.height = height
        self.days_old = age
        self.growth_rate = rt

    def show(self) -> None:
        print(f'{self.name}: {self.height:.1f}cm, {self.days_old} days old')

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days_old += 1


def main() -> None:
    print('=== Garden Plant Growth ===')

    rose = Plant('Rose', 25.0, 30, 0.8)
    initial_height = rose.height

    rose.show()

    for day in range(1, 8):
        print(f'=== Day {day} ===')
        rose.grow()
        rose.age()
        rose.show()

    print(f'Growth this week: {rose.height - initial_height:.1f}cm')


if __name__ == '__main__':
    main()
