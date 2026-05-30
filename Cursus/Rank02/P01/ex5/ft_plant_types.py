class Plant:
    # Common plant data lives in the parent class so the child classes
    # only add their own special characteristics.
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = int(age)

    # The base show() method prints the shared plant information.
    def show(self) -> None:
        print(f'{self._name}: {self._height:.1f}cm, {self._age} days old')

    # All plants can grow. The example for the vegetable expects a
    # noticeable increase in height over time, so we use a fixed step.
    def grow(self) -> None:
        self._height += 2.1

    # All plants age by one day when this method is called.
    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    # The flower reuses the parent initialization and only adds color.
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    # The flower show() method reuses Plant.show() and then prints
    # the extra flower-specific information.
    def show(self) -> None:
        super().show()
        print(f'Color: {self._color}')
        if self._bloomed:
            print(f'{self._name} is blooming beautifully!')
        else:
            print(f'{self._name} has not bloomed yet')

    # Blooming changes the flower state and announces the change.
    def bloom(self) -> None:
        self._bloomed = True
        print(f'{self._name} is blooming beautifully!')


class Tree(Plant):
    # Trees also reuse the parent setup and add trunk diameter.
    def __init__(self, name: str, height: float, age: int, t_d: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(t_d)

    # Tree.show() keeps the standard plant output and then prints the
    # trunk diameter.
    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter:.1f}cm')

    # Trees can produce shade based on their own size.
    def produce_shade(self) -> None:
        print(
            f'Tree {self._name} now produces a shade of '
            f'{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.'
        )


class Vegetable(Plant):
    # Vegetables reuse the common plant state and add harvest season plus
    # nutritional value. The nutritional value starts at zero.
    def __init__(self, name: str, height: float, age: int, h_szn: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = h_szn
        self._nutritional_value = 0.0

    # The vegetable show() method keeps the common plant output and then
    # prints its extra data.
    def show(self) -> None:
        super().show()
        print(f'Harvest season: {self._harvest_season}')
        print(f'Nutritional value: {round(self._nutritional_value)}')

    # Vegetables change over time: they still grow like a plant, but their
    # nutritional value also increases as they grow.
    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    # Ageing also contributes to the vegetable's nutritional value.
    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5


def main() -> None:
    print('=== Garden Plant Types ===')

    # Flower example: show the inherited state, then bloom it, then show
    # the updated state again.
    print('=== Flower ===')
    rose = Flower('Rose', 15.0, 10, 'red')
    rose.show()
    print('[asking the rose to bloom]')
    rose.bloom()
    rose.show()

    # Tree example: the tree keeps the common plant data and adds its own
    # trunk-specific characteristic.
    print('\n=== Tree ===')
    oak = Tree('Oak', 200.0, 365, 5.0)
    oak.show()
    print('[asking the oak to produce shade]')
    oak.produce_shade()

    # Vegetable example: the vegetable starts with zero nutritional value
    # and gains value every time age() and grow() are called.
    print('\n=== Vegetable ===')
    tomato = Vegetable('Tomato', 5.0, 10, 'April')
    tomato.show()
    print('[make tomato grow and age for 20 days]')
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == '__main__':
    main()
