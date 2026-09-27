from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        raise NotImplementedError
