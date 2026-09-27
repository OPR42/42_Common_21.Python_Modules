#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == (ContactType.telepathic and
                                 self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least "
                             "3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals should include received messages")
        return self


def main() -> None:
    print("\n\33[1m=====\33[35m Alien Contact Log Validation \33[37m=====")
    print("\n\33[32mValid\33[37m contact report:")
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-03-15T22:30:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    print(f"ID: \33[36m{contact.contact_id}\33[37m")
    print(f"Type: \33[36m{contact.contact_type.value}\33[37m")
    print(f"Location: \33[36m{contact.location}\33[37m")
    print(f"Signal: \33[36m{contact.signal_strength}\33[37m/10")
    print(f"Duration: \33[36m{contact.duration_minutes}\33[37m minutes")
    print(f"Witnesses: \33[36m{contact.witness_count}\33[37m")
    print(f"Message: '\33[36m{contact.message_received}\33[37m'")
    print("\n\33[31mInvalid\33[37m contact report:")
    try:
        AlienContact(
            contact_id="AC_FAIL",
            timestamp="2024-03-01T10:00:00",
            location="Unknown",
            contact_type=ContactType.telepathic,
            signal_strength=6,
            duration_minutes=1337,
            witness_count=1,
        )
    except ValidationError as e:
        print("Expected validation \33[31merrors\33[37m:")
        print(f"\33[0m\33[3m\33[33m{e.errors()[0]["msg"]}\33[37m\33[0m\33[1m")
    finally:
        print("\33[0m")


if __name__ == "__main__":
    main()
