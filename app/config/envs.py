import os

from dotenv import load_dotenv

load_dotenv()

API_KEY_ENV_VAR = "ANTHROPIC_API_KEY"


def get_api_key() -> str:
    """Return the Anthropic API key.

    Raises:
        RuntimeError: if the key is not set in the environment or in .env.
    """
    api_key = os.getenv(API_KEY_ENV_VAR)
    if not api_key:
        raise RuntimeError(f"{API_KEY_ENV_VAR} is not set. Run 'make env' and fill in .env.")
    return api_key
