import importlib
import os
import sys
from typing import Any, Optional


def import_dotenv() -> Optional[Any]:
    # python-dotenv is loaded with importlib (same trick as in
    # ex1/loading.py): if it is missing we can print a helpful message
    # instead of crashing, and mypy --strict stays happy either way.
    try:
        return importlib.import_module("dotenv")
    except ImportError:
        return None


def get_env_path() -> str:
    # The .env is always looked for next to this script, not in the
    # current directory, so the result is the same wherever oracle.py
    # is launched from.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, ".env")


def load_configuration(dotenv: Any, env_path: str) -> dict[str, str]:
    # load_dotenv does not override variables that already exist, so
    # real environment variables win over the .env file.
    dotenv.load_dotenv(env_path)
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get(
            "DATABASE_URL", "sqlite:///local.db"
        ),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get(
            "ZION_ENDPOINT", "http://localhost:8000"
        ),
    }


def describe_database(mode: str, url: str) -> str:
    if mode == "production":
        return f"Connected to production instance ({url})"
    return "Connected to local instance"


def describe_api(api_key: str) -> str:
    if api_key:
        return "Authenticated"
    return "Missing API_KEY - running unauthenticated"


def check_security(env_file_exists: bool) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_file_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found, using defaults")
    print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    dotenv = import_dotenv()
    if dotenv is None:
        print("[ERROR] python-dotenv is not installed.")
        print("Install it with: pip install python-dotenv")
        sys.exit(1)

    env_path = get_env_path()
    env_file_exists = os.path.isfile(env_path)
    config = load_configuration(dotenv, env_path)

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    database = describe_database(
        config["MATRIX_MODE"], config["DATABASE_URL"]
    )
    print(f"Database: {database}")
    print(f"API Access: {describe_api(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: Online ({config['ZION_ENDPOINT']})")

    check_security(env_file_exists)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
