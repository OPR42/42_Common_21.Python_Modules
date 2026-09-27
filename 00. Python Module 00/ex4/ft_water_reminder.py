def ft_water_reminder() -> None:
    watered: int = int(input("Days since last watering: "))
    if watered > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
