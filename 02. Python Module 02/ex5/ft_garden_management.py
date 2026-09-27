#!/usr/bin/env python3


class GardenError(Exception):
    """GardenError parent class"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Specific PlantError"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Specific WaterError"""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class GardenManager:
    """GardenManager core"""
    def __init__(self) -> None:
        self._plants: list[str] = []
        self._water_levels: list[int] = []
        self._sun_levels: list[int] = []
        self._tank: int = 10

    def add_plant(self, name: str) -> None:
        """Adds plants if name ok"""
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        if name in self._plants:
            raise PlantError(f"Plant '\33[33m{name}\33[37m]' already exists!")
        self._plants.append(name)
        self._water_levels.append(0)
        self._sun_levels.append(0)

    def set_conditions(self, name: str, water: int, sun: int) -> None:
        """Sets plant condition"""
        idx = self._index_of(name)
        self._water_levels[idx] = water
        self._sun_levels[idx] = sun

    def water_plants(self) -> None:
        """Waters plants and closes watering system even in case of error"""
        print("Opening \33[36mwatering\33[37m system")
        try:
            for name in self._plants:
                self._use_water(1)
                idx = self._index_of(name)
                self._water_levels[idx] += 5
                print(f"Watering \33[36m{name}\33[37m - "
                      "\33[32msuccess\33[37m")
        finally:
            print("Closing \33[36mwatering\33[37m system (cleanup)")

    def check_plant_health(self, name: str) -> None:
        """Checks if plant's conditions are ok"""
        idx = self._index_of(name)
        water = self._water_levels[idx]
        sun = self._sun_levels[idx]
        if water < 0:
            raise PlantError(f"Water level \33[36m{water}\33[37m"
                             " is too low (min 0)")
        if water > 10:
            raise PlantError(f"Water level \33[36m{water}\33[37m"
                             " is too high (max 10)")
        if sun < 0:
            raise PlantError(f"Sun level \33[36m{sun}\33[37m"
                             " is too low (min 0)")
        if sun > 10:
            raise PlantError(f"Sun level \33[36m{sun}\33[37m"
                             " is too high (max 10)")
        print(f"\33[36m{name}\33[37m: \33[32mhealthy\33[37m (water: \33[36m"
              f"{water}\33[37m, sun: \33[36m{sun}\33[37m)")

    def _index_of(self, name: str) -> int:
        """Looks for plant index in garden"""
        if name not in self._plants:
            raise PlantError(f"Unknown plant: \33[31m{name}\33[37m")
        return self._plants.index(name)

    def _use_water(self, amount: int) -> None:
        """Checks water ressource"""
        if amount > self._tank:
            raise WaterError("Not enough water in tank")
        self._tank -= amount


def test_garden_management() -> None:
    """Tests GardenManager methods"""
    print("\33[1m]")
    print("===== \33[35mGarden Management System\33[37m =====")
    manager = GardenManager()
    print("\n\33[35mAdding plants\33[37m to garden...")
    try:
        manager.add_plant("tomato")
        print("Added \33[36mtomato\33[37m successfully")
    except GardenError as error:
        print(f"\33[31mError\33[37m adding plant: {error}")
    try:
        manager.add_plant("lettuce")
        print("Added \33[36mlettuce\33[37m successfully")
    except GardenError as error:
        print(f"\33[31mError\33[37m adding plant: {error}")
    try:
        manager.add_plant("")
        print("Added \33[36m(empty)\33[37m successfully")
    except GardenError as error:
        print(f"\33[31mError\33[37m adding plant: {error}")
    print("\n\33[35mWatering plants\33[37m...")
    manager.water_plants()
    print("\n\33[35mChecking plant health\33[37m...")
    manager.set_conditions("tomato", water=5, sun=8)
    manager.set_conditions("lettuce", water=15, sun=8)
    try:
        manager.check_plant_health("tomato")
    except GardenError as error:
        print(f"\33[31mError\33[37m checking \33[36mtomato\33[37m: {error}")
    try:
        manager.check_plant_health("lettuce")
    except GardenError as error:
        print(f"\33[31mError\33[37m checking \33[36mlettuce\33[37m: {error}")
    print("\n\33[35mTesting error recovery\33[37m...")
    try:
        manager._use_water(9999)
    except GardenError as error:
        print(f"Caught \33[31mGardenError\33[37m: {error}")
        print("System recovered and \33[32mcontinuing\33[37m...")
    print("\n\33[35mGarden management system\33[37m test \33[32m"
          "complete\33[37m!\n")


if __name__ == "__main__":
    test_garden_management()
