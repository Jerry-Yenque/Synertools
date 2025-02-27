from src.ui.theme.color import GRAY, YELLOW
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.model.document_not_found_error import DocumentNotFoundError
from bson import ObjectId
from src.data.mapper.data_to_domain_mapper import invoiceToDomain
from src.domain.model.receipt import Receipt
from src.data.api.invoice_api import InvoiceApi
from src.data.model.receipt import ReceiptResponse
from pprint import pprint

class InvoiceRepository:
    def __init__(self, mongo_datasource: MongoDataSource, invoice_api: InvoiceApi) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.mongo_datasource = mongo_datasource
        self.invoice_api = invoice_api

    def getInvoiceById(self, id: str) -> Receipt:
        receipt = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"_id": ObjectId(id)}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Invoice with id {id} not found")
        return invoiceToDomain(receipt)
    
    def getInvoiceByOid(self, oid: str) -> dict:
        receipt = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"oid": oid}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Invoice with oid {oid} not found")
        return invoiceToDomain(receipt)
    
    def getInvoiceByNumber(self, number: str) -> Receipt:
        """ Return a invoice directly from mongodb """
        invoice = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"number": number}
        )
        if invoice is None:
            raise DocumentNotFoundError(f"Invoice with number {number} not found")
        return invoiceToDomain(invoice)
    
    def getRemoteInvoiceById(self, id: str) -> ReceiptResponse:
        return self.invoice_api.getInvoiceById(id=id)
    
if __name__ == "__main__":
    invoice_api =  InvoiceApi("http://localhost:8080")
    mongo_datasource = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    invoice_repository = InvoiceRepository(mongo_datasource=mongo_datasource, invoice_api=invoice_api)
    receipt = invoice_repository.getRemoteInvoiceById(id = "67b4ca12fa0f9264c10a36bc")
    # receipt = receipt_repository.getReceiptByNumber(number= "B908-00462108")

    pprint(receipt)