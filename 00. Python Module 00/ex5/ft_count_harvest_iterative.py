def ft_count_harvest_iterative() -> None:
    days: int = range(int(input("Days until harvest: ")))
    day: int
    for day in days:
        print(f"Day {day + 1}")
    print("Harvest time!")
