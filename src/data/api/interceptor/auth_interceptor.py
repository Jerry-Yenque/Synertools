import os

import requests
from dotenv import load_dotenv

from src.ui.theme.color import GREEN, GRAY, YELLOW, BLUE, WHITE


class Auth:
    """ Test me  python -m data.api.interceptor.Auth """
    token: str = ""
    refresh_token: str = ""

    @staticmethod
    def authenticate() -> None:
        print(f"\t{YELLOW}Authenticating...{GRAY}")
        load_dotenv("local.env", override=-True)
        body = {
            "userName": os.getenv("USER_LOCAL"),
            "password": os.getenv("PASSWORD_LOCAL")
        }

        print(f"\t{BLUE}user: {WHITE}{os.getenv("USER_LOCAL")}, {BLUE}password: {WHITE}{os.getenv("PASSWORD_LOCAL")}")

        header = {
            "Content-Type": "application/json"
        }

        response = requests.post(f'{os.getenv("HOST_LOCAL")}/api/authenticate', json=body, headers=header)
        # Processing response
        if response.status_code == 200:
            Auth.token = response.json()["accessToken"]
            Auth.refresh_token = response.json()["refreshToken"]
            print(f'\t{YELLOW}Auth Successful.{GRAY}')
        else:
            print("Error:", response.status_code)
            print("Response:", response.text)

    @staticmethod
    def test() -> None:
        load_dotenv("cloud.env", override=True)
        print("in test", os.getenv("USER_CLOUD"))

    @staticmethod
    def check_auth() -> None:
        if Auth.token == "":
            Auth.authenticate()

if __name__ == "__main__":
    print(f"'{Auth.token}'")
    Auth.authenticate()
    print(f"{GREEN}'{Auth.token}'{GRAY}")
    Auth.test()
    