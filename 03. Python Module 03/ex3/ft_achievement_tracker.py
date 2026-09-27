#!/usr/bin/env python3

def main() -> None:
    """Testing sets"""
    print("\33[01m\n=====\33[35m Achievment Tracker System \33[37m=====\n")
    alice = set(('first_kill', 'level_10', 'treasure_hunter', 'speed_demon'))
    bob = set(('first_kill', 'level_10', 'boss_slayer', 'collector'))
    charlie = set(('level_10', 'treasure_hunter', 'boss_slayer',
                   'speed_demon', 'perfectionnist'))
    print(f"Player Alice achievments: \33[36m{alice}\33[37m")
    print(f"Player Bob achievments: \33[36m{bob}\33[37m")
    print(f"Player Charlie achievments: \33[36m{charlie}\33[37m")
    print("\n=====\33[35m Achievment Analytics \33[37m=====")
    unique = alice.union(bob).union(charlie)
    print(f"All unique achievments: \33[36m{unique}\33[37m")
    print(f"Total unique achievments: \33[36m{len(unique)}\33[37m\n")
    common = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: \33[36m{common}\33[37m")
    rare = unique.difference(alice.intersection(bob).union(alice.intersection(
           charlie)).union(bob.intersection(charlie)))
    print(f"Rare achievments (1 player): \33[36m{rare}\33[37m\n")
    print(f"Alice vs Bob common: \33[36m{alice.intersection(bob)}\33[37m")
    print(f"Alice unique: \33[36m{alice.difference(bob)}\33[37m")
    print(f"Bob unique: \33[36m{bob.difference(alice)}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
