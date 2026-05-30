def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        temp = input_temperature('25')
        print(f'Temperature is now {temp}°C')
    except ValueError as e:
        print(f'Caught input_temperature error: {e}')

    try:
        print("\nInput data is 'abc'")
        temp = input_temperature('abc')
        print(f'Temperature is now {temp}°C')
    except ValueError as e:
        print(f'Caught input_temperature error: {e}')


def main() -> None:
    print('=== Garden Temperature ===')
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    main()
