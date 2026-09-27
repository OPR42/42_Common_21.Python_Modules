def healing_potion() -> str:
    from .elements import create_fire, create_water
    return (f"\33[34mHealing potion\33[37m brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    from .elements import create_earth, create_fire
    return (f"\33[32mStrength potion\33[37m brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    return (f"\33[33mInvisibility potion\33[37m brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion() -> str:
    from .elements import create_fire, create_water, create_earth, create_air
    return (f"\33[35mWisdom potion\33[37m with all elements: {create_fire()}, "
            f"{create_water()}, {create_earth()} and {create_air()}")
