import json
from decimal import Decimal
from pprint import pprint

import requests
from dacite import from_dict, Config

import src.ui.theme.color as color
from src.data.api.interceptor.auth_interceptor import Auth
from src.data.model.invoice import InvoiceResponse


class InvoiceApi:
    def __init__(self, host: str) -> None:
        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.host = host

    def getInvoiceById(self, id: str) -> InvoiceResponse:
        Auth.checkAuth()

        headers = {
            'Authorization': f'Bearer {Auth.token}',  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }
        url = f"{self.host}/api/documents/invoices/{id}"
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        # print(f"{GREEN}{response.json()}{GRAY}")
        # print(f"{GREEN}{response.text}{GRAY}")
        data = json.loads(response.text, parse_float=Decimal)
        # print(data)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=InvoiceResponse, data=data, config=config)
    
if __name__ == "__main__":
    invoice_api =  InvoiceApi("http://localhost:8080")
    invoice = invoice_api.getInvoiceById("67b4ca12fa0f9264c10a36bc")
    pprint(invoice)