from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict


class CardType(str, Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"
    TOURNAMENT = "Tournament"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    def get_card_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", ""),
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
