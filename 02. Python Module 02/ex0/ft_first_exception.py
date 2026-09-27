#!/usr/bin/env python3

def check_temperature(temp_str) -> int:
    """Checks temperature and handles error"""
    try:
        temp: int = int(temp_str)
        if temp >= 0 and temp <= 40:
            print(f"\33[32m{temp}\33[37m°C is perfect for plants!")
            return temp
        elif temp > 40:
            print(f"\33[31m{temp}\33[37m°C is too hot for plants (max 40°C)")
            return
        else:
            print(f"\33[36m{temp}\33[37m°C is too cold for plants (min 0°C)")
            return

    except ValueError:
        print(f"'\33[33m{temp_str}\33[37m' is not a valid number")
        return


def test_temperature_input() -> None:
    """Tests different temperature inputs"""
    print("\n\33[1m===== \33[35mGarden Temperature Checker\33[37m =====")
    print("\nTesting temperature:\33[35m 25 \33[37m")
    check_temperature("25")
    print("\nTesting temperature:\33[35m abc \33[37m")
    check_temperature("abc")
    print("\nTesting temperature:\33[35m 100 \33[37m")
    check_temperature("100")
    print("\nTesting temperature:\33[35m -50 \33[37m")
    check_temperature("-50")
    print("\nAll tests completed - \33[32mprogram didn't crash\33[37m!\n")


if __name__ == "__main__":
    test_temperature_input()
