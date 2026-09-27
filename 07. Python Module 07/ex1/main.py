from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("\n\33[1m=====\33[35m DataDeck Deck Builder \33[37m=====")
    print("\n\33[35mBuilding deck\33[37m with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 4, "Common", 3,
                               "Permanent: +1 mana per turn"))
    print(f"Deck stats: \33[36m{deck.get_deck_stats()}\33[37m")
    print("\n\33[35mDrawing\33[37m and \33[35mplaying\33[37m cards:")
    deck.shuffle()
    for _ in range(3):
        card = deck.draw_card()
        print(f"\nDrew: \33[36m{card.name}\33[37m "
              f"(\33[36m{card.get_card_info()['type']}\33[37m)")
        print(f"Play result: \33[36m{card.play({})}\33[37m")
    print("\nPolymorphism \33[32min action\33[37m: Same interface, "
          "different card behaviors!\n\33[0m")


if __name__ == "__main__":
    main()
