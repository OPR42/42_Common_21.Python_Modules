#!/usr/bin/env python3

import time
from functools import wraps


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def deco(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None and args and isinstance(args[-1], int):
                power = args[-1]
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return deco


def retry_spell(max_attempts: int) -> callable:
    def deco(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempt += 1
                    if attempt < max_attempts:
                        print("Spell failed, retrying... (attempt \33[36m"
                              f"{attempt}\33[37m/{max_attempts})")
            return (f"Spell casting failed after \33[36m{max_attempts}"
                    "\33[31m attempts")
        return wrapper
    return deco


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        cleaned = name.strip()
        if len(cleaned) < 3:
            return False
        for ch in cleaned:
            if not (ch.isalpha() or ch == " "):
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast \33[36m{spell_name}\33[32m with "
                f"\33[36m{power}\33[32m power")


def main() -> None:
    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    @retry_spell(max_attempts=3)
    def unstable_teleport() -> str:
        if not hasattr(unstable_teleport, "tries"):
            unstable_teleport.tries = 0
        unstable_teleport.tries += 1
        if unstable_teleport.tries < 3:
            raise RuntimeError("Portal collapsed")
        return "Teleport successful!"

    @retry_spell(max_attempts=2)
    def always_fails() -> str:
        raise ValueError("Mana overload")

    @power_validator(min_power=50)
    def meteor(target: str, power: int) -> str:
        return (f"Meteor strikes \33[36m{target}\33[32m with \33[36m{power}"
                "\33[32m power!")

    print("\n\33[1mTesting\33[35m spell_timer\33[37m...")
    result = fireball()
    print(f"Result: \33[36m{result}\33[37m")
    print("\nTesting\33[35m retry_spell (eventual success)\33[37m...")
    print(f"Result: \33[32m{unstable_teleport()}\33[37m")
    print("\nTesting\33[35m retry_spell (always fails)\33[37m...")
    print(f"Result: \33[31m{always_fails()}\33[37m")
    print("\nTesting\33[35m power_validator on a normal function\33[37m...")
    print(f"Low power:  \33[33m{meteor('Castle', 10)}\33[37m")
    print(f"High power: \33[32m{meteor('Castle', 80)}\33[37m")
    print("\nTesting\33[35m MageGuild.validate_mage_name\33[37m "
          "(staticmethod)...")
    print(f"Alex: \33[36m{MageGuild.validate_mage_name('Alex')}\33[37m")
    print(f"A1:   \33[36m{MageGuild.validate_mage_name('A1')}\33[37m")
    print(f"' Nemo ': \33[36m{MageGuild.validate_mage_name(' Nemo ')}\33[37m")
    print("\nTesting\33[35m MageGuild.cast_spell\33[37m (method + "
          "power_validator)...")
    guild = MageGuild()
    print(f"Power 20: \33[32m{guild.cast_spell('Lightning', 20)}\33[37m")
    print(f"Power  5: \33[33m{guild.cast_spell('Lightning', 5)}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
