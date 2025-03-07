import src.ui.theme.color as Color
import pandas as pd
from src.data.repository.invoice_repository import InvoiceRepository
from src.data.repository.receipt_repository import ReceiptRepository
from src.data.repository.order_repository import OrderRepository
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.api.receipt_api import ReceiptApi
from src.data.api.calculator_api import CalculatorApi
from src.data.api.order_api import OrderApi
from src.data.repository.calculator_repository import CalculatorRepository
from src.data.repository.order_repository import OrderRepository
from src.domain.model.receipt import Receipt
from pprint import pprint
from src.data.model.order_request import OrderRequest
from decimal import Decimal
import pandas as pd

class ReceiptUseCases:
    def __init__(
            self,
            # invoice_repository: InvoiceRepository, 
            receipt_repository: ReceiptRepository,
            calculator_repository: CalculatorRepository,
            order_repository: OrderRepository) -> None:
        
        print(f"{Color.YELLOW}{self.__class__.__name__} Init.{Color.GRAY}")
        # self.__invoice_repository = invoice_repository
        self.__receipt_repository: ReceiptRepository = receipt_repository
        self.__calculator_repository: CalculatorRepository = calculator_repository
        self.__order_repository: OrderRepository = order_repository

    def generateReceiptsYamlFromCsv(self, filepath: str, workSpaceOid: str, balanceOid: str):
        errors_file = "errors.csv"

        # Escribir encabezados antes de procesar los datos
        with open(errors_file, "w", encoding="utf-8") as f:
            f.write("Receipt_Number,User,Subtraction\n")
        # errors = []
        df = pd.read_csv(filepath_or_buffer=filepath, dtype={'oid': str, 'number': str}, sep="\t")
        for i, number in enumerate(df['number'], start=1): # .iloc[17677:17690]
            receiptMongo: Receipt = self.__receipt_repository.getReceiptByNumber(number=number)
            print(f"{Color.YELLOW}{i}- {Color.BLUE}{number} -> {Color.WHITE}{receiptMongo.number} : {receiptMongo.id}{Color.GRAY}")
            calculator_response = self.__calculator_repository.calculate_from_local_receipt(workSpaceOid=workSpaceOid, body=receiptMongo)
            order_request = OrderRequest.from_receipt_and_calculator(receipt=receiptMongo, calculator_response=calculator_response)
            order_response = self.__order_repository.createOrder(body=order_request)
            if (Decimal(receiptMongo.crossTotal) == order_response["crossTotal"]): 
                print(f"{Color.GREEN}CrossTotal not changed!{Color.GRAY}")
            else:
                print(f"\t{Color.RED}crossTotal changed{Color.GRAY}")
                print(f"\t{Color.WHITE}receiptMongo.crossTotal: {receiptMongo.crossTotal} -> {type(receiptMongo.crossTotal)}")
                print(f"\torderResponse.crossTotal: {order_response["crossTotal"]} -> {type(order_response["crossTotal"])}{Color.GRAY}")
                print(f"\tuser: {Color.RED}{receiptMongo.user}{Color.GRAY}")
                # errors.append([receiptMongo.number, receiptMongo.user, Decimal(receiptMongo.crossTotal)-order_response["crossTotal"]])
                with open(errors_file, "a", encoding="utf-8") as f:
                    f.write(f"{receiptMongo.number},{receiptMongo.user},{Decimal(receiptMongo.crossTotal) - order_response['crossTotal']}\n")
                    f.flush()  # Forzar la escritura inmediata
            print()

        # df_errors = pd.DataFrame(errors, columns=["Receipt_Number", "User", "Subtraction"])
        # df_errors.to_csv("errors.csv", index=False, encoding="utf-8")




if __name__ == "__main__":
    receipt_api =  ReceiptApi("http://localhost:8080")
    order_api =  OrderApi("http://localhost:8080")
    calculator_api = CalculatorApi("http://localhost:8080")
    mongo_datasource = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    # invoice_repository = InvoiceRepository(mongo_datasource=mongo_datasource)
    calculator_repository = CalculatorRepository(calculator_api=calculator_api)
    order_repository = OrderRepository(order_api=order_api)
    receipt_repository = ReceiptRepository(mongo_datasource=mongo_datasource, receipt_api=receipt_api)

    usecase = ReceiptUseCases(
        # invoice_repository=invoice_repository, 
        receipt_repository=receipt_repository,
        calculator_repository=calculator_repository,
        order_repository=order_repository
        )
    
    usecase.generateReceiptsYamlFromCsv(
        filepath = r"data\input\Receipts.csv",
        workSpaceOid="36937.1",
        balanceOid="67bf79057c7343444851ecb0" # oid or ObjectId, An open balance
        )