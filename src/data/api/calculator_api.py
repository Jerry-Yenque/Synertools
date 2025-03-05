import src.ui.theme.color as color
import requests
from src.data.api.interceptor.auth_interceptor import Auth
from dacite import from_dict, Config
from src.data.model.calculator_response import CalculatorResponse
from pprint import pprint
import json
from decimal import Decimal

class CalculatorApi:
    def __init__(self, host: str) -> None:
        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.host = host

    def calculate(self, workSpaceOid: str, body: dict) -> CalculatorResponse:
        Auth.checkAuth()

        headers = {
            'Authorization': f'Bearer {Auth.token}',  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }

        url = f"{self.host}/api/workspaces/{workSpaceOid}/calculator"
        response = requests.post(url=url, headers=headers, json=body)
        response.raise_for_status()

        # print(f"{GREEN}{response.json()}{GRAY}")
        # print(f"{GREEN}{response.text}{GRAY}")

        data = json.loads(response.text, parse_float=Decimal)
        # config = Config(type_hooks={Decimal: Decimal})
        # return from_dict(data_class=CalculatorResponse, data=data, config=config)
        return data
    
if __name__ == "__main__":
    calculator_api =  CalculatorApi("http://localhost:8080")
    calculation = calculator_api.calculate(workSpaceOid="36937.1", body={
  "positions": [
    {
      "quantity": 1,
      "productOid": "7044.35"
    },
    {
      "quantity": 1,
      "productOid": "7044.117"
    },
    {
      "quantity": 1,
      "productOid": "7044.54"
    }
  ]
})
    pprint(calculation["positions"][0])
    