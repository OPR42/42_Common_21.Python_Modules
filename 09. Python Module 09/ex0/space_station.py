#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("\n\33[1m=====\33[35m Space Station Data Validation \33[37m=====")
    print("\n\33[32mValid station\33[37m created:")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="1977-04-18T23:42:00",
    )
    print(f"ID: \33[36m{station.station_id}\33[37m")
    print(f"Name: \33[36m{station.name}\33[37m")
    print(f"Crew: \33[36m{station.crew_size}\33[37m people")
    print(f"Power: \33[36m{station.power_level}\33[37m%")
    print(f"Oxygen: \33[36m{station.oxygen_level}\33[37m%")
    print("Status: \33[32mOperational\33[37m")
    print("\n\33[31mInvalid station\33[37m created:")
    try:
        SpaceStation(
            station_id="BAD01",
            name="Broken Station",
            crew_size=42,
            power_level=-2.0,
            oxygen_level=120.0,
            last_maintenance="1977-04-18T23:42:00",
        )
    except ValidationError as e:
        print("Expected validation \33[31merrors\33[37m:")
        for error in e.errors():
            location = "->".join(str(x) for x in error["loc"])
            print(f"- \33[33m{location}\33[37m: \33[0m\33[3m\33[37m"
                  f"{error['msg']}\33[37m\33[0m\33[1m")
    finally:
        print("\33[0m")


if __name__ == "__main__":
    main()
