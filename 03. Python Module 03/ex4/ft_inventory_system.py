#!/usr/bin/env python3

def main() -> None:
    """Testing dicts"""
    import sys
    if len(sys.argv) < 2:
        print("No item provided. Usage: python3 ft_inventory_system.py"
              " <item1:qty1> <item2:qty2> ...")
        return
    print("\33[1m")
    print("===== \33[35mInventory System Analysis\33[37m =====")
    inv = dict()
    for i, arg in enumerate(sys.argv[1:]):
        pair = arg.split(":")
        try:
            if len(pair) != 2 or pair[0] == "":
                raise ValueError
            inv[pair[0]] = int(pair[1])
        except ValueError:
            print(f"'\33[36m{arg}\33[37m' is \33[31minvalid\33[37m - "
                  "\33[33mIGNORED\33[37m")
    total_qty: int = 0
    for value in inv.values():
        total_qty += value
    print(f"Total items in inventory: \33[36m{total_qty}\33[37m")
    print(f"Unique item types: \33[36m{len(inv)}\33[37m")
    print("\n=== \33[35mCurrent Inventory\33[37m ===")
    abundant = {}
    moderate = {}
    scarce = {}
    restock = []
    keys = []
    values = []
    for key, value in inv.items():
        print(f"{key}: \33[36m{value}\33[37m unit{'s' if value > 1 else ''} "
              f"(\33[36m{((value * 100) / total_qty):.1f}\33[37m%)")
        if value >= 10:
            abundant[key] = value
        elif value >= 5:
            moderate[key] = value
        else:
            scarce[key] = value
        if value == 1:
            restock.append(key)
        keys.append(key)
        values.append(value)
    print("\n=== \33[35mInventory Statistics\33[37m ===")
    most_item = max(inv, key=inv.get)
    least_item = min(inv, key=inv.get)
    print(f"Most abundant: {most_item} (\33[36m{inv[most_item]}\33[37m "
          f"unit{'s' if inv[most_item] > 1 else ''})")
    print(f"Least abundant: {least_item} (\33[36m{inv[least_item]}\33[37m "
          f"unit{'s' if inv[least_item] > 1 else ''})")
    print("\n=== \33[35mItem Categories\33[37m ===")
    print(f"Abundant: \33[36m{abundant}\33[37m")
    print(f"Moderate: \33[36m{moderate}\33[37m")
    print(f"Scarce: \33[36m{scarce}\33[37m")
    print("\n=== \33[35mManagement Suggestions\33[37m ===")
    print(f"Restock needed: \33[36m{restock}\33[37m")
    print("\n=== \33[35mDictionary Properties Demo\33[37m ===")
    print(f"Dictionary keys: \33[36m{keys}\33[37m")
    print(f"Dictionary values: \33[36m{values}\33[37m")
    sword_inv = "sword" in inv
    print(f"Sample lookup - 'sword' in inventory: "
          f"{"\33[32m" if sword_inv is True else "\33[31m"}{sword_inv}\33[37m")
    print("\33[0m")


if __name__ == "__main__":
    main()
