#!/usr/bin/env python3

class Plant:
    """Plant informations and methods"""
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
        """Returns plant information"""
        part1: str = f" ║ \33[36m{self.name:^12} \33[33m│ \33[36m"
        part2: str = f"{self.height:>6} \33[37mcm    \33[33m│ \33[36m"
        part3: str = f"{self.old:>3}\33[37m days old \33[33m║"
        return f"{part1}{part2}{part3}"


def main() -> None:
    """Create plants and displays growth during a week"""
    plants = [
        Plant("Rose", 25, 30, 2),
        Plant("Sunflower", 80, 45, 13),
        Plant("Cactus", 15, 120, 1),
    ]
    print("\33[1m\33[33m")
    print(" ╔════════════════════════════════════════════╗")
    print(" ║           \33[35mWelcome to OPR Garden\33[33m            ║")
    print(" ╠══════════════╤══════════════╤══════════════╣")
    print(" ║     \33[37mNAME     \33[33m│    \33[37mHEIGHT    "
          "\33[33m│     \33[37mAGE      \33[33m║")
    day = 0
    while day <= 7:
        print(
            f" ╟──────────────┼────\33[37mDAY\33[33m─\33[36m"
            f"{day:02d}\33[33m────┼──────────────╢"
        )
        for plant in plants:
            if day > 0:
                plant.grow(1)
                plant.age(1)
            print(plant.get_info())
        day += 1
    print(" ╠══════════════╧═\33[37mWEEKLY\33[33m══\33[37mGAIN\33[33m"
          "═╧══════════════╣")
    for plant in plants:
        txt1 = f"\33[36m{plant.name} \33[37mgrew \33[36m"
        txt2 = f"{plant.height - plant.start_height:+03d} \33[37mcm this week"
        txt = f"{txt1}{txt2}\33[33m"
        print(f" ║ {txt:^67} ║")
    print(" ╚════════════════════════════════════════════╝\33[0m\n")


if __name__ == "__main__":
    main()
