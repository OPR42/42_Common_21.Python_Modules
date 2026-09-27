#!/usr/bin/env python3

class SecurePlant:
    """Handles plants information in a secure way"""
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__old = 0
        print(f"\33[36m{self.name}\33[37m plant created "
              "[\33[32mOK\33[37m]")

    def set_height(self, height: int) -> None:
        """Sets plant's valid height"""
        if height < 0:
            print(f"Invalid operation attempted on \33[36m{self.name}"
                  f"\33[37m: height \33[36m{height}\33[37m cm "
                  "[\33[31mREJECTED\33[37m]")
            print("Security : \33[033mNegative height\33[37m rejected")
        else:
            self.__height = height
            print(f"\33[36m{self.name}\33[37m height updated: \33[36m"
                  f"{height}\33[37m cm [\33[32mOK\33[37m]")

    def set_age(self, old: int) -> None:
        """Sets plant's valid age"""
        if old < 0:
            print(f"Invalid operation attempted on \33[36m{self.name}"
                  f"\33[37m: age \33[36m{old}\33[37m days "
                  "[\33[31mREJECTED\33[37m]")
            print("Security : \33[033mNegative age\33[37m rejected")
        else:
            self.__old = old
            print(f"\33[36m{self.name}\33[37m age updated: \33[36m"
                  f"{old}\33[37m days [\33[32mOK\33[37m]")

    def get_height(self) -> int:
        """Gets plant's height"""
        return self.__height

    def get_age(self) -> int:
        """Gets plant's age"""
        return self.__old


def main() -> None:
    """Tests set/get methods"""
    print("\33[1m")
    print("\33[35m🌿 Creating plants 🌿\33[37m")
    plants = [
        SecurePlant("Simoleons tree"),
        SecurePlant("Yggdrasill"),
        SecurePlant("Power plant"),
        SecurePlant("Archespore"),
    ]
    print("\n\33[35m👎 Testing absurd values 👎\33[37m")
    plants[0].set_height(-42)
    plants[2].set_height(-1337)
    plants[3].set_age(-1)
    plants[1].set_age(-68)
    print("\n\33[35m🌿 Setting coherent values 🌿\33[37m")
    plants[0].set_height(170)
    plants[0].set_age(7)
    plants[1].set_height(10000042)
    plants[1].set_age(1071337)
    plants[2].set_height(10500)
    plants[2].set_age(17520)
    plants[3].set_height(280)
    plants[3].set_age(4)
    print("\n\33[35m🌿 Garden inventory 🌿\33[37m")
    for plant in plants:
        print(f"Plant \33[36m{plant.name}\33[37m is known as \33[36m"
              f"{plant.get_height()}\33[37m cm high and \33[36m"
              f"{plant.get_age()}\33[37m days old")
    print("\33[0m")


if __name__ == "__main__":
    main()
