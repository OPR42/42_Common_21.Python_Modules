#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    max_p = max(mages, key=lambda m: m["power"])["power"]
    min_p = min(mages, key=lambda m: m["power"])["power"]
    total = sum(map(lambda m: m["power"], mages))
    avg = round(total / len(mages), 2)
    return {"max_power": max_p, "min_power": min_p, "avg_power": avg}


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Dagger", "power": 12, "type": "weapon"},
    ]
    spells = ["fireball", "heal", "shield"]
    print("\n\33[1mTesting \33[35martifact sorter\33[37m...")
    sorted_artifacts = artifact_sorter(artifacts)
    a0 = sorted_artifacts[0]
    a1 = sorted_artifacts[1]
    print(f"\33[36m{a0['name']}\33[37m (\33[36m{a0['power']}\33[37m power) "
          f"comes before \33[36m{a1['name']}\33[37m (\33[36m{a1['power']}"
          "\33[37m power)")
    print("\nTesting \33[35mpower filter\33[37m")
    filtered_artifacts = power_filter(artifacts, 20)
    filtered_names = ", ".join(
        f"\33[36m{artifact['name']}\33[37m"
        for artifact in filtered_artifacts
    )
    print(f"Artifacts stronger than 20: {filtered_names}")
    print("\nTesting \33[35mspell transformer\33[37m...")
    transformed = spell_transformer(spells)
    print(f"\33[36m{" ".join(transformed)}\33[37m")
    print("\nTesting \33[35mmage stats\33[37m...")
    mages = [
        {"name": "Merlin", "power": 80},
        {"name": "Rincewind", "power": 4},
        {"name": "Gandalf", "power": 100},
    ]
    stats = mage_stats(mages)
    labels = {
        "max_power": "Max power",
        "min_power": "Min power",
        "avg_power": "Avg power"
    }
    for key, label in labels.items():
        print(f"{label}: \33[36m{stats[key]}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
