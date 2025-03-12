from src.ui.theme.color import GRAY, GREEN, RED, YELLOW
from src.data.api.yaml_generator_api import YamlGeneratorApi
from src.data.model.receipt_response import ReceiptResponse
from src.data.model.invoice import InvoiceResponse
from src.data.model.creditnote_receipt_request import CreditNoteForReceiptRequest
from src.data.model.creditnote_invoice_request import CreditNoteForInvoiceRequest

class CreditNoteRepository:
    def __init__(self, yaml_generator_api: YamlGeneratorApi) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.yaml_generator_api = yaml_generator_api
    
    def generateCreditNoteYamlForReceipt(self, workSpaceOid: str, body: ReceiptResponse, balanceOid: str):
        creditNoteRequest = CreditNoteForReceiptRequest.from_receipt(receipt=body, balanceOid=balanceOid)
        self.yaml_generator_api.generateCreditNoteYaml(workSpaceOid=workSpaceOid, body=creditNoteRequest)

    def generateCreditNoteYamlForInvoice(self, workSpaceOid: str, body: InvoiceResponse, balanceOid: str):
        creditNoteRequest = CreditNoteForInvoiceRequest.from_invoice(invoice=body, balanceOid=balanceOid)
        self.yaml_generator_api.generateCreditNoteYaml(workSpaceOid=workSpaceOid, body=creditNoteRequest)