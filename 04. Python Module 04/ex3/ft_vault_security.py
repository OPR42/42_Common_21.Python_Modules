#!/usr/bin/env python3

def main() -> None:
    """Tests 'with' """
    print("\n\33[1m===\33[35m CYBER ARCHIVES - "
          "VAULT SECURITY SYSTEM \33[37m=====\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\n\33[35mSECURE EXTRACTION\33[37m:")
    try:
        with open("classified_data.txt", "r") as file:
            data = file.read()
            print(f"\33[36m{data}\33[37m")
    except FileNotFoundError:
        print("\33[31m[ERROR]\33[37m No existing vault data found")
    print("\n\33[35mSECURE PRESERVATION\33[37m:")
    text = "[CLASSIFIED] New security protocols archived"
    try:
        with open("security_protocols.txt", "x") as vault:
            vault.write(f"{text}")
            print(f"\33[36m{text}\33[37m\n")
    except FileExistsError:
        print("\33[31mERROR:\33[37m \33[36msecurity_protocols.txt\33[37m "
              "already exists.\n       First secure existing archive.\n")
        return
    print("Vault automatically \33[32msealed\33[37m upon completion\n")
    print("All vault operations \33[32mcompleted\33[37m "
          "with maximum security.")
    print("\33[0m")


if __name__ == "__main__":
    main()
