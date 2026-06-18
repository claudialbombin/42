import math


def get_player_pos():
    while True:
        raw_input = input("Enter new coordinates as floats in format 'x,y,z':")

        try:
            raw_values = raw_input.split(",")
            if len(raw_values) != 3:
                raise ValueError("Invalid syntax")

            coordinates = tuple(float(value) for value in raw_values)
            return coordinates
        except ValueError as error:
            if str(error) == "Invalid syntax":
                print("Invalid syntax")
            elif len(raw_input.split(",")) == 3:
                invalid_value = None
                for value in raw_input.split(","):
                    try:
                        float(value)
                    except ValueError:
                        invalid_value = value
                        break

                if invalid_value is not None:
                    try:
                        float(invalid_value)
                    except ValueError as p_error:
                        print(
                            f"Error on parameter '{invalid_value}': {p_error}"
                        )
                else:
                    print("Invalid syntax")
            else:
                print("Invalid syntax")


def distance(point_a, point_b):
    return math.sqrt(
        (point_b[0] - point_a[0]) ** 2
        + (point_b[1] - point_a[1]) ** 2
        + (point_b[2] - point_a[2]) ** 2
    )


def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    f_cs = get_player_pos()
    print(f"Got a first tuple: {f_cs}")
    print(
        f"It includes: X={f_cs[0]}, Y={f_cs[1]}, Z={f_cs[2]}"
    )
    print(f"Distance to center: {distance((0, 0, 0), f_cs):.4f}")

    print("Get a second set of coordinates")
    s_cs = get_player_pos()
    print(
        f"Distance between the sets of coordinates: {distance(f_cs, s_cs):.4f}"
    )


if __name__ == "__main__":
    main()
