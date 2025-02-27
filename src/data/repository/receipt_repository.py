from src.ui.theme.color import GRAY, GREEN, YELLOW
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.model.document_not_found_error import DocumentNotFoundError
from bson import ObjectId
from src.data.mapper.data_to_domain_mapper import receiptToDomain
from src.domain.model.receipt import Receipt
from src.data.api.receipt_api import ReceiptApi
from src.data.model.receipt import ReceiptResponse
from pprint import pprint

class ReceiptRepository:
    def __init__(self, mongo_datasource: MongoDataSource, receipt_api: ReceiptApi) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.mongo_datasource = mongo_datasource
        self.receipt_api = receipt_api

    def getReceiptById(self, id: str) -> Receipt:
        """ Return a receipt directly from mongodb """
        receipt = self.mongo_datasource.get_document(
        collection_name="receipts",
        query={"_id": ObjectId(id)}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Receipt with id {id} not found")
        return receiptToDomain(receipt)
    
    def getReceiptByOid(self, oid: str) -> dict:
        """ Return a receipt directly from mongodb """
        receipt = self.mongo_datasource.get_document(
        collection_name="receipts",
        query={"oid": oid}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Receipt with oid {oid} not found")
        return receiptToDomain(receipt)
    
    def getReceiptByNumber(self, number: str) -> Receipt:
        """ Return a receipt directly from mongodb """
        receipt = self.mongo_datasource.get_document(
        collection_name="receipts",
        query={"number": number}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Receipt with number {number} not found")
        return receiptToDomain(receipt)
    
    def getRemoteReceiptById(self, id: str) -> ReceiptResponse:
        return self.receipt_api.getReceiptById(id=id)

    
     


if __name__ == "__main__":
    receipt_api =  ReceiptApi("http://localhost:8080")
    mongo_datasource = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    receipt_repository = ReceiptRepository(mongo_datasource=mongo_datasource, receipt_api=receipt_api)
    receipt = receipt_repository.getRemoteReceiptById(id = "67bdec8cdab1a70ff49de60b")
    # receipt = receipt_repository.getReceiptByNumber(number= "B908-00462108")

    pprint(receipt)