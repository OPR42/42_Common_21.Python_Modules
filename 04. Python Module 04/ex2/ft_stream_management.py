#!/usr/bin/env python3

def main() -> None:
    """Tests stdin, stdout and stderr"""
    import sys
    print("\n\33[1m=====\33[35m CYBER ARCHIVES - "
          "COMMUNICATION SYSTEM \33[37m=====")
    archivist_id = input("Input Stream active. Enter archivist ID: \33[36m")
    status = input("\33[37mInput Stream active. Enter status report: \33[36m")
    sys.stdout.write("\n\33[36m[STANDARD]\33[37m Archive status from \33[36m"
                     f"{archivist_id}\33[37m: \33[36m{status}\33[37m\n")
    sys.stderr.write("\33[33m[ALERT]\33[37m System diagnostic: "
                     "Communication channels \33[32mverified\33[37m\n")
    sys.stdout.write("\33[36m[STANDARD]\33[37m Data transmission "
                     "\33[32mcomplete\33[37m\n")
    print("\nThree-channel communication test \33[32msuccessful\33[37m.")
    print("\33[0m")


if __name__ == "__main__":
    main()
