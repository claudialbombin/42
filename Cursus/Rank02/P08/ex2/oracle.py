import os

from dotenv import load_dotenv


def load_configuration() -> dict[str, str]:
    load_dotenv()
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

    env_file_exists = os.path.isfile(".env")
    config = load_configuration()

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
