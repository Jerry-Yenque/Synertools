import json
from dataclasses import asdict
from decimal import Decimal
from pprint import pprint

import requests
import simplejson
from dacite import from_dict, Config

import src.ui.theme.color as color
from src.data.api.interceptor.auth_interceptor import Auth
from src.data.model.create_receipt_request import CreateReceiptRequest
from src.data.model.invoice import InvoiceResponse


class InvoiceApi:
    def __init__(self, host: str) -> None:
        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.host = host

    def get_invoice_by_id(self, mongo_id: str) -> InvoiceResponse:
        Auth.check_auth()

        headers = {
            'Authorization': f'Bearer {Auth.token}',  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }
        url = f"{self.host}/api/documents/invoices/{mongo_id}"
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        # print(f"{GREEN}{response.json()}{GRAY}")
        # print(f"{GREEN}{response.text}{GRAY}")
        data = json.loads(response.text, parse_float=Decimal)
        # print(data)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=InvoiceResponse, data=data, config=config)

    def generate_invoice(self, workspace_oid: str, order_id: str, body: CreateReceiptRequest) -> None:
        """ Order must be with status 'OPEN', we are using CreateReceiptRequest because the body request is the same """
        Auth.check_auth()

        header = {
        'Authorization' : f'Bearer {Auth.token}',
        'Content-Type': 'application/json'
        }
        url = f'{self.host}/api/workspaces/{workspace_oid}/documents/invoices?orderId={order_id}'

        body_dict = asdict(body) # type: ignore
        json_data = simplejson.dumps(body_dict, use_decimal=True)

        response = requests.post(url=url, headers=header, data=json_data)
        if response.status_code == 200:
            print(f"{color.GREEN}Success: Invoice created (200). {response.json()["number"]}{color.GRAY}")
        else:
            print(f"{color.RED}Failure: Invoice not created ({response.status_code}). {response.json()["message"]}{color.GRAY}")
            response.raise_for_status()
    
if __name__ == "__main__":
    invoice_api =  InvoiceApi("http://localhost:8080")
    invoice = invoice_api.get_invoice_by_id("67b4ca12fa0f9264c10a36bc")
    pprint(invoice)