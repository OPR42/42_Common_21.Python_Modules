#!/usr/bin/env python3

from alchemy.grimoire import record_spell, validate_ingredients


def main() -> None:
    print("\n\33[1m=====\33[35m Circular Curse Breaking \33[37m=====")

    print("\nTesting\33[35m ingredient validation\33[37m:")
    print("validate_ingredients(\"fire air\"): "
          f"{validate_ingredients("fire air")}")
    print("validate_ingredients(\"dragon scales\"): "
          f"{validate_ingredients("dragon scales")}")
    print("\nTesting \33[35mspell recording with validation\33[37m:")
    print("record_spell(\"Fireball\", \"fire air\"): "
          f"{record_spell("Fireball", "fire air")}")
    print("record_spell(\"Dark Magic\", \"shadow\"): "
          f"{record_spell("Dark Magic", "shadow")}")
    print("\nTesting \33[35mlate import technique\33[37m:")
    print("record_spell(\"Lightning\", \"air\"): "
          f"{record_spell("Lightning", "air")}")

    print("\nCircular dependency curse \33[32mavoided\33[37m using late "
          "imports!")
    print("All spells processed \33[32msafely\33[37m!\33[0m\n")


if __name__ == "__main__":
    main()
