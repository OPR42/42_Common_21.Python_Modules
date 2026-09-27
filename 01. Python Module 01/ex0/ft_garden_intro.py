#!/usr/bin/env python3

def say_my_name() -> None:
    """Init and display plant information"""
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print("\33[1m\33[33m")
    print(" ╔═══════════════════════╗")
    print(" ║ \33[35mWelcome to OPR Garden\33[33m ║")
    print(" ╟───────────┬───────────╢")
    print(f" ║ \33[37mPlant     \33[33m│ \33[36m{name:<9} \33[33m║")
    print(f" ║ \33[37mHeight    \33[33m│ \33[36m{height:<4} cm   \33[33m║")
    print(f" ║ \33[37mAge       \33[33m│ \33[36m{age:<4} days \33[33m║")
    print(" ╚═══════════╧═══════════╝\33[0m\n")


if __name__ == "__main__":
    say_my_name()
