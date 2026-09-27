from typing import Dict, List
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        mana_pool = 5
        played = []
        mana_used = 0
        damage = 0
        targets_attacked = []
        creatures = [c for c in hand if isinstance(c, CreatureCard)]
        spells = [c for c in hand if isinstance(c, SpellCard)]
        creatures.sort(key=lambda c: c.cost)
        spells.sort(key=lambda c: c.cost)
        for c in creatures:
            if mana_used + c.cost <= mana_pool and c.name == "Goblin Warrior":
                played.append(c.name)
                mana_used += c.cost
                damage += c.attack
                targets_attacked.append("Enemy Player")
                battlefield.append(c.name)
        for s in spells:
            if mana_used + s.cost <= mana_pool and s.name == "Lightning Bolt":
                played.append(s.name)
                mana_used += s.cost
                damage += 3
                if "Enemy Player" not in targets_attacked:
                    targets_attacked.append("Enemy Player")
        return {
            "cards_played": played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        if "Enemy Player" in available_targets:
            return (["Enemy Player"] +
                    [t for t in available_targets if t != "Enemy Player"])
        return available_targets
