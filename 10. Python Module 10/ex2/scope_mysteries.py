#!/usr/bin/env python3

def mage_counter() -> callable:
    count = 0

    def inc() -> int:
        nonlocal count
        count += 1
        return count

    return inc


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def add(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add


def enchantment_factory(enchantment_type: str) -> callable:

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    mem: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        nonlocal mem  # noqa: F824
        mem[key] = value

    def recall(key: str) -> str:
        if key in mem:
            return mem[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("\n\33[1mTesting \33[35mmage counter\33[37m...")
    counter = mage_counter()
    print(f"Call 1: \33[36m{counter()}\33[37m")
    print(f"Call 2: \33[36m{counter()}\33[37m")
    print(f"Call 3: \33[36m{counter()}\33[37m")
    print("\nTesting \33[35mspell accumulator\33[37m...")
    accrued = spell_accumulator(0)
    print(f"Call 1: \33[36m{accrued(12)}\33[37m")
    print(f"Call 2: \33[36m{accrued(14)}\33[37m")
    print(f"Call 3: \33[36m{accrued(16)}\33[37m")
    print("\nTesting \33[35menchantment factory\33[37m...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(f"\33[36m{flaming('Sword')}\33[37m")
    print(f"\33[36m{frozen('Shield')}\33[37m")
    print("\nTesting \33[35mmemory vault\33[37m...")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    vault["store"]("target", "Dragon")
    print("Store 'spell': 'Fireball'")
    print("Store 'target': 'Dragon'")
    print(f"Recall 'spell': \33[36m{vault['recall']('spell')}\33[37m")
    print(f"Recall 'target': \33[36m{vault['recall']('target')}\33[37m")
    print(f"Recall 'missing': \33[36m{vault['recall']('mana')}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
