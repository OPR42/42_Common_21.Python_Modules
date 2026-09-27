#!/usr/bin/env python3

class GardenError(Exception):
    """Init GardenError"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Init PlantError"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Init WaterError"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


def provoke_plant_error() -> None:
    """Trigger PlantError"""
    raise PlantError("The tomato plant is wilting!")


def provoke_water_error() -> None:
    """Trigger WaterError"""
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    """Test custom errors"""
    print("\n\33[1m===== \33[35mCustom Garden Errors Demo\33[37m ===")

    print("\nTesting PlantError...")
    try:
        provoke_plant_error()
    except PlantError as error:
        print(f"Caught \33[31mPlantError\33[37m: {error}")

    print("\nTesting WaterError...")
    try:
        provoke_water_error()
    except WaterError as error:
        print(f"Caught \33[31mWaterError\33[37m: {error}")

    print("\nTesting catching all garden errors...")
    try:
        provoke_plant_error()
    except GardenError as error:
        print(f"Caught a \33[31mgarden error\33[37m: {error}")

    try:
        provoke_water_error()
    except GardenError as error:
        print(f"Caught a \33[31mgarden error\33[37m: {error}")

    print("\nAll custom error types \33[32mwork correctly\33[37m!\n\33[0m")


if __name__ == "__main__":
    main()
