from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0
        self.platform_status: str = "active"

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        self.matches_played += 1
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]
        if c1.rating >= c2.rating:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1
        winner.update_wins(1)
        loser.update_losses(1)
        return ({"winner": winner.card_id, "loser": loser.card_id,
                "winner_rating": winner.rating, "loser_rating": loser.rating})

    def get_leaderboard(self) -> List[TournamentCard]:
        return sorted(self.cards.values(), key=lambda c: c.rating,
                      reverse=True)

    def generate_tournament_report(self) -> Dict:
        total_cards = len(self.cards)
        avg = 0
        if total_cards:
            avg = sum([c.rating for c in self.cards.values()]) // total_cards
        return ({"total_cards": total_cards,
                 "matches_played": self.matches_played, "avg_rating": avg,
                 "platform_status": self.platform_status})
