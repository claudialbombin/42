class Plant:
    # The internal statistics system is nested inside Plant so the data
    # stays tightly coupled to the object that owns it.
    class _Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f'Stats: {self._grow_calls} grow, '
                f'{self._age_calls} age, {self._show_calls} show'
            )

    # The base plant keeps the shared data used by every specialized type.
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = int(age)
        self._stats = self._Statistics()

    # The static method answers a general question without needing an object.
    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    # The class method creates a safe default plant when the caller does not
    # yet have the full set of data.
    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls('Unknown plant', 0.0, 0)

    # The base show() only prints the common data and updates statistics.
    def show(self) -> None:
        self._stats.count_show()
        print(f'{self._name}: {self._height:.1f}cm, {self._age} days old')

    # The base grow() and age() methods update the common counters.
    # Specialized plants can reuse them with super() and then apply their
    # own specific evolution.
    def grow(self) -> None:
        self._stats.count_grow()
        self._height = round(self._height + 1.0, 1)

    def age(self) -> None:
        self._stats.count_age()
        self._age += 1


class Flower(Plant):
    # Flower extends Plant with a color and a bloom state.
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    # Reuse the parent output and then append the extra flower details.
    def show(self) -> None:
        super().show()
        print(f'Color: {self._color}')
        if self._bloomed:
            print(f'{self._name} is blooming beautifully!')
        else:
            print(f'{self._name} has not bloomed yet')

    # Flowers grow faster than the base plant. We call the parent method so
    # the common statistics stay centralized, then add the flower-specific
    # growth on top.
    def grow(self) -> None:
        super().grow()
        self._height = round(self._height + 7.0, 1)

    # Blooming only changes the internal state. The visual confirmation is
    # shown later through show().
    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    # Trees add trunk diameter and keep an extra statistics counter for shade.
    class _Statistics(Plant._Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def count_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f'{self._shade_calls} shade')

    def __init__(self, name: str, height: float, age: int, t_d: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(t_d)

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self._trunk_diameter:.1f}cm')

    def produce_shade(self) -> None:
        self._stats.count_shade()
        print(
            f'Tree {self._name} now produces a shade of '
            f'{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.'
        )


class Seed(Flower):
    # Seed inherits from Flower because it is a flower that has bloomed and
    # now carries a seed count.
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    # The seed keeps the flower display and adds the seed count.
    def show(self) -> None:
        super().show()
        print(f'Seeds: {self._seeds}')

    # Seeds grow more aggressively, so the height increase is larger.
    def grow(self) -> None:
        super(Flower, self).grow()
        self._height = round(self._height + 29.0, 1)

    # Seeds also age in bigger steps once we simulate time passing.
    def age(self) -> None:
        super(Flower, self).age()
        self._age += 19

    # Once the flower has bloomed, the seed count appears.
    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


# This standalone helper keeps the statistics display separate from the
# classes themselves, as requested by the exercise.
def display_statistics(plant: Plant) -> None:
    print(f'[statistics for {plant._name}]')
    plant._stats.display()


def main() -> None:
    print('=== Garden statistics ===')

    # Static method demo: no object is needed to answer the question.
    print('=== Check year-old')
    print(f'Is 30 days more than a year? -> {Plant.is_older_than_year(30)}')
    print(f'Is 400 days more than a year? -> {Plant.is_older_than_year(400)}')

    # Flower example: we show the base data, inspect statistics, then make
    # the flower grow and bloom to see the state change.
    print('\n=== Flower')
    rose = Flower('Rose', 15.0, 10, 'red')
    rose.show()
    display_statistics(rose)
    print('[asking the rose to grow and bloom]')
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    # Tree example: the extra shade counter lives in the tree-specific
    # statistics object.
    print('\n=== Tree')
    oak = Tree('Oak', 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    display_statistics(oak)

    # Seed example: this starts as a flower, then blooms and gains seeds.
    print('\n=== Seed')
    sunflower = Seed('Sunflower', 80.0, 45, 'yellow')
    sunflower.show()
    display_statistics(sunflower)
    print('[make sunflower grow, age and bloom]')
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    # Anonymous plant example: the class method creates a safe default object.
    print('\n=== Anonymous')
    anonymous = Plant.anonymous()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == '__main__':
    main()
