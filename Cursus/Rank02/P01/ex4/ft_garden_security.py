class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0

        self.set_height(height, announce=False)
        self.set_age(age, announce=False)

    def show(self) -> None:
        print(f'{self._name}: {self._height:.1f}cm, {self._age} days old')

    def set_height(self, height: float, announce: bool = True) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            if announce:
                print('Height update rejected')
            return False

        self._height = float(height)
        if announce:
            print(f'Height updated: {self._height:.1f}cm')
        return True

    def set_age(self, age: int, announce: bool = True) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            if announce:
                print('Age update rejected')
            return False

        self._age = int(age)
        if announce:
            print(f'Age updated: {self._age} days')
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


def main() -> None:
    print('=== Garden Security System ===')

    rose = Plant('Rose', 15.0, 10)
    print('Plant created:', end=' ')
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-12)
    print()
    print('Current state:', end=' ')
    rose.show()


if __name__ == '__main__':
    main()
