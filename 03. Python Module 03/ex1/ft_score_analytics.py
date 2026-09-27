#!/usr/bin/env python3

def main():
    """Use of operators on lists"""
    print("\33[1m")
    print("===== \33[35mPayer Score Analytics\33[37m =====")
    import sys
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
    else:
        scores: int = []
        for i, arg in enumerate(sys.argv[1:]):
            try:
                scores.append(int(arg))
            except ValueError:
                print(f"'\33[36m{arg}\33[37m' is \33[31mnot a score\33[37m - "
                      "\33[33mIGNORED\33[37m")
        print(f"Scores processed: \33[36m{scores}\33[37m")
        print(f"Total players: \33[36m{len(scores)}\33[37m")
        print(f"Total score: \33[36m{sum(scores)}\33[37m")
        print(f"Average score: \33[36m{sum(scores) / len(scores)}\33[37m")
        print(f"High score: \33[36m{max(scores)}\33[37m")
        print(f"Low score: \33[36m{min(scores)}\33[37m")
        print(f"High score: \33[36m{max(scores) - min(scores)}\33[37m")
        print("\33[0m")


if __name__ == "__main__":
    main()
