from datetime import datetime
from decimal import Decimal

import pandas as pd

import src.ui.theme.color as color
from src.data.api.calculator_api import CalculatorApi
from src.data.api.invoice_api import InvoiceApi
from src.data.api.order_api import OrderApi
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.model.calculator_response import CalculatorResponse
from src.data.model.order_request import OrderRequest
from src.data.repository.calculator_repository import CalculatorRepository
from src.data.repository.invoice_repository import InvoiceRepository
from src.data.repository.order_repository import OrderRepository
from src.domain.model.receipt import Receipt


class InvoiceUseCases:
    def __init__(
            self,
            invoice_repository: InvoiceRepository,
            calculator_repository: CalculatorRepository,
            order_repository: OrderRepository) -> None:

        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.__invoice_repository: InvoiceRepository = invoice_repository
        self.__calculator_repository: CalculatorRepository = calculator_repository
        self.__order_repository: OrderRepository = order_repository

    def generate_invoices_yaml_from_csv(self, filepath: str, workspace_oid: str, balance_oid: str):
        errors_file = "errors.csv"
        with open(errors_file, "w", encoding="utf-8") as f:
            f.write("Receipt_Number,User,Subtraction,OrderNumber\n")
        df = pd.read_csv(filepath_or_buffer=filepath, dtype={'oid': str, 'number': str}, sep="\t")
        for i, number in enumerate(df['number'], start=1): # .iloc[17677:17690]
            # We got the receipt from mongo by the given number in csv file
            invoice_mongo: Receipt = self.__invoice_repository.get_invoice_by_number(number=number)
            print(f"{color.YELLOW}{i}- {color.BLUE}{number} -> {color.WHITE}{invoice_mongo.number} : {invoice_mongo.id}{color.GRAY}")
            # We recalculate using the items in receipt_mongo and the calculator service
            calculator_response: CalculatorResponse = self.__calculator_repository.calculate_from_local_receipt(workspace_oid=workspace_oid, body=invoice_mongo)
            # We create the order request from data obtained in mongo and calculator response
            order_request = OrderRequest.from_receipt_and_calculator(receipt=invoice_mongo, calculator_response=calculator_response)
            # We request for creating the new order
            order_response = self.__order_repository.create_order(body=order_request)

            if Decimal(invoice_mongo.crossTotal) == order_response["crossTotal"]:
                print(f"{color.GREEN}CrossTotal not changed!{color.GRAY}")
            else:
                print(f"\t{color.RED}CrossTotal changed!{color.GRAY}")
                print(f"\t{color.WHITE}receiptMongo.crossTotal: {invoice_mongo.crossTotal} -> {type(invoice_mongo.crossTotal)}")
                print(f"\torderResponse.crossTotal: {order_response["crossTotal"]} -> {type(order_response["crossTotal"])}{color.GRAY}")
                print(f"\tuser: {color.RED}{invoice_mongo.user}{color.GRAY}")
                with open(errors_file, "a", encoding="utf-8") as f:
                    f.write(f"{invoice_mongo.number},{invoice_mongo.user},{Decimal(invoice_mongo.crossTotal) - order_response['crossTotal']},{order_response['number']}\n")
                    f.flush()

            # We create the CreateReceiptRequest to finally get the yaml
            self.__invoice_repository.generate_invoice(
                workspace_oid=workspace_oid,
                order_id=order_response["id"],
                invoice_mongo=invoice_mongo,
                calculator_response=calculator_response,
                create_order_request=order_request,
                balance_oid=balance_oid
            )
            print()

        end_time = datetime.now().time()

        # Imprimir la hora en formato HH:MM:SS
        print("End time:", end_time)



if __name__ == "__main__":
    invoice_api =  InvoiceApi("http://localhost:8080")
    order_api =  OrderApi("http://localhost:8080")
    calculator_api = CalculatorApi("http://localhost:8080")
    mongo_datasource = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    # invoice_repository = InvoiceRepository(mongo_datasource=mongo_datasource)
    calculator_repository_test = CalculatorRepository(calculator_api=calculator_api)
    order_repository_test = OrderRepository(order_api=order_api)
    invoice_repository_test = InvoiceRepository(mongo_datasource=mongo_datasource, invoice_api=invoice_api)

    usecase = InvoiceUseCases(
        # invoice_repository=invoice_repository,
        invoice_repository=invoice_repository_test,
        calculator_repository=calculator_repository_test,
        order_repository=order_repository_test
    )

    usecase.generate_invoices_yaml_from_csv(
        filepath = r"data\input\Invoices.csv", #r"data\input\Receipts.csv",
        workspace_oid="36937.2",
        balance_oid="67bf79057c7343444851ecb0" # oid or ObjectId, An open balance
    )