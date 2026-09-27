#!/usr/bin/env python3

def crisis_handler(filename: str) -> None:
    if filename == "standard_archive.txt":
        print("\n\33[33mROUTINE ACCESS\33[37m: Attempting access to "
              f"'\33[36m{filename}\33[37m'...")
    else:
        print("\n\33[31mCRISIS ALERT\33[37m: Attempting access to "
              f"'\33[36m{filename}\33[37m'...")
    try:
        with open(filename, "r") as archive:
            content = archive.read()
            print("\33[32mSUCCESS\33[37m: Archive recovered - "
                  f"''\33[36m{content}\33[37m''")
            print("STATUS: Normal operations \33[32mresumed\33[37m")

    except FileNotFoundError:
        print("\33[33mRESPONSE\33[37m: Archive not found in storage matrix")
        print("STATUS: Crisis handled, \33[32msystem stable\33[37m")

    except PermissionError:
        print("\33[33mRESPONSE\33[37m: Security protocols deny access")
        print("STATUS: Crisis handled, \33[32msecurity maintained\33[37m")

    except Exception:
        print("\33[33mRESPONSE\33[37m: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, \33[32msystem stable\33[37m")


def main() -> None:
    print("\n\33[1m===== \33[35mCYBER ARCHIVES - "
          "CRISIS RESPONSE SYSTEM \33[35m=====")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("\nAll crisis scenarios handled \33[32msuccessfully\33[37m. "
          "Archives secure.")
    print("\33[0m")


if __name__ == "__main__":
    main()
