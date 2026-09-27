from abc import ABC, abstractmethod
from typing import Dict, List


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def get_strategy_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        raise NotImplementedError
