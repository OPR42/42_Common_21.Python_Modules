from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return ("\33[36mPhilosopher's stone\33[37m created using "
            f"{lead_to_gold()} and {healing_potion()}")


def elixir_of_life() -> str:
    return ("\33[35mElixir of life\33[37m: eternal youth "
            "\33[32machieved\33[37m")
