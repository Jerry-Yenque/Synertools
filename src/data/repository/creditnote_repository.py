from src.ui.theme.color import GRAY, GREEN, RED, YELLOW
from src.data.api.yaml_generator_api import YamlGeneratorApi
from src.data.model.receipt import ReceiptResponse
from src.data.model.creditnote_request import CreditNoteRequest

class CreditNoteRepository:
    def __init__(self, yaml_generator_api: YamlGeneratorApi) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.yaml_generator_api = yaml_generator_api
    
    def generateCreditNoteYaml(self, workSpaceOid: str, body: ReceiptResponse, balanceOid: str):
        creditNoteRequest = CreditNoteRequest.from_receipt(receipt=body, balanceOid=balanceOid)
        self.yaml_generator_api.generateCreditNoteYaml(workSpaceOid=workSpaceOid, body=creditNoteRequest)
        # if response.status_code == 200:
        #     print(f"{GREEN}CreditNoteRepository: Credit note done!{GRAY}")
        # else:
        #     print(f"{RED}CreditNoteRepository: Something happens!{GRAY}")