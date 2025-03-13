
import json
from dataclasses import asdict
from decimal import Decimal

import requests
import simplejson as simplejson
from dacite import from_dict, Config

import src.ui.theme.color as color
from src.data.api.interceptor.auth_interceptor import Auth
# from src.data.datasource.tests_datasource import get_create_receipt_request
from src.data.model.create_receipt_request import CreateReceiptRequest
from src.data.model.receipt_response import ReceiptResponse


class ReceiptApi:
    def __init__(self, host: str) -> None:
        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.host = host

    def get_receipt_by_id(self, receipt_id: str) -> ReceiptResponse:
        Auth.check_auth()

        headers = {
            'Authorization': f'Bearer {Auth.token}',  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }
        url = f"{self.host}/api/documents/receipts/{receipt_id}"
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        # print(f"{GREEN}{response.json()}{GRAY}")
        # print(f"{GREEN}{response.text}{GRAY}")
        data = json.loads(response.text, parse_float=Decimal)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=ReceiptResponse, data=data, config=config)
    
    def generate_receipt(self, workspace_oid: str, order_id: str, body: CreateReceiptRequest) -> None:
        """ Order must be with status 'OPEN' """
        Auth.check_auth()

        header = {
            'Authorization' : f'Bearer {Auth.token}',
            'Content-Type': 'application/json'
        }
        url = f'{self.host}/api/workspaces/{workspace_oid}/documents/receipts?orderId={order_id}'

        body_dict = asdict(body) # type: ignore
        json_data = simplejson.dumps(body_dict, use_decimal=True)

        response = requests.post(url=url, headers=header, data=json_data)
        if response.status_code == 200:
            print(f"{color.GREEN}Success: Receipt created (200). {response.json()["number"]}{color.GRAY}")
        else:
            print(f"{color.RED}Failure: Receipt not created ({response.status_code}). {response.json()["message"]}{color.GRAY}")
        response.raise_for_status()

    
if __name__ == "__main__":
    receipt_api =  ReceiptApi("http://localhost:8080")
    # receipt = receipt_api.get_receipt_by_id("677bc4122c6c472706a022bc")
    # pprint(receipt)
    # print(asdict(receipt))

    
    #=============== generateReceipt test ===============================00
    # receipt_request = get_create_receipt_request()
    # receipt_api.generate_receipt(workspace_oid="36937.12", order_id="67d08df49a527e255819c153", body=receipt_request)
    # pprint(receipt_request)

