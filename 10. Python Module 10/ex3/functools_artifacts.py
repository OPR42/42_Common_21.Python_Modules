#!/usr/bin/env python3

import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in ops:
        raise ValueError("Unsupported operation")
    op = ops[operation]
    if operation in ("max", "min"):
        return functools.reduce(lambda a, b: op(a, b), spells)
    return functools.reduce(op, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment,
            50,
            "lightning"
            ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatch(value):
        return "Unknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return f"Damage spell: {value} dmg"

    @dispatch.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatch


def main() -> None:
    spells = [10, 20, 30, 40]
    print("\n\33[1mTesting \33[35mspell reducer\33[37m...")
    print(f"Sum : \33[36m{spell_reducer(spells, 'add')}\33[37m")
    print(f"Product: \33[36m{spell_reducer(spells, 'multiply')}\33[37m")
    print(f"Max: \33[36m{spell_reducer(spells, 'max')}\33[37m")
    print(f"Min: \33[36m{spell_reducer(spells, 'min')}\33[37m")
    print(f"Empty list add: \33[36m{spell_reducer([], 'add')}\33[37m")
    try:
        spell_reducer(spells, "divide")
    except ValueError as e:
        print(f"\33[31mExpected error\33[37m: {e}")
    print("\nTesting \33[35mpartial enchanter\33[37m...")

    def base_enchantment(power: int, element: str, item: str) -> str:
        return f"{element.title()} enchant on {item} with power {power}"

    enchants = partial_enchanter(base_enchantment)
    print(f"\33[36m{enchants['fire_enchant']('Sword')}\33[37m")
    print(f"\33[36m{enchants['ice_enchant']('Shield')}\33[37m")
    print(f"\33[36m{enchants['lightning_enchant']('Staff')}\33[37m")
    print("\nTesting \33[35mmemoized fibonacci\33[37m...")
    print(f"Fib(10): \33[36m{memoized_fibonacci(10)}\33[37m")
    print(f"Fib(15): \33[36m{memoized_fibonacci(15)}\33[37m")
    print(f"Fib(30): \33[36m{memoized_fibonacci(30)}\33[37m")
    try:
        memoized_fibonacci(-1)
    except ValueError as e:
        print(f"\33[31mExpected error\33[37m: {e}")
    print("\nTesting \33[35mspell dispatcher\33[37m...")
    dispatch = spell_dispatcher()
    print(f"Dispatch int: \33[36m{dispatch(42)}\33[37m")
    print(f"Dispatch str: \33[36m{dispatch('Flaming Sword')}\33[37m")
    print(f"Dispatch list: \33[36m{dispatch(['fireball', 'heal', 'icebolt'])}"
          "\33[37m")
    print(f"Dispatch unknown: \33[36m{dispatch(3.14)}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
