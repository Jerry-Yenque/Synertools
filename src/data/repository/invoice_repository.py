from src.ui.theme.color import GRAY, YELLOW
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.model.document_not_found_error import DocumentNotFoundError
from bson import ObjectId
from src.data.mapper.data_to_domain_mapper import receiptToDomain
from src.domain.model.receipt import Receipt

class InvoiceRepository:
    def __init__(self, mongo_datasource: MongoDataSource) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.mongo_datasource = mongo_datasource

    def getInvoiceById(self, id: str) -> Receipt:
        receipt = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"_id": ObjectId(id)}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Invoice with id {id} not found")
        return receiptToDomain(receipt)
    
    def getInvoiceByOid(self, oid: str) -> dict:
        receipt = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"oid": oid}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Invoice with oid {oid} not found")
        return receiptToDomain(receipt)
    
    def getInvoiceByNumber(self, number: str) -> Receipt:
        receipt = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"number": number}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Invoice with number {number} not found")
        return receiptToDomain(receipt)