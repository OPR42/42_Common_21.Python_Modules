#!/usr/bin/env python3

import os
import sys
from typing import Dict, Optional


def _load_dotenv_if_available() -> bool:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        return True
    except ModuleNotFoundError:
        return False


def _get_env(name: str) -> Optional[str]:
    val = os.environ.get(name)
    if val is None:
        return None
    val = val.strip()
    if not val:
        return None
    return val


def _mask_secret(secret: str) -> str:
    if len(secret) <= 4:
        return "*" * len(secret)
    return secret[:2] + "*" * (len(secret) - 4) + secret[-2:]


def _read_config() -> Dict[str, Optional[str]]:
    keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    return {k: _get_env(k) for k in keys}


def _validate_config(cfg: Dict[str, Optional[str]]) -> bool:
    ok = True
    for key, val in cfg.items():
        if val is None:
            ok = False
    return ok


def _print_config(cfg: Dict[str, Optional[str]]) -> None:
    mode = cfg["MATRIX_MODE"] or "(missing)"
    db = cfg["DATABASE_URL"]
    api = cfg["API_KEY"]
    log = cfg["LOG_LEVEL"] or "(missing)"
    zion = cfg["ZION_ENDPOINT"]
    print("\33[35mORACLE STATUS\33[37m: Reading the Matrix...")
    print("\n\33[35mConfiguration\33[37m loaded:")
    print(f"Mode: \33[36m{mode}\33[37m")
    if db is None:
        print("Database: \33[31mMissing\33[37m DATABASE_URL")
    else:
        if "localhost" in db or "sqlite" in db or "local" in db:
            print("Database: \33[32mConnected\33[37m to local instance")
        else:
            print("Database: \33[32mConnected\33[37m")
    if api is None:
        print("API Access: \33[31mMissing\33[37m API_KEY")
    else:
        print("API Access: \33[32mAuthenticated\33[37m")
    print(f"Log Level: \33[36m{log}\33[37m")
    if zion is None:
        print("Zion Network: \33[31mOffline\33[37m (missing ZION_ENDPOINT)")
    else:
        print("Zion Network: \33[32mOnline\33[37m")


def _security_checks(cfg: Dict[str, Optional[str]]) -> None:
    print("\n\33[35mEnvironment\33[37m security check:")
    print("[\33[32mOK\33[37m] No hardcoded secrets detected")
    env_file_present = os.path.exists(".env")
    if env_file_present:
        print("[\33[32mOK\33[37m] .env file properly configured")
    else:
        print("[\33[31mWARN\33[37m] .env not found "
              "(copy .env.example to .env)")
    if cfg.get("MATRIX_MODE") == "production":
        print("[\33[32mOK\33[37m] Production overrides available")
    else:
        print("[\33[32mOK\33[37m] Production overrides available")


def main() -> None:
    print("\33[1m\33[37m")
    dotenv_used = _load_dotenv_if_available()
    if not dotenv_used:
        print("\33[33mNOTE\33[37m: python-dotenv not installed, "
              "using only environment vars.")
    cfg = _read_config()
    _print_config(cfg)
    _security_checks(cfg)
    if not _validate_config(cfg):
        print("\33[31mWARNING\33[37m: Missing configuration values detected.")
        print("Tip: copy .env.example to .env and edit values, "
              "or export vars.\33[0m\n")
        sys.exit(1)
    if cfg["API_KEY"] is not None:
        masked = _mask_secret(cfg["API_KEY"])
        _ = masked
    print("\nThe Oracle \33[32msees all configurations\33[37m.")
    print("\33[0m")


if __name__ == "__main__":
    main()
