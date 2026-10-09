from app.config.envs import API_KEY_ENV_VAR, get_api_key


def mask(secret: str, keep: int = 4) -> str:
    """Render a secret as its first and last characters only."""
    if len(secret) <= keep * 2:
        return "*" * len(secret)
    return f"{secret[:keep]}...{secret[-keep:]}"


def main() -> None:
    print(f"{API_KEY_ENV_VAR} loaded: {mask(get_api_key())}")


if __name__ == "__main__":
    main()
