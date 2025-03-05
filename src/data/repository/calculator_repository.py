import src.ui.theme.color as Color
from src.data.api.calculator_api import CalculatorApi
from src.data.model.calculator_response import CalculatorResponse
from pprint import pprint

class CalculatorRepository:
    def __init__(self, calculator_api: CalculatorApi) -> None:
        print(f"{Color.YELLOW}{self.__class__.__name__} Init.{Color.GRAY}")
        self.calculator_api = calculator_api

    def hello(self) -> None:
        print(f"{Color.BLUE}Hellow{Color.GRAY}")

    def calculate(self, workSpaceOid: str, body: dict) -> CalculatorResponse:
        return self.calculator_api.calculate(workSpaceOid=workSpaceOid, body=body)

    
if __name__ == "__main__":
    calculator_api =  CalculatorApi("http://localhost:8080")
    calculator_repository = CalculatorRepository(calculator_api=calculator_api)
    calculation = calculator_repository.calculate(workSpaceOid="36937.1", body={
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
    
    pprint(calculation)
