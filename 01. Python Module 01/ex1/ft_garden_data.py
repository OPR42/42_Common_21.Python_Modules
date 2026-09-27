#!/usr/bin/env python3

class Plant:
    """Plant informations"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """Init plants and display information"""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    print("\33[1m\33[33m")
    print(" ╔════════════════════════════════════════════╗")
    print(" ║           \33[35mWelcome to OPR Garden\33[33m            ║")
    print(" ╠══════════════╤══════════════╤══════════════╣")
    print(" ║     \33[37mNAME     \33[33m│    \33[37mHEIGHT    "
          "\33[33m│     \33[37mAGE      \33[33m║")
    print(" ╟──────────────┼──────────────┼──────────────╢")
    for plant in plants:
        print(
            f" ║ \33[36m{plant.name:^12} \33[33m│ "
            f"\33[36m{plant.height:>6} \33[37mcm    \33[33m│ "
            f"\33[36m{plant.age:>3}\33[37m days old \33[33m║"
        )
    print(" ╚══════════════╧══════════════╧══════════════╝\33[0m\n")


if __name__ == "__main__":
    main()
