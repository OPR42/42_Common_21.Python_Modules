#!/usr/bin/env python3

def full_module_import() -> None:
    import alchemy.elements
    print("\n\33[3mMethod 1\33[0m\33[1m -\33[35m Full module import\33[37m:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def specific_function_import() -> None:
    from alchemy.elements import create_water
    print("\n\33[3mMethod 2\33[0m\33[1m -\33[35m Specific function "
          "import\33[37m:")
    print(f"create_water(): {create_water()}")


def aliased_import() -> None:
    from alchemy.potions import healing_potion as heal
    print("\n\33[3mMethod 3\33[0m\33[1m -\33[35m Aliased import\33[37m:")
    print(f"heal(): {heal()}")


def multiple_imports() -> None:
    from alchemy.potions import strength_potion as strength
    from alchemy.elements import create_earth, create_fire
    print("\n\33[3mMethod 4\33[0m\33[1m -\33[35m Multiple import\33[37m:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength()}")


def full_imports() -> None:
    import alchemy.elements
    import alchemy.potions
    print("\n\33[3mMethod 5\33[0m\33[1m -\33[35m Full import\33[37m:")
    print(f"create_fire(): {alchemy.elements.create_fire()}")
    print(f"create_water(): {alchemy.elements.create_water()}")
    print(f"create_earth(): {alchemy.elements.create_earth()}")
    print(f"create_air(): {alchemy.elements.create_air()}")
    print(f"wisdom_potion(): {alchemy.potions.wisdom_potion()}")


def main() -> None:
    print("\33[1m\n\33[37m=====\33[35m Import Transmutation Mastery "
          "\33[37m=====")
    full_module_import()
    specific_function_import()
    aliased_import()
    multiple_imports()
    full_imports()
    print("\nAll import transmutation methods\33[32m mastered\33[37m\33[0m\n")


if __name__ == "__main__":
    main()
