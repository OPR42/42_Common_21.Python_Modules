#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours) -> None:
    """Checks plant's health"""
    try:
        if (plant_name == "" or water_level < 1 or water_level > 10 or
           sunlight_hours < 2 or sunlight_hours > 12):
            raise ValueError
        print(f"Plant '\33[36m{plant_name}\33[37m' is \33[32mhealthy\33[37m!")

    except ValueError:
        if plant_name == "":
            print("\33[31mError\33[37m: Plant name cannot be empty!")
        elif water_level < 1:
            print(f"\33[31mError\33[37m: Water level \33[36m{water_level}"
                  "\33[37m is too low (min 1)")
        elif water_level > 10:
            print(f"\33[31mError\33[37m: Water level \33[36m{water_level}"
                  "\33[37m is too high (max 10)")
        elif sunlight_hours < 2:
            print("\33[31mError\33[37m: Sunlight hours \33[36m"
                  f"{sunlight_hours}\33[37m is too low (min 2)")
        elif sunlight_hours > 12:
            print("\33[31mError\33[37m: Sunlight hours \33[36m"
                  f"{sunlight_hours}\33[37m is too high (max 12)")
        else:
            print("\33[31mError\33[37m: Unknown error type")


def test_plant_checks() -> None:
    """Tests health system"""
    print("\n\33[1m===== \33[35mGarden Plant Health Checker\33[37m =====")
    print("\nTesting good values...")
    check_plant_health("tomato", 3, 6)
    print("\nTesting empty plant name...")
    check_plant_health("", 3, 6)
    print("\nTesting too low water level...")
    check_plant_health("tomato", 0, 6)
    print("\nTesting too high water level...")
    check_plant_health("tomato", 15, 6)
    print("\nTesting not enough sunlight hours...")
    check_plant_health("tomato", 3, 1)
    print("\nTesting too much sunlight hours...")
    check_plant_health("tomato", 3, 16)
    print("\nAll error raising tests \33[32mcompleted\33[37m!\n\33[0m")


if __name__ == "__main__":
    test_plant_checks()
