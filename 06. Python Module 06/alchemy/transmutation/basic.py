from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return ("\33[36mLead\33[37m transmuted to \33[33mgold\33[37m "
            f"using {create_fire()}")


def stone_to_gem() -> str:
    return ("\33[33mStone\33[37m transmuted to \33[36mgem\33[37m "
            f"using {create_earth()}")
