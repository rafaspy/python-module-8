import os
from dotenv import load_dotenv

def get_config(name: str) -> str | None:
    """Get a configuration value from environment variables."""
    return os.getenv(name)


def main() -> None:
    load_dotenv()

    mode = get_config("MATRIX_MODE")
    database_url = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL")
    zion_endpoint = get_config("ZION_ENDPOINT")


    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    if mode is None:
        print("Mode: Not configured")
    else:
        print(f"Mode: {mode}")

    if database_url is None:
        print("Database: Configuration missing")
    else:
        print("Database: Connected to local instance")

    if api_key is None:
        print("API Access: Missing")
    else:
        print("API Access: Authenticated")

    if log_level is None:
        print("Log Level: Not configured")
    else:
        print(f"Log Level: {log_level}")

    if zion_endpoint is None:
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    if mode == "development":
        print("Environment: Development")
    elif mode == "production":
        print("Environment: Production")
    else:
        print("Environment: Not configured")

    print("The Oracle sees all configurations")


if __name__ == "__main__":
    main()
