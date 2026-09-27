#!/usr/bin/env python3

def main() -> None:
    print("\n\33[1m=====\33[35m Game Analytics Dashboard \33[37m=====")
    players = [
        {"name": "Alice", "score": 2300, "active": True,  "region": "north",
         "achievements": {"first_kill", "level_10", "boss_slayer",
                          "collector", "speedrun"}},
        {"name": "Bob", "score": 1800, "active": True,  "region": "east",
         "achievements": {"first_kill", "level_10", "trader"}},
        {"name": "Charlie", "score": 2150, "active": True, "region": "central",
         "achievements": {"first_kill", "boss_slayer", "explorer", "builder",
                          "crafter", "level_10", "survivor"}},
        {"name": "Diana", "score": 1200, "active": False, "region": "north",
         "achievements": {"first_kill"}},
    ]
    print("\n===\33[35m List Comprehension Examples \33[37m===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): \33[36m{high_scorers}\33[37m")
    doubled_scores = [p["score"] * 2 for p in players]
    print(f"Scores doubled: \33[36m{doubled_scores}\33[37m")
    active_players = [p["name"] for p in players if p["active"]]
    print(f"Active players: \33[36m{active_players}\33[37m")
    print("\n===\33[35m Dict Comprehension Examples \33[37m===")
    player_scores = {p["name"]: p["score"] for p in players}
    print(f"Player scores: \33[36m{player_scores}\33[37m")
    categories = ["high", "medium", "low"]
    score_categories = {
        c: len([p for p in players if (
            (c == "high" and p["score"] > 2000)
            or (c == "medium" and 1500 <= p["score"] <= 2000)
            or (c == "low" and p["score"] < 1500)
        )])
        for c in categories
    }
    print(f"Score categories: \33[36m{score_categories}\33[37m")
    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
    print(f"Achievement counts: \33[36m{achievement_counts}\33[37m")
    print("\n===\33[35m Set Comprehension Examples \33[37m===")
    unique_players = {p["name"] for p in players}
    print(f"Unique players: \33[36m{unique_players}\33[37m")
    unique_achievements = {a for p in players for a in p["achievements"]}
    print(f"Unique achievements: \33[36m{unique_achievements}\33[37m")
    active_regions = {p["region"] for p in players if p["active"]}
    print(f"Active regions: \33[36m{active_regions}\33[37m")
    print("\n===\33[35m Combined Analysis \33[37m===")
    all_scores = [p["score"] for p in players]
    total_players = len(players)
    total_unique_ach = len(unique_achievements)
    avg_score = sum(all_scores) / len(all_scores) if len(all_scores) else 0
    top_score = max(all_scores) if len(all_scores) else 0
    top_candidates = [p for p in players if p["score"] == top_score]
    top = top_candidates[0] if len(top_candidates) else {
        "name": "n/a", "score": 0, "achievements": set()}
    print(f"Total players: \33[36m{total_players}\33[37m")
    print(f"Total unique achievements: \33[36m{total_unique_ach}\33[37m")
    print(f"Average score: \33[36m{avg_score:.1f}\33[37m")
    print(f"Top performer: \33[36m{top['name']}\33[37m "
          f"(\33[36m{top['score']}\33[37m points, "
          f"\33[36m{len(top['achievements'])}\33[37m achievements)")
    leaderboard = sorted([(p["score"], p["name"]) for p in players],
                         reverse=True)
    print("\nLeaderboard (score, player):")
    print(f"\33[36m{leaderboard}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
