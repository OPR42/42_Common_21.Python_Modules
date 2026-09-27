from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        raise NotImplementedError
