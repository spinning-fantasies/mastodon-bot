import os

from dotenv import load_dotenv
from mastodon import Mastodon

load_dotenv()

def register_app() -> None:
    # Create an instance of the Mastodon class
    mastodon = Mastodon(
        access_token=os.getenv("MASTODON_ACCESS_TOKEN"),
        api_base_url='https://3615.computer'
    )

    # Post a new status update
    mastodon.status_post('Hello, Mastodon!')


def main() -> None:
    password = os.getenv("MASTODON_PASSWORD")
    if not password:
        raise ValueError("Password is required")
    
    register_app()

if __name__ == "__main__":
    main()
