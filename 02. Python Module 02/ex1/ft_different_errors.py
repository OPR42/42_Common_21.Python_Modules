#!/usr/bin/env python3

def garden_operation(err_to_test) -> None:
    """Provokes errors to check"""
    try:
        if err_to_test == "ValueError":
            int("abc")
        elif err_to_test == "ZeroDivisionError":
            42 / 0
        elif err_to_test == "FileNotFoundError":
            open("the_cake_is_a_lie.404")
        elif err_to_test == "KeyError":
            dummy = {"nb": 42}
            dummy["plant"]

    except ValueError:
        print("Caught \33[33mValueError\33[37m: invalid literal for int()")

    except ZeroDivisionError:
        print("Caught \33[33mZeroDivisionError\33[37m: division by zero")

    except FileNotFoundError:
        print("Caught \33[33mFileNotFoundError\33[37m: no such file "
              "'the_cake_is_a_lie.404'")

    except KeyError:
        print("Caught \33[33mKeyError\33[37m: 'dummy\\plant'")


def test_multiple_errors() -> None:
    """Catches all error types with only one except"""
    try:
        int("abc") / 0

    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    """Tests error events"""
    print("\n\33[1m===== \33[35mGarden Error Types Demo\33[37m =====")
    print("\nTesting\33[35m ValueError\33[37m...")
    garden_operation("ValueError")
    print("\nTesting\33[35m ZeroDivisionError\33[37m...")
    garden_operation("ZeroDivisionError")
    print("\nTesting\33[35m FileNotFoundError\33[37m...")
    garden_operation("FileNotFoundError")
    print("\nTesting\33[35m KeyError\33[37m...")
    garden_operation("KeyError")
    print("\nTesting\33[35m multiple errors \33[37mtogether...")
    test_multiple_errors()
    print("\nAll error types\33[32m tested successfully\33[37m!\n")


if __name__ == "__main__":
    test_error_types()
