def ft_plant_age() -> None:
    age = int(input("Enter the age of the plant in days: "))
    if age > 60:
        print('Plant is ready to harvest!')
    else:
        print('Plant needs more time to grow.')
