from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n\33[1m=====\33[35m DataDeck Ability System \33[37m=====")
    print("\n\33[35mEliteCard\33[37m capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print("\nPlaying \33[35mArcane Warrior\33[37m (Elite Card):")
    card = EliteCard("Arcane Warrior", 4, "Epic", 5)
    card.play({})
    print("\n\33[35mCombat\33[37m phase:")
    attack = card.attack("Enemy")
    print(f"Attack result: \33[36m{attack}\33[37m")
    defense = card.defend(5)
    print(f"Defense result: \33[36m{defense}\33[37m")
    print("\n\33[35mMagic\33[37m phase:")
    spell = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: \33[36m{spell}\33[37m")
    mana = card.channel_mana(3)
    print(f"Mana channel: \33[36m{mana}\33[37m")
    print("\nMultiple interface implementation \33[32msuccessful\33[37m!")
    print("\33[0m")


if __name__ == "__main__":
    main()
