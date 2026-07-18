import sys


def parse_inventory(arguments):
    inventory = {}

    for argument in arguments:
        if ":" not in argument:
            print(f"Error - invalid parameter '{argument}'")
            continue

        item_name, quantity_text = argument.split(":", 1)

        if item_name in inventory:
            print(f"Redundant item '{item_name}'- discarding")
            continue

        try:
            inventory[item_name] = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")

    return inventory


def report_inventory(inventory):
    item_list = list(inventory.keys())
    quantities = list(inventory.values())
    total_quantity = sum(quantities)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(
        f"Total quantity of the {len(item_list)} items: {total_quantity}"
    )

    if total_quantity != 0:
        for item_name in item_list:
            percentage = round(
                inventory[item_name] * 100 / total_quantity, 1
            )
            print(f"Item {item_name} represents {percentage}%")

        most_abundant = item_list[0]
        least_abundant = item_list[0]

        for item_name in item_list[1:]:
            if inventory[item_name] > inventory[most_abundant]:
                most_abundant = item_name
            if inventory[item_name] < inventory[least_abundant]:
                least_abundant = item_name

        print(
            f"Item most abundant: {most_abundant} with quantity "
            f"{inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} with quantity "
            f"{inventory[least_abundant]}"
        )


def main():
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])
    report_inventory(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
