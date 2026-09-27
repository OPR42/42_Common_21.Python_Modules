#!/usr/bin/env python3

def absolute_import() -> None:
    print("\nTesting\33[35m Absolute Imports\33[37m \33[3m(from "
          "\33[36mbasic.py\33[37m)\33[0m\33[1m\33[37m")
    from alchemy.transmutation.basic import (
        lead_to_gold,
        stone_to_gem
    )
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


def relative_import() -> None:
    print("\nTesting\33[35m Relative Imports\33[37m \33[3m(from "
          "\33[36madvanced.py\33[37m)\33[0m\33[1m\33[37m")
    from alchemy.transmutation.advanced import (
        philosophers_stone,
        elixir_of_life
    )
    print("philosophers_stone(): "
          f"{philosophers_stone()}")
    print("elixir_of_live(): "
          f"{elixir_of_life()}")


def package_access() -> None:
    print("\nTesting\33[35m Package Access\33[37m:")
    import alchemy.transmutation
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


def main() -> None:
    print("\33[1m\n\33[37m=====\33[35m Pathway Debate Mastery "
          "\33[37m=====")
    absolute_import()
    relative_import()
    package_access()
    print("\nBoth pathways\33[32m work\33[37m! Absolute:\33[32m clear\33[37m, "
          "Relative: \33[32mconcise\33[37m\33[0m\n")


if __name__ == "__main__":
    main()
