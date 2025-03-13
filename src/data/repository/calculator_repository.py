from pprint import pprint

import src.ui.theme.color as color
from src.data.api.calculator_api import CalculatorApi
from src.data.datasource.tests_datasource import get_calculator_request
from src.data.mapper.domain_to_data_mapper import receipt_to_calculator_request
from src.data.model.calculator_request import CalculatorRequest
from src.data.model.calculator_response import CalculatorResponse
from src.domain.model.receipt import Receipt


class CalculatorRepository:
    def __init__(self, calculator_api: CalculatorApi) -> None:
        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.__calculator_api = calculator_api


    def calculate(self, workspace_oid: str, body: CalculatorRequest) -> CalculatorResponse:
        return self.__calculator_api.calculate(workspace_oid=workspace_oid, body=body)
    
    def calculate_from_local_receipt(self, workspace_oid: str, body: Receipt) -> CalculatorResponse:
        calculator_request = receipt_to_calculator_request(receipt=body)
        # print(f"{Color.GREEN}{calculator_request}{Color.GRAY}")
        return self.__calculator_api.calculate(workspace_oid=workspace_oid, body=calculator_request)
        


    
if __name__ == "__main__":
    calculator_api_test =  CalculatorApi("http://localhost:8080")

    calculator_request_test = get_calculator_request()
    calculator_repository = CalculatorRepository(calculator_api=calculator_api_test)
    calculation = calculator_repository.calculate(workspace_oid="36937.1", body=calculator_request_test)
    
    pprint(calculation)
