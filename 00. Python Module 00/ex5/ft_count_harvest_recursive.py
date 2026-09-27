def ft_count_harvest_recursive(days: int = None, day: int = 1) -> None:
    if days is None:
        days = int(input("Days until harvest: "))
    if day > days:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(days, day + 1)
