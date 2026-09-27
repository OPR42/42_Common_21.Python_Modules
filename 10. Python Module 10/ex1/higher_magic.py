#!/usr/bin/env python3

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequencer(*args, **kwargs):
        return [s(*args, **kwargs) for s in spells]
    return sequencer


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("\n\33[1mTesting \33[35mspell combiner\33[37m...")
    combined = spell_combiner(fireball, heal)
    r1, r2 = combined("Dragon")
    print(f"Combined spell result: \33[36m{r1}\33[37m, \33[36m{r2}\33[37m")
    print("\nTesting \33[35mpower amplifier\33[37m...")

    def base_damage() -> int:
        return 10

    amp = power_amplifier(base_damage, 3)
    print(f"Original: \33[36m{base_damage()}\33[37m, Amplified: "
          f"\33[36m{amp()}\33[37m")
    print("\nTesting \33[35mconditional caster\33[37m...")

    def has_mana(target: str) -> bool:
        return target != "Dragon"

    cast_if_mana = conditional_caster(has_mana, fireball)
    ok = cast_if_mana("Goblin")
    ko = cast_if_mana("Dragon")
    print(f"Cast on Goblin: \33[32m{ok}\33[37m")
    print(f"Cast on Dragon: \33[31m{ko}\33[37m")
    print("\nTesting \33[35mspell sequence\33[37m...")
    seq = spell_sequence([fireball, heal])
    results = seq("Knight")
    print("Sequence result: ", end="")
    print(", ".join(f"\33[36m{r}\33[37m" for r in results))
    print("\33[0m")


if __name__ == "__main__":
    main()
