#!/usr/bin/env python3

import os
import site
import sys


def _venv_name(venv_path: str) -> str:
    """directory name of venv path."""
    parts = venv_path.rstrip("/").split("/")
    if parts:
        return parts[-1]
    return "unknown_env"


def _is_in_venv() -> bool:
    """detects venv"""
    base = getattr(sys, "base_prefix", sys.prefix)
    if sys.prefix != base:
        return True
    if os.environ.get("VIRTUAL_ENV"):
        return True
    return False


def _print_outside(python_path: str) -> None:
    print("\n\33[1m\33[35mMATRIX STATUS\33[37m: "
          "You're still 🔵 \33[34mplugged in\33[37m 🔵")
    print(f"\nCurrent Python: \33[36m{python_path}\33[37m")
    print("Virtual Environment: None detected")
    print("\n\33[31mWARNING\33[37m: You're in the "
          "\33[34mglobal environment\33[37m!")
    print("The machines can see everything you install.")
    print("\nTo \33[33menter the construct\33[37m, run:")
    print("- on Unix:")
    print("\33[0m\33[3mpython -m venv matrix_env")
    print("source matrix_env/bin/activate\33[0m\33[1m\33[37m")
    print("- on Windows:")
    print("\33[0m\33[3mmatrix_env")
    print("Scripts")
    print("activate\33[0m\33[1m\33[37m")
    print("\nThen run this program again.\n\33[0m")


def _print_inside(python_path: str, venv_path: str) -> None:
    venv = _venv_name(venv_path)
    print("\n\33[1m\33[35mMATRIX STATUS\33[37m: "
          "Welcome to 🔴 \33[31mthe construct\33[37m 🔴")
    print(f"\nCurrent Python: \33[36m{python_path}\33[37m")
    print(f"Virtual Environment: \33[36m{venv}\33[37m")
    print(f"Environment Path: \33[36m{venv_path}\33[37m")
    print("\n\33[32mSUCCESS\33[37m: You're in an "
          "\33[31misolated environment\33[37m!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    paths = site.getsitepackages()
    if paths:
        print(f"\33[36m{paths[0]}\33[37m\n\33[0m")
    else:
        print("\33[36m(unknown site-packages path)\33[37m\n\33[0m")


def main() -> None:
    in_venv = _is_in_venv()
    python_path = sys.executable
    if not in_venv:
        _print_outside(python_path)
        return
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    _print_inside(python_path, venv_path)


if __name__ == "__main__":
    main()
