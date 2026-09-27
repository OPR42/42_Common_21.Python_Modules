#!/usr/bin/env python3

def main():
    """Use of sys.argv"""
    print("\33[1m")
    print("===== \33[35mCommand Quest\33[37m =====")
    import sys
    if len(sys.argv) < 2:
        print("No arguments provided!")
    print(f"Program name: \33[36m{sys.argv[0]}\33[37m")
    if len(sys.argv) >= 2:
        print(f"Arguments received: \33[36m{len(sys.argv) - 1}\33[37m")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"    Argument {i}:   \33[36m{arg}\33[37m")
    print(f"Total arguments: \33[36m{len(sys.argv)}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
