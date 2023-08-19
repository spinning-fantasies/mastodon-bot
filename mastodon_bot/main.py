import os

from dotenv import load_dotenv
from mastodon import Mastodon

load_dotenv()

def register_app() -> None:
    Mastodon.create_app(
        "mastodon_bot",
        api_base_url="https://3615.computer/",
        to_file="mastodon_bot_clientcred.secret",
    )

def main() -> None:
    password = os.getenv("MASTODON_PASSWORD")
    if not password:
        raise ValueError("Password is required")
    
    print(password)
    register_app()

if __name__ == "__main__":
    main()
