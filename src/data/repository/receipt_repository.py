from decimal import Decimal
from typing import cast

from bson import ObjectId
from dacite import from_dict, Config
from dacite.data import Data

from src.data.api.receipt_api import ReceiptApi
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.model.calculator_response import CalculatorResponse
from src.data.model.create_receipt_request import CreateReceiptRequest
from src.data.model.document_not_found_error import DocumentNotFoundError
from src.data.model.order_request import OrderRequest
from src.data.model.receipt_response import ReceiptResponse
from src.domain.model.receipt import Receipt
from src.ui.theme.color import GRAY, YELLOW


class ReceiptRepository:
    def __init__(self, mongo_datasource: MongoDataSource, receipt_api: ReceiptApi) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.mongo_datasource = mongo_datasource
        self.receipt_api = receipt_api

    def get_receipt_by_id(self, mongo_id: str) -> None:
        """ Return a receipt directly from mongodb """
        receipt = self.mongo_datasource.get_document(
        collection_name="receipts",
        query={"_id": ObjectId(mongo_id)}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Receipt with id {mongo_id} not found")
        # return receiptToDomain(receipt) # DEPRECATED
    
    def get_receipt_by_oid(self, oid: str) -> None:
        """ Return a receipt directly from mongodb """
        receipt = self.mongo_datasource.get_document(
        collection_name="receipts",
        query={"oid": oid}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Receipt with oid {oid} not found")
        # return receiptToDomain(receipt) # DEPRECATED
    
    def get_receipt_by_number(self, number: str) -> Receipt:
        """ Return a receipt directly from mongodb """
        receipt = self.mongo_datasource.get_document(
        collection_name="receipts",
        query={"number": number}
        )
        if receipt is None:
            raise DocumentNotFoundError(f"Receipt with number {number} not found")
        # return receiptToDomain(receipt)

        if "_id" in receipt:
            receipt["id"] = str(receipt.pop("_id"))
        receipt_data = cast(Data, receipt)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=Receipt, data=receipt_data, config=config)

    def get_remote_receipt_by_id(self, mongo_id: str) -> ReceiptResponse:
        return self.receipt_api.get_receipt_by_id(receipt_id=mongo_id)
    
    def generate_receipt(self,
                         workspace_oid: str,
                         order_id: str,
                         receipt_mongo: Receipt,
                         calculator_response: CalculatorResponse,
                         create_order_request: OrderRequest,
                         balance_oid: str) -> None:

        create_receipt_request = CreateReceiptRequest.from_mongo_receipt_and_calculator(receipt=receipt_mongo, calculator_response=calculator_response, create_order_request=create_order_request, workspace_oid=workspace_oid, balance_oid=balance_oid)
        self.receipt_api.generate_receipt(workspace_oid=workspace_oid, order_id=order_id, body=create_receipt_request)
        

    
     


if __name__ == "__main__":
    receipt_api_test =  ReceiptApi("http://localhost:8080")
    mongo_datasource_test = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    receipt_repository = ReceiptRepository(mongo_datasource=mongo_datasource_test, receipt_api=receipt_api_test)

    # =========== get_receipt_by_number test ======================================

    receipt_mongo_test = receipt_repository.get_receipt_by_number(number= "B908-00462092")
    print(receipt_mongo_test)

# =========== generate_receipt test ======================================
#     receipt_request = get_create_receipt_request()
#     receipt_repository.generate_receipt(workspace_oid="36937.12", order_id="67d08df49a527e255819c153", body=receipt_request)