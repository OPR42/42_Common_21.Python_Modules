from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n\33[1m=====\33[35m DataDeck Tournament Platform \33[37m=====")
    platform = TournamentPlatform()
    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary",
                            7, 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic", 5, 1150)
    platform.register_card(dragon)
    platform.register_card(wizard)
    print("\n\33[36mFire Dragon\33[37m (ID: dragon_001):")
    print("- Interfaces: \33[36m[Card, Combatable, Rankable]\33[37m")
    print("- Rating: \33[36m1200\33[37m")
    print("- Record: \33[36m0-0\33[37m")
    print("\n\33[36mIce Wizard\33[37m (ID: wizard_001):")
    print("- Interfaces: \33[36m[Card, Combatable, Rankable]\33[37m")
    print("- Rating: \33[36m1150\33[37m")
    print("- Record: \33[36m0-0\33[37m")
    print("\nCreating\33[35m tournament\33[37m match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: \33[36m{result}\33[37m")
    print("\n\33[35mTournament\33[37m Leaderboard:")
    board = platform.get_leaderboard()
    for i, c in enumerate(board, start=1):
        print(f"{i}. \33[36m{c.name}\33[37m - Rating: \33[36m{c.rating}"
              f"\33[37m (\33[36m{c.wins}\33[37m-\33[36m{c.losses}\33[37m)")
    print("\n\33[35mPlatform\33[37m Report:")
    print(f"\33[36m{platform.generate_tournament_report()}\33[37m")
    print("\n===\33[35m Tournament Platform\33[37m \33[32mSuccessfully\33[37m"
          " Deployed! ===")
    print("All abstract patterns\33[32m working together harmoniously"
          "\33[37m!\n\33[0m")


if __name__ == "__main__":
    main()
