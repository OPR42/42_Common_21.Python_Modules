#!/usr/bin/env python3

class Plant:
    """Plant information"""
    def __init__(self, name: str, height: int, age: int, type: str) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.type = type


class Flower(Plant):
    """Plant Flower information"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name=name, height=height, age=age, type="Flower")
        self.color = color

    def display_info(self) -> None:
        """Display flower information"""
        print(f"\n\33[36m{self.name}\33[37m (\33[36m{self.type}\33[37m): "
              f"\33[36m{self.height}\33[37mcm, \33[36m{self.age}\33[37m "
              f"days, \33[36m{self.color}\33[37m color")

    def bloom(self) -> None:
        """Display flower action"""
        print(f"🌸 \33[36m{self.name}\33[37m is blooming beautifully 😊")


class Tree(Plant):
    """Plant Tree information"""
    def __init__(self, name: str, height: int, age: int, diam: int) -> None:
        super().__init__(name=name, height=height, age=age, type="Tree")
        self.diam = diam

    def display_info(self) -> None:
        """Display tree information"""
        print(f"\n\33[36m{self.name}\33[37m (\33[36m{self.type}\33[37m): "
              f"\33[36m{self.height}\33[37mcm, \33[36m{self.age}\33[37m "
              f"days, \33[36m{self.diam}\33[37mcm diameter")

    def produce_shade(self) -> None:
        """Display tree action"""
        print(f"🌳 \33[36m{self.name}\33[37m provides \33[36m"
              f"{self.diam * self.diam * 0.0312:.0f}\33[37m"
              " square meters of shade 😊")


class Vegetable(Plant):
    """Plant Vegetable information"""
    def __init__(self, nm: str, hg: int, ag: int, ssn: str, nt: str) -> None:
        super().__init__(name=nm, height=hg, age=ag, type="Vegetable")
        self.season = ssn
        self.nutri = nt

    def display_info(self) -> None:
        """Display vegetable information"""
        print(f"\n\33[36m{self.name}\33[37m (\33[36m{self.type}\33[37m): "
              f"\33[36m{self.height}\33[37mcm, \33[36m{self.age}\33[37m "
              f"days, \33[36m{self.season}\33[37m harvest")

    def display_nutri(self) -> None:
        """Display vegetable action"""
        print(f"🍆 \33[36m{self.name}\33[37m is rich in \33[36m"
              f"{self.nutri}\33[37m 😊")


def main() -> None:
    """Tests specialized plant information"""
    print("\33[1m")
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Daisy", 10, 10, "white"),
    ]
    trees = [
        Tree("Oak", 1000, 7000, 50),
        Tree("Sequoia", 3000, 17520, 80),
    ]
    vegetables = [
        Vegetable("Broccoli", 15, 90, "fall", "vitamin C"),
        Vegetable("Carrot", 25, 60, "spring", "dietary fibre"),
    ]
    flowers[0].display_info()
    flowers[0].bloom()
    flowers[1].display_info()
    flowers[1].bloom()
    trees[0].display_info()
    trees[0].produce_shade()
    trees[1].display_info()
    trees[1].produce_shade()
    vegetables[0].display_info()
    vegetables[0].display_nutri()
    vegetables[1].display_info()
    vegetables[1].display_nutri()
    print("\33[0m")


if __name__ == "__main__":
    main()
