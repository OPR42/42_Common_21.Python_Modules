#!/usr/bin/env python3

import alchemy


def direct_access() -> None:
    print("\nTesting \33[35mdirect module access\33[37m:")
    from alchemy.elements import (create_fire, create_water,
                                  create_earth, create_air)
    print(f"alchemy.elements.create.fire(): {create_fire()}")
    print(f"alchemy.elements.create.water(): {create_water()}")
    print(f"alchemy.elements.create.earth(): {create_earth()}")
    print(f"alchemy.elements.create.air(): {create_air()}")


def package_access() -> None:
    print("\nTesting \33[35mpackage-level access\33[37m \33[0m\33[3m"
          "(controlled by \33[36m__ini__.py\33[37m)\33[0m\33[1m\33[37m:")
    print("alchemy.create.fire(): ", end="")
    try:
        print(f"{alchemy.create_fire()}")
    except AttributeError:
        print("AttributeError -\33[31m not exposed\33[37m")
    print("alchemy.create.water(): ", end="")
    try:
        print(f"{alchemy.create_water()}")
    except AttributeError:
        print("AttributeError -\33[31m not exposed\33[37m")
    print("alchemy.create.earth(): ", end="")
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError:
        print("AttributeError -\33[31m not exposed\33[37m")
    print("alchemy.create.air(): ", end="")
    try:
        print(f"{alchemy.create_air()}")
    except AttributeError:
        print("AttributeError -\33[31m not exposed\33[37m")


def package_metadata() -> None:
    print("\nPackage \33[35mmetadata\33[37m:")
    print(f"Version: \33[36m\33[3m{alchemy.__version__}\33[0m\33[1m\33[37m")
    print(f"Author: \33[36m\33[3m{alchemy.__author__}\33[0m\33[1m\33[37m")


def main() -> None:
    print("\33[1m\n\33[37m=====\33[35m Sacred Scroll Mastery \33[37m=====")
    direct_access()
    package_access()
    package_metadata()
    print("\33[0m")


if __name__ == "__main__":
    main()
