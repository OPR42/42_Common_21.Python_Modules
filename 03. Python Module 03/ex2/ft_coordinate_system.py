#!/usr/bin/env python3

def calc_distance(position: tuple[int, int, int]) -> None:
    """calc distance from 3D position to origin"""
    x, y, z = position
    import math
    distance: float = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance between (0, 0, 0) and \33[36m{position}\33[37m: "
          f"\33[36m{distance:.2f}\33[37m")


def parse_coords(text_coords: str) -> None:
    """parse player coords then runs calc_distance"""
    coords = text_coords.split(",")
    try:
        xyz = []
        for coord in coords:
            xyz.append(int(coord))
        position = tuple([xyz[0], xyz[1], xyz[2]])
        print(f"Parsed position: \33[36m{position}\33[37m")
        calc_distance(position)

    except ValueError as error:
        print(f"\33[31mError parsing coordinates\33[37m: {error}")
        print(f"\33[31mError details\33[37m - Type: {type(error).__name__}, "
              f"Args: {error.args}")
        return None


def main() -> None:
    """test 3D distance"""
    print("\33[1m\n=====\33[35m Game Coordinate System \33[37m=====")
    position = tuple([10, 20, 5])
    print(f"\nPosition created: \33[36m{position}\33[37m")
    calc_distance(position)
    print("\nParsing coordinates: \"3,4,0\"")
    parse_coords("3,4,0")
    print("\nParsing invalid coordinates: \"abc,def,ghi\"")
    parse_coords("abc,def,ghi")
    print("\nUnpacking demonstration:\nPlayer at x=3, y=4, z=0")
    position = tuple([3, 4, 0])
    x, y, z = position
    print(f"Coordinates: X=\33[36m{x}\33[37m, Y=\33[36m{y}\33[37m, "
          f"Z=\33[36m{z}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
