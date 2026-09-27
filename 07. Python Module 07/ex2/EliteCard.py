from typing import Any, Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
                self, name: str,
                cost: int,
                rarity: str,
                attack_power: int
                ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack_power: int = attack_power
        self.mana: int = 0
        self.damage_blocked: int = 0

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed",
        }

    def attack(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(3, incoming_damage)
        taken = incoming_damage - blocked
        self.damage_blocked += blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True,
        }

    def get_combat_stats(self) -> Dict:
        return ({"attack_power": self.attack_power,
                "total_blocked": self.damage_blocked})

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        mana_used = 4
        self.mana = max(0, self.mana - mana_used)
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [str(t) for t in targets],
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> Dict:
        return {"mana": self.mana}
