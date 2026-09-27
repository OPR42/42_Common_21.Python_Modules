import random
from typing import Dict, List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, c in enumerate(self.cards):
            if c.name == card_name:
                del self.cards[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is\33[31m empty\33[37m")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict[str, float | int]:
        total = len(self.cards)
        creatures = len([c for c in self.cards if isinstance(c, CreatureCard)])
        spells = len([c for c in self.cards if isinstance(c, SpellCard)])
        artifacts = len([c for c in self.cards if isinstance(c, ArtifactCard)])
        avg_cost = 0.0
        if total > 0:
            avg_cost = sum([c.cost for c in self.cards]) / total
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
