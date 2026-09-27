from typing import Any, Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
                self, name: str,
                cost: int,
                rarity: str,
                durability: int,
                effect: str
                ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.durability: int = durability
        self.effect: str = effect

    def activate_ability(self) -> Dict[str, Any]:
        if self.durability > 0:
            self.durability -= 1
        return ({"artifact": self.name, "effect": self.effect,
                "durability_left": self.durability})

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return ({"card_played": self.name, "mana_used": self.cost,
                "effect": self.effect})

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
