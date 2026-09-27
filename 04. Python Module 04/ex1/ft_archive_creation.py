#!/usr/bin/env python3

def main() -> None:
    """Creates new file ans writes into it"""
    print("\n\33[1m=====\33[35m CYBER ARCHIVES - "
          "PRESERVATION SYSTEM \33[37m=====")
    filename = "new_discovery.txt"
    print(f"\nInitializing new storage unit: \33[36m{filename}\33[37m")
    try:
        f = open(filename, "x")
    except FileExistsError:
        print(f"\33[31mERROR:\33[37m \33[36m{filename}\33[37m "
              "already exists.\n       First secure existing archive.\n")
        return
    print("Storage unit created \33[32msuccessfully\33[37m...\n")
    content = ("[ENTRY 001] New quantum algorithm discovered\n"
               "[ENTRY 002] Efficiency increased by 347%\n"
               "[ENTRY 003] Archived by Data Archivist trainee")
    print("Inscribing preservation data...")
    f.write(f"{content}")
    print(f"\33[36m{content}\33[37m")
    f.close()
    print("\nData inscription \33[32mcomplete\33[37m. Storage unit "
          "\33[32msealed\33[37m.")
    print(f"Archive '\33[36m{filename}\33[37m' ready for \33[35mlong-term "
          "preservation\33[37m.")
    print("\33[0m")


if __name__ == "__main__":
    main()
