from typing import Dict, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.hand: List = []
        self.battlefield: List = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature("Fire Dragon"),
            factory.create_creature("Goblin Warrior"),
            factory.create_spell("Lightning Bolt"),
        ]
        self.cards_created = 3

    def simulate_turn(self) -> Dict:
        if self.factory is None or self.strategy is None:
            raise ValueError("Engine not configured")

        self.turns_simulated += 1
        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.total_damage += int(actions.get("damage_dealt", 0))
        return {
            "Strategy": self.strategy.get_strategy_name(),
            "Actions": actions,
        }

    def get_engine_status(self) -> Dict:
        if self.strategy is None:
            strategy_name = "None"
        else:
            strategy_name = self.strategy.get_strategy_name()
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
