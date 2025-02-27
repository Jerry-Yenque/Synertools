
from src.ui.theme.color import GRAY, GREEN, YELLOW
import requests
from src.data.api.interceptor.auth_interceptor import Auth
from dacite import from_dict, Config
from src.data.model.receipt import ReceiptResponse
from pprint import pprint
import json
from decimal import Decimal
from dataclasses import asdict

class ReceiptApi:
    def __init__(self, host: str) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.host = host

    def getReceiptById(self, id: str) -> ReceiptResponse:
        Auth.checkAuth()

        headers = {
            'Authorization': f'Bearer {Auth.token}',  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }
        url = f"{self.host}/api/documents/receipts/{id}"
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        # print(f"{GREEN}{response.json()}{GRAY}")
        # print(f"{GREEN}{response.text}{GRAY}")
        data = json.loads(response.text, parse_float=Decimal)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=ReceiptResponse, data=data, config=config)

    
if __name__ == "__main__":
    receipt_api =  ReceiptApi("http://localhost:8080")
    receipt = receipt_api.getReceiptById("677bc4122c6c472706a022bc")
    pprint(receipt)
    # print(asdict(receipt))
    
