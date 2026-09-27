#!/usr/bin/env python3

def main() -> None:
    """Opens, reads and closes file"""
    print("\n\33[1m=====\33[35m CYBER ARCHIVES - "
          "DATA RECOVERY SYSTEM \33[37m=====")
    filename = "ancient_fragment.txt"
    print(f"\nAccessing Storage Vault: \33[36m{filename}\33[37m")
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("\33[31mERROR:\33[37m Storage vault not found.\n"
              "       Run data generator first.\n")
        return
    print("Connection established...\n")
    content = f.read()
    print("\33[35mRECOVERED DATA:\33[37m")
    print(f"\33[36m{content}\33[37m")
    f.close()
    print("\nData recovery \33[32mcomplete\33[37m. Storage unit "
          "\33[32mdisconnected\33[37m.")
    print("\33[0m")


if __name__ == "__main__":
    main()
