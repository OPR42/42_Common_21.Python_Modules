#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        leaders = {Rank.commander, Rank.captain}
        if not any(member.rank in leaders for member in self.crew):
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")
        if self.duration_days > 365:
            experienced = [
                m for m in self.crew if m.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("\n\33[1m=====\33[36m Space Mission Crew Validation \33[37m=====")
    print("\n\33[32mValid\33[37m mission created:")
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2025-06-01T09:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=45,
                specialization="Mission Command",
                years_experience=20,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=34,
                specialization="Navigation",
                years_experience=6,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=29,
                specialization="Engineering",
                years_experience=5,
            ),
        ],
    )
    print(f"Mission: \33[36m{mission.mission_name}\33[37m")
    print(f"ID: \33[36m{mission.mission_id}\33[37m")
    print(f"Destination: \33[36m{mission.destination}\33[37m")
    print(f"Duration: \33[36m{mission.duration_days} days\33[37m")
    print(f"Budget: $\33[36m{mission.budget_millions}M\33[37m")
    print(f"Crew size: \33[36m{len(mission.crew)}\33[37m")
    print("Crew members:")
    for member in mission.crew:
        print(f"- \33[36m{member.name}\33[37m ({member.rank.value}) - "
              f"\33[36m{member.specialization}\33[37m")
    print("\n\33[31mInvalid\33[37m mission created:")
    try:
        SpaceMission(
            mission_id="BAD01",
            mission_name="Broken Mission",
            destination="Mars",
            launch_date="2025-01-01T00:00:00",
            duration_days=100,
            budget_millions=500.0,
            crew=[
                CrewMember(
                    member_id="CMX",
                    name="No Leader",
                    rank=Rank.cadet,
                    age=22,
                    specialization="Training",
                    years_experience=1,
                )
            ],
        )
    except ValidationError as e:
        print("Expected validation \33[31merrors\33[37m:")
        print(f"\33[0m\33[3m\33[33m{e.errors()[0]["msg"]}\33[37m\33[0m\33[1m")
    finally:
        print("\33[0m")


if __name__ == "__main__":
    main()
