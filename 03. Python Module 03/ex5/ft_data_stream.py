#!/usr/bin/env python3

def prng(seed: int):
    """Linear Congruential Generator"""
    while True:
        seed = (1103515245 * seed + 12345) % (2**31)
        yield seed


def game_event_stream(n: int, rng):
    """Yields n game events, one by one"""
    players = ("alice", "bob", "charlie", "diana", "eve")
    event_types = ("killed monster", "found treasure", "leveled up")
    for i in range(1, n + 1):
        chaos = next(rng)
        name = players[((i - 1) * chaos) % len(players)]
        level = ((i * 7 * chaos) % 20) + 1
        event_type = event_types[((i - 1) * chaos) % len(event_types)]
        yield (i, name, level, event_type)


def filter_high_level(stream, min_level: int):
    """Yields only events where player level >= min_level"""
    for event in stream:
        _event_id, _name, level, _event_type = event
        if level >= min_level:
            yield event


def filter_event_type(stream, wanted_type: str):
    """Yields only events matching a given event type"""
    for event in stream:
        _event_id, _name, _level, event_type = event
        if event_type == wanted_type:
            yield event


def take(stream, count: int):
    """Takes first count items from a stream using next()"""
    it = iter(stream)
    out = ()
    i = 0
    while i < count:
        try:
            out = out + (next(it),)
        except StopIteration:
            break
        i += 1
    return out


def fibonacci_stream():
    """Infinite Fibonacci generator"""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Prime checker"""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_stream():
    """Infinite prime generator"""
    x = 2
    while True:
        if is_prime(x):
            yield x
        x += 1


def main() -> None:
    n = 1000

    print("\n\33[1m===== \33[35mGame Data Stream Processor\33[37m =====")
    print(f"Processing \33[35m{n}\33[37m game events...")
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    rng = prng(42)
    for event_id, name, level, event_type in game_event_stream(n, rng):
        total += 1
        if total <= 3:
            print(f"Event \33[35m{event_id}\33[37m: Player \33[36m{name}"
                  f"\33[37m (level \33[36m{level}\33[37m) {event_type}")
        elif total == 4:
            print("...")
        if level >= 10:
            high_level += 1
        if event_type == "found treasure":
            treasure += 1
        if event_type == "leveled up":
            level_up += 1
    print("\n=== \33[35mStream Analytics\33[37m ===")
    print(f"Total events processed: \33[36m{total}\33[37m")
    print(f"High-level players (10+): \33[36m{high_level}\33[37m")
    print(f"Treasure events: \33[36m{treasure}\33[37m")
    print(f"Level-up events: \33[36m{level_up}\33[37m")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: (not relevant)")
    print("\n=== \33[35mGenerator Demonstration\33[37m ===")
    fib_first_ten = take(fibonacci_stream(), 10)
    print("Fibonacci sequence (first 10): ", end="")
    i = 0
    while i < len(fib_first_ten):
        end = ", " if i + 1 < len(fib_first_ten) else "\n"
        print(f"\33[36m{fib_first_ten[i]}\33[37m", end=end)
        i += 1
    primes_first_five = take(prime_stream(), 5)
    print("Prime numbers (first 5): ", end="")
    i = 0
    while i < len(primes_first_five):
        end = ", " if i + 1 < len(primes_first_five) else "\n"
        print(f"\33[36m{primes_first_five[i]}\33[37m", end=end)
        i += 1
    print("\33[0m")


if __name__ == "__main__":
    main()
