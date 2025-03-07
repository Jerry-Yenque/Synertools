import src.ui.theme.color as Color
from src.data.api.calculator_api import CalculatorApi
from src.data.model.calculator_response import CalculatorResponse
from pprint import pprint
from src.domain.model.receipt import Receipt
from src.data.mapper.domain_to_data_mapper import receipt_to_calculator_request
from src.data.model.calculator_request import CalculatorRequest, Position

class CalculatorRepository:
    def __init__(self, calculator_api: CalculatorApi) -> None:
        print(f"{Color.YELLOW}{self.__class__.__name__} Init.{Color.GRAY}")
        self.__calculator_api = calculator_api

    def hello(self) -> None:
        print(f"{Color.BLUE}Hellow{Color.GRAY}")

    def calculate(self, workSpaceOid: str, body: dict) -> CalculatorResponse:
        return self.__calculator_api.calculate(workSpaceOid=workSpaceOid, body=body)
    
    def calculate_from_local_receipt(self, workSpaceOid: str, body: Receipt) -> CalculatorResponse:
        calculator_request = receipt_to_calculator_request(receipt=body)
        # print(f"{Color.GREEN}{calculator_request}{Color.GRAY}")
        return self.__calculator_api.calculate(workSpaceOid=workSpaceOid, body=calculator_request)
        


    
if __name__ == "__main__":
    calculator_api =  CalculatorApi("http://localhost:8080")
    position_1 = Position(quantity=1, productOid="7044.57")
    position_2 = Position(quantity=1, productOid="7044.2")

    calculator_request = CalculatorRequest(positions=[position_1, position_2])
    calculator_repository = CalculatorRepository(calculator_api=calculator_api)
    calculation = calculator_repository.calculate(workSpaceOid="36937.1", body=calculator_request)
    
    pprint(calculation)
