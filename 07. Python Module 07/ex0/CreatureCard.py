from typing import Any, Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("attack and health must be positive integers")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        battlefield = game_state.get("battlefield", [])
        battlefield.append(self.name)
        game_state["battlefield"] = battlefield
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: Any) -> Dict[str, Any]:
        target_name = str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
