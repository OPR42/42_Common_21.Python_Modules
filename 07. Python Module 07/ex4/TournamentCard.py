from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int, rarity: str,
                 attack_power: int, rating: int) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.card_id: str = card_id
        self.attack_power: int = attack_power
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = rating

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return ({"card_played": self.name, "mana_used": self.cost,
                "effect": "Tournament card entered arena"})

    def attack(self, target) -> Dict:
        return ({"attacker": self.name, "target": str(target),
                "damage": self.attack_power})

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(2, incoming_damage)
        taken = incoming_damage - blocked
        return ({"defender": self.name, "damage_taken": taken,
                "blocked": blocked})

    def get_combat_stats(self) -> Dict:
        return {"attack_power": self.attack_power}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> Dict:
        return ({"id": self.card_id, "rating": self.rating,
                "record": f"{self.wins}-{self.losses}"})

    def get_tournament_stats(self) -> Dict:
        return ({"wins": self.wins, "losses": self.losses,
                "rating": self.rating})
