from decimal import Decimal
from pprint import pprint
from typing import cast

from bson import ObjectId
from dacite import Config, from_dict
from dacite.data import Data

from src.data.api.invoice_api import InvoiceApi
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.model.document_not_found_error import DocumentNotFoundError
from src.data.model.invoice import InvoiceResponse
from src.domain.model.receipt import Receipt
from src.ui.theme.color import GRAY, YELLOW


class InvoiceRepository:
    def __init__(self, mongo_datasource: MongoDataSource, invoice_api: InvoiceApi) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.mongo_datasource = mongo_datasource
        self.invoice_api = invoice_api

    def get_invoice_by_id(self, mongo_id: str) -> Receipt:
        """ we are recycling and returning Receipt because it shares the same info we need for Invoice """
        invoice = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"_id": ObjectId(mongo_id)}
        )
        if invoice is None:
            raise DocumentNotFoundError(f"Invoice with id {mongo_id} not found")

        if "_id" in invoice:
            invoice["id"] = str(invoice.pop("_id"))
        invoice_data = cast(Data, invoice)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=Receipt, data=invoice_data, config=config)
    
    def get_invoice_by_oid(self, oid: str) -> Receipt:
        """ we are recycling and returning Receipt because it shares the same info we need for Invoice  """
        invoice = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"oid": oid}
        )
        if invoice is None:
            raise DocumentNotFoundError(f"Invoice with oid {oid} not found")

        if "_id" in invoice:
            invoice["id"] = str(invoice.pop("_id"))
        invoice_data = cast(Data, invoice)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=Receipt, data=invoice_data, config=config)
    
    def get_invoice_by_number(self, number: str) -> Receipt:
        """ Return an invoice directly from mongodb, we are recycling and returning Receipt because it shares the same info we need for Invoice """
        invoice = self.mongo_datasource.get_document(
        collection_name="invoices",
        query={"number": number}
        )
        if invoice is None:
            raise DocumentNotFoundError(f"Invoice with number {number} not found")

        if "_id" in invoice:
            invoice["id"] = str(invoice.pop("_id"))
        invoice_data = cast(Data, invoice)
        config = Config(type_hooks={Decimal: Decimal})
        return from_dict(data_class=Receipt, data=invoice_data, config=config)
    
    def get_remote_invoice_by_id(self, mongo_id: str) -> InvoiceResponse:
        return self.invoice_api.get_invoice_by_id(mongo_id=mongo_id)
    
if __name__ == "__main__":
    invoice_api_test =  InvoiceApi("http://localhost:8080")
    mongo_datasource_test = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    invoice_repository = InvoiceRepository(mongo_datasource=mongo_datasource_test, invoice_api=invoice_api_test)

#=========== get_remote_invoice_by_id test =============================================================
    # receipt_test = invoice_repository.get_remote_invoice_by_id(mongo_id = "67b4ca12fa0f9264c10a36bc")

#=========== get_remote_invoice_by_id test =============================================================
    # receipt_test = invoice_repository.get_invoice_by_oid(oid = "14206.3031594")

#=========== get_invoice_by_id test =============================================================
    receipt_test = invoice_repository.get_invoice_by_id(mongo_id="67b4ca12fa0f9264c10a36bc")

    pprint(receipt_test)