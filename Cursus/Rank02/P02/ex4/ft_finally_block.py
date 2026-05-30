class GardenError(Exception):
    def __init__(self, message: str = 'Unknown garden error') -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = 'Unknown plant error') -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f'Watering {plant_name}: [OK]')


def watering_session(p_names: tuple[str, ...], stop_error: bool) -> bool:
    print('Opening watering system')
    try:
        for plant_name in p_names:
            water_plant(plant_name)
    except PlantError as error:
        print(f'Caught PlantError: {error}')
        if stop_error:
            print('.. ending tests and returning to main')
            return False
    finally:
        print('Closing watering system')

    return True


def test_watering_system() -> None:
    print('=== Garden Watering System ===')

    print('Testing valid plants...')
    watering_session(('Tomato', 'Lettuce', 'Carrots'), stop_error=False)

    print('Testing invalid plants...')
    if not watering_session(('Tomato', 'lettuce', 'Carrots'), stop_error=True):
        return


def main() -> None:
    test_watering_system()
    print('Cleanup always happens, even with errors!')


if __name__ == '__main__':
    main()
