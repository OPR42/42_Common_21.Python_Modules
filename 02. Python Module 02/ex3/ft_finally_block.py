#!/usr/bin/env python3

def water_plants(plant_list) -> None:
    """Waters valid plants"""
    plant_inv = {"tomato", "lettuce", "carrots"}
    print("Opening \33[35mwatering system\33[37m")
    try:
        for plant in plant_list:
            if plant not in plant_inv:
                raise KeyError
            print(f"Watering \33[36m{plant}\33[37m")

    except KeyError:
        print(f"\33[31mError\33[37m: Cannot water \33[33m{plant}"
              "\33[37m - invalid plant!")

    finally:
        print("Closing \33[35mwatering system\33[37m (cleanup)")


def test_watering_system() -> None:
    """Tests watering system"""
    print("\n\33[1m===== \33[35mGarden Watering System\33[37m =====\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed \33[32msuccessfully\33[37m!")
    print("\nTesting with error...")
    water_plants(["tomato", "None", "carrots"])
    print("\nCleanup always happens, even with errors!\n\33[0m")


if __name__ == "__main__":
    test_watering_system()
