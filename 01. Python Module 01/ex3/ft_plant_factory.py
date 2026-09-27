#!/usr/bin/env python3

class Plant:
    """Plant information and methods"""
    def __init__(self, name: str, height: int, old: int, speed: int) -> None:
        self.name = name
        self.height = height
        self.old = old
        self.start_height = height
        self.daily_growth = speed

    def grow(self, period: int = 1) -> None:
        """Grow plant"""
        self.height += period * self.daily_growth

    def age(self, period: int = 1) -> None:
        """Age plant"""
        self.old += period

    def get_info(self) -> str:
        """Return plant information"""
        part1: str = f" ║ \33[36m{self.name:^12} \33[33m│ \33[36m"
        part2: str = f"{self.height:>6} \33[37mcm    \33[33m│ \33[36m"
        part3: str = f"{self.old:>3}\33[37m days old \33[33m║"
        return f"{part1}{part2}{part3}"


def main() -> None:
    """Creates plants and displays their informations"""
    plants = [
        Plant("Rose", 25, 30, 2),
        Plant("Oak", 200, 365, 2),
        Plant("Cactus", 5, 90, 1),
        Plant("Sunflower", 80, 45, 13),
        Plant("Fern", 15, 120, 1),
    ]
    print("\33[1m\33[33m")
    print(" ╔════════════════════════════════════════════╗")
    print(" ║           \33[35mWelcome to OPR Garden\33[33m            ║")
    print(" ╠══════════════╤══════════════╤══════════════╣")
    print(" ║     \33[37mNAME     \33[33m│    \33[37mHEIGHT    "
          "\33[33m│     \33[37mAGE      \33[33m║")
    print(" ╟──────────────┼──────────────┼──────────────╢")
    count: int = 0
    for plant in plants:
        print(plant.get_info())
        count += 1
    print(" ╠══════════════╧══════════════╧══════════════╣")
    txt = f"\33[37mTotal plants created : \33[36m{count:<5d}\33[33m"
    print(f" ║ {txt:^57} ║")
    print(" ╚════════════════════════════════════════════╝\33[0m\n")


if __name__ == "__main__":
    main()
