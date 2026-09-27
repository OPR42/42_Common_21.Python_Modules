from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n\33[1m=====\33[35m DataDeck Card Foundation \33[37m=====")
    print("\nTesting \33[35mAbstract Base Class Design\33[37m:")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\nCreatureCard Info:")
    print(f"\33[36m{creature.get_card_info()}\33[37m")
    print("\nPlaying \33[35mFire Dragon\33[37m with \33[36m6\33[37m "
          "mana available:")
    if creature.is_playable(6) is True:
        print("Playable: \33[32mTrue\33[37m")
    else:
        print("Playable: \33[31mFalse\33[37m")
    result = creature.play({"battlefield": []})
    print(f"Play result: \33[36m{result}\33[37m")
    print("\n\33[35mFire Dragon\33[37m attacks \33[35mGoblin Warrior\33[37m:")
    fight = creature.attack_target("Goblin Warrior")
    print(f"Attack result: \33[36m{fight}\33[37m")
    print("\nTesting \33[35minsufficient mana\33[37m (\33[36m3\33[37m "
          "available):")
    if creature.is_playable(3) is True:
        print("Playable: \33[32mTrue\33[37m")
    else:
        print("Playable: \33[31mFalse\33[37m")
    print("\nAbstract pattern \33[32msuccessfully\33[37m "
          "demonstrated!\n\33[0m")


if __name__ == "__main__":
    main()
