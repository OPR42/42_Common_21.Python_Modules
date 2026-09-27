#!/usr/bin/env python3

class Plant:
    """Plant info and methods"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = f"\33[36m{name}\33[37m"
        self.height = height
        self.age = age
        self._start_height = height

    def grow(self, growth: int = 1) -> None:
        """Grow plant"""
        self.height += growth
        self.age += 1
        print(f"{self.name} grew \33[36m{growth}\33[37mcm")

    def get_info(self) -> str:
        """Returns plant info"""
        return f"{self.name}: \33[36m{self.height}\33[37mcm"

    def growth_since_start(self) -> int:
        """Returns plant growth"""
        return self.height - self._start_height

    def type_name(self) -> str:
        """Returns plant type"""
        return "regular"

    def score(self) -> int:
        """Returns plant score. There is no score in this class"""
        return 0


class FloweringPlant(Plant):
    """FloweringPlant info and methods"""
    def __init__(self, name: str, height: int, age: int, color: str,
                 blooming: bool = True) -> None:
        super().__init__(name=name, height=height, age=age)
        self.color = color
        self.blooming = blooming

    def get_info(self) -> str:
        """Returns floweringplant info"""
        state = "blooming" if self.blooming else "not blooming"
        return (f"{self.name}: \33[36m{self.height}\33[37mcm, "
                f"\33[36m{self.color}\33[37m flowers \33[36m{state}\33[37m")

    def type_name(self) -> str:
        """Returns floweringplant type"""
        return "flowering"


class PrizeFlower(FloweringPlant):
    """PrizeFlower info and methods"""
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int, blooming: bool = True) -> None:
        super().__init__(name=name, height=height, age=age,
                         color=color, blooming=blooming)
        self.points = points

    def get_info(self) -> str:
        """Returns prizeflower info"""
        base = super().get_info()
        return (f"{base}, Prize points: \33[36m{self.points}\33[37m")

    def type_name(self) -> str:
        """Returns prizeflower type"""
        return "prize"

    def score(self) -> int:
        """Returns prizeflower score"""
        return self.points


class Garden:
    """Garden info and methods"""
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Creates plant"""
        self.plants.append(plant)
        print(f"Added {plant.name} to \33[36m{self.owner}\33[37m's garden")

    def grow_all(self) -> None:
        """Grows all plants in the garden"""
        print(f"\33[36m{self.owner}\33[37m is helping all plants grow")
        for plant in self.plants:
            plant.grow(1)

    def list_plants(self) -> None:
        """Displays all plants in the garden"""
        print("Plants in garden:")
        count: int = 1
        for plant in self.plants:
            print(f"{count:02d}. {plant.get_info()}")
            count += 1


class GardenManager:
    """GardenManager methods"""
    gardens: int = 0

    class GardenStats:
        """GardenStats methods"""
        @staticmethod
        def plants_added(garden: Garden) -> int:
            """Returns plants count"""
            count: int = 0
            for _ in garden.plants:
                count += 1
            return count

        @staticmethod
        def total_growth(garden: Garden) -> int:
            """Returns sum of all plant's growths"""
            growth: int = 0
            for plant in garden.plants:
                growth += plant.growth_since_start()
            return growth

        @staticmethod
        def count_types(garden: Garden) -> tuple[int, int, int]:
            """Return inventory by type"""
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            for plant in garden.plants:
                type_name = plant.type_name()
                if type_name == "prize":
                    prize += 1
                elif type_name == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def garden_score(garden: Garden) -> int:
            """Returns garden score"""
            score: int = 0
            for plant in garden.plants:
                score += plant.height
                score += plant.score()
            return score

    def __init__(self) -> None:
        """Creates gardens list"""
        self.gardens = []

    def add_garden(self, owner: str) -> None:
        """Create new garden"""
        if self.get_garden(owner) is None:
            self.gardens.append(Garden(owner))
            GardenManager.gardens += 1

    def get_garden(self, owner: str):
        """Finds owner's garden"""
        for garden in self.gardens:
            if garden.owner == owner:
                return garden
        return None

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        """Creates new plant in owner's garden"""
        garden = self.get_garden(owner)
        if garden is None:
            garden = Garden(owner)
            self.gardens.append(garden)
        garden.add_plant(plant)

    def grow_garden(self, owner: str) -> None:
        """Grows all plants in the owner's garden"""
        garden = self.get_garden(owner)
        if garden is None:
            return
        garden.grow_all()

    def report(self, owner: str) -> None:
        """Displays owner's garden informations"""
        garden = self.get_garden(owner)
        if garden is None:
            return
        print(f"\n\33[35m===== \33[36m{owner}\33[35m"
              "'s Garden Report =====\33[37m")
        garden.list_plants()
        added: int = GardenManager.GardenStats.plants_added(garden)
        growth: int = GardenManager.GardenStats.total_growth(garden)
        reg, flo, pri = GardenManager.GardenStats.count_types(garden)
        print(f"Plants added: \33[36m{added}\33[37m, Total growth: \33[36m"
              f"{growth}\33[37mcm")
        print(f"Plant types: \33[36m{reg}\33[37m regular, \33[36m{flo}\33[37m"
              f" flowering, \33[36m{pri}\33[37m prize flowers")

    @staticmethod
    def validate_heights(plants: list[Plant]) -> bool:
        """Check heights"""
        for plant in plants:
            if plant.height < 0:
                return False
        return True

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        """Creates gardens inside GardenManager"""
        manager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager

    def compare_scores(self, owner_a: str, owner_b: str) -> None:
        """Displays gardens' scores"""
        garden_a = self.get_garden(owner_a)
        garden_b = self.get_garden(owner_b)
        if garden_a is None or garden_b is None:
            return
        score_a: int = GardenManager.GardenStats.garden_score(garden_a)
        score_b: int = GardenManager.GardenStats.garden_score(garden_b)
        print("\n\33[35m===== Garden Scores =====\33[37m")
        print(f"\33[36m{owner_a}\33[37m: \33[36m{score_a}\33[37m")
        print(f"\33[36m{owner_b}\33[37m: \33[36m{score_b}\33[37m")


def main() -> None:
    """Tests GardenManager"""
    print("\33[1m")
    print("\33[35m===== Garden Management System Demo =====\33[37m")
    manager = GardenManager.create_garden_network(["Alice", "Bob"])
    manager.add_plant_to_garden("Alice", Plant("Oak Tree", 100, 3650))
    manager.add_plant_to_garden("Alice",
                                FloweringPlant("Rose", 25, 30, "red"))
    manager.add_plant_to_garden("Alice",
                                PrizeFlower("Sunflower", 50, 45, "yellow", 10))
    manager.grow_garden("Alice")
    manager.report("Alice")
    alice_garden = manager.get_garden("Alice")
    ok = GardenManager.validate_heights(alice_garden.plants)
    if ok is True:
        color: str = "\33[32m"
    else:
        color: str = "\33[31m"
    print(f"Height validation test: {color}{ok}\33[37m\n")
    manager.add_plant_to_garden("Bob", Plant("Pine", 80, 2000))
    manager.add_plant_to_garden("Bob",
                                PrizeFlower("Tulip", 20, 12, "pink", 12))
    manager.report("Bob")
    manager.compare_scores("Alice", "Bob")
    print(f"Total gardens managed: \33[36m"
          f"{GardenManager.gardens}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
