from typing import Dict, List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.created_count: int = 0

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        self.created_count += 1
        if name_or_power == "Fire Dragon" or name_or_power is None:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        if name_or_power == "Goblin Warrior":
            return CreatureCard("Goblin Warrior", 2, "Common", 5, 2)
        return CreatureCard(str(name_or_power), 2, "Common", 2, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        self.created_count += 1
        if name_or_power == "Lightning Bolt" or name_or_power is None:
            return SpellCard("Lightning Bolt", 3, "Rare", "damage")
        return SpellCard(str(name_or_power), 2, "Common", "damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        self.created_count += 1
        if name_or_power == "Mana Ring" or name_or_power is None:
            return ArtifactCard("Mana Ring", 2, "Common", 5,
                                "Permanent: +1 mana per turn")
        return ArtifactCard(str(name_or_power), 2, "Common", 3,
                            "Permanent effect")

    def create_themed_deck(self, size: int) -> Dict:
        cards: List[Card] = []
        for _ in range(size):
            cards.append(self.create_creature("Goblin Warrior"))
        return {"theme": "fantasy", "size": size, "cards": cards}

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
