from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n\33[1m=====\33[35m DataDeck Game Engine \33[37m=====")
    print("\nConfiguring\33[35m Fantasy Card\33[37m Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print(f"Factory: \33[36m{factory.__class__.__name__}\33[37m")
    print(f"Strategy: \33[36m{strategy.get_strategy_name()}\33[37m")
    print(f"Available types: \33[36m{factory.get_supported_types()}\33[37m")
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print("\nSimulating \33[35maggressive\33[37m turn.")
    print(
        "Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]"
    )
    turn = engine.simulate_turn()
    print("\n\33[35mTurn\33[37m execution:")
    print(f"Strategy: \33[36m{turn['Strategy']}\33[37m")
    print(f"Actions: \33[36m{turn['Actions']}\33[37m")
    print("\n\33[35mGame\33[37m Report:")
    print(f"\33[36m{engine.get_engine_status()}\33[37m")
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility "
          "\33[32machieved\33[37m!\n\33[0m")


if __name__ == "__main__":
    main()
