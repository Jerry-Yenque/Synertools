import json
from dataclasses import asdict
from decimal import Decimal
from pprint import pprint

import requests
import simplejson as simplejson
from dacite import from_dict, Config

import src.ui.theme.color as color
from src.data.api.interceptor.auth_interceptor import Auth
from src.data.model.calculator_request import CalculatorRequest, Position
from src.data.model.calculator_response import CalculatorResponse


class CalculatorApi:
    def __init__(self, host: str) -> None:
        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.host = host

    def calculate(self, workspace_oid: str, body: CalculatorRequest) -> CalculatorResponse:
        Auth.check_auth()

        headers = {
            'Authorization': f'Bearer {Auth.token}',  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            'Content-Type': 'application/json'
        }

        url = f"{self.host}/api/workspaces/{workspace_oid}/calculator"


        body_dict = asdict(body) # type: ignore
        json_data = simplejson.dumps(body_dict, use_decimal=True)

        response = requests.post(url=url, headers=headers, data=json_data)
        response.raise_for_status()

        # print(f"{GREEN}{response.json()}{GRAY}")
        # print(f"{GREEN}{response.text}{GRAY}")

        data = json.loads(response.text, parse_float=Decimal)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=CalculatorResponse, data=data, config=config)
        # return data
    
if __name__ == "__main__":
    calculator_api =  CalculatorApi("http://localhost:8080")
    position_1 = Position(quantity=1, productOid="7044.57")
    position_2 = Position(quantity=1, productOid="7044.2")

    calculator_request = CalculatorRequest(positions=[position_1, position_2])

    calculation = calculator_api.calculate(workspace_oid="36937.1", body=calculator_request)
    pprint(calculation.positions)
    