#!/usr/bin/env python3

import importlib
import sys
from typing import Any, Dict, Optional, Tuple


def _import_or_none(module_name: str) -> Optional[Any]:
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        return None


def _module_version(mod: Any) -> str:
    ver = getattr(mod, "__version__", None)
    if isinstance(ver, str) and ver:
        return ver
    return "unknown"


def _check_deps() -> Tuple[bool, Dict[str, Optional[Any]]]:
    mods: Dict[str, Optional[Any]] = {
        "pandas": _import_or_none("pandas"),
        "requests": _import_or_none("requests"),
        "matplotlib": _import_or_none("matplotlib"),
        "numpy": _import_or_none("numpy"),
    }
    ok = True
    for name in mods:
        if mods[name] is None:
            ok = False
    return ok, mods


def _print_deps(mods: Dict[str, Optional[Any]]) -> None:
    print("\nChecking \33[35mdependencies\33[37m:")
    for name, mod in mods.items():
        if mod is None:
            print(f"\33[31m[MISSING]\33[36m {name}\33[37m - Install required")
        else:
            print(f"\33[32m[OK] \33[36m{name}\33[37m "
                  f"(\33[36m{_module_version(mod)}\33[37m) - Ready")


def _install_help() -> None:
    print("\nDependencies missing.")
    print("Install with pip:")
    print("\33[0m\33[3mpip install -r requirements.txt\33[0m\33[1m")
    print("\n\33[37mOr install with Poetry:")
    print("\33[0m\33[3mpoetry install")
    print("poetry run python loading.py\33[0m\33[1m\n")


def _simulate_matrix_data(numpy_mod: Any) -> Any:
    np = numpy_mod
    x = np.arange(0, 1000, dtype=float)
    signal = np.sin(x / 50.0) * 10.0
    noise = (np.mod(x * 17.0, 7.0) - 3.0) * 0.3
    y = signal + noise
    return x, y


def _analyze_and_plot(mods: Dict[str, Optional[Any]]) -> None:
    pd = mods["pandas"]
    np = mods["numpy"]
    mpl = mods["matplotlib"]
    if pd is None or np is None or mpl is None:
        raise RuntimeError("\33[31mMissing\33[37m core dependencies "
                           "for analysis")
    plt = importlib.import_module("matplotlib.pyplot")
    print("\n\33[35mAnalyzing Matrix data\33[37m...")
    print("Processing \33[36m1000\33[37m data points...")
    x, y = _simulate_matrix_data(np)
    df = pd.DataFrame({"tick": x, "signal": y})
    df["rolling_mean"] = df["signal"].rolling(window=25).mean()
    print("Generating \33[35mvisualization\33[37m...")
    plt.figure()
    plt.plot(df["tick"], df["signal"], label="signal")
    plt.plot(df["tick"], df["rolling_mean"], label="rolling_mean")
    plt.title("Matrix Analysis")
    plt.xlabel("tick")
    plt.ylabel("signal")
    plt.legend()
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis \33[32mcomplete\33[37m!")
    print("Results saved to: \33[36mmatrix_analysis.png\33[37m\33[0m\n")


def main() -> None:
    print("\n\33[1m\33[35mLOADING STATUS\33[37m: Loading programs...")
    ok, mods = _check_deps()
    _print_deps(mods)
    if not ok:
        _install_help()
        return
    try:
        _analyze_and_plot(mods)
    except Exception as exc:
        print("\33[31mERROR\33[37m: Analysis failed.")
        print(f"Reason: \33[36m{exc}\33[37m")
        print("\33[33mTip\33[37m: verify your environment and dependencies."
              "\33[0m\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
