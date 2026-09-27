from typing import Any, Dict, List
from ex0.Card import Card


class SpellCard(Card):
    def __init__(
                self, name: str,
                cost: int,
                rarity: str,
                effect_type: str
                ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.effect_type: str = effect_type

    def resolve_effect(self, targets: List[Any]) -> Dict[str, Any]:
        target_names = [str(t) for t in targets]
        return ({"spell": self.name, "effect_type": self.effect_type,
                "targets": target_names})

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        effect = self._effect_description()
        return ({"card_played": self.name, "mana_used": self.cost,
                "effect": effect})

    def _effect_description(self) -> str:
        if self.name == "Lightning Bolt":
            return "Deal 3 damage to target"
        if self.effect_type == "heal":
            return "Restore 3 health to target"
        if self.effect_type == "buff":
            return "Buff target creature"
        if self.effect_type == "debuff":
            return "Debuff target creature"
        return "Spell effect resolved"

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info
