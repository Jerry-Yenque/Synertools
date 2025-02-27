from src.ui.theme.color import GRAY, GREEN, BLUE, WHITE, GRAY, YELLOW
import pandas as pd
from src.data.repository.invoice_repository import InvoiceRepository
from src.data.repository.receipt_repository import ReceiptRepository
from src.data.datasource.mongo_datasource import MongoDataSource
from src.data.api.receipt_api import ReceiptApi
from src.data.api.yaml_generator_api import YamlGeneratorApi
from src.data.repository.creditnote_repository import CreditNoteRepository
import time

class CreditNoteUseCases:
    def __init__(
            self, 
            invoice_repository: InvoiceRepository, 
            receipt_repository: ReceiptRepository,
            creditnote_repository: CreditNoteRepository) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.__invoice_repository = invoice_repository
        self.__receipt_repository = receipt_repository
        self.__creditnote_repository = creditnote_repository

    def generateCreditNotesYamlFromCsvForInvoices(self, filepath: str, workSpaceOid: str, balanceOid: str):
        df = pd.read_csv(filepath_or_buffer=filepath, dtype={'oid': str, 'number': str}, sep=">")
        for i, number in enumerate(df['number'], start=1):
            invoiceMongo = self.__invoice_repository.getInvoiceByNumber(number=number)
            print(f"{YELLOW}{i}- {BLUE}{number} -> {WHITE}{invoiceMongo.number} : {invoiceMongo.id}{GRAY}")
            invoiceRemote = self.__invoice_repository.getRemoteInvoiceById(id=invoiceMongo.id)
            print(f"{WHITE}InvoiceRemote: {GREEN}{invoiceRemote.number}{GRAY}")
            self.__creditnote_repository.generateCreditNoteYamlForInvoice(workSpaceOid=workSpaceOid, body=invoiceRemote, balanceOid=balanceOid)

    def generateCreditNotesYamlFromCsvForReceipts(self, filepath: str, workSpaceOid: str, balanceOid: str):
        df = pd.read_csv(filepath_or_buffer=filepath, dtype={'oid': str, 'number': str}, sep="\t")
        # iteration_times = []
        for i, number in enumerate(df['number'].iloc[5324:], start=1):
            # start_time = time.perf_counter()
            receiptMongo = self.__receipt_repository.getReceiptByNumber(number=number)
            print(f"{YELLOW}{i}- {BLUE}{number} -> {WHITE}{receiptMongo.number} : {receiptMongo.id}{GRAY}")
            receiptRemote = self.__receipt_repository.getRemoteReceiptById(id=receiptMongo.id)
            print(f"{WHITE}ReceiptRemote: {GREEN}{receiptRemote.number}{GRAY}")
            self.__creditnote_repository.generateCreditNoteYamlForReceipt(workSpaceOid=workSpaceOid, body=receiptRemote, balanceOid=balanceOid)

            # end_time = time.perf_counter()  # Finaliza el temporizador
            # elapsed_time = end_time - start_time  # Tiempo de la iteración
            # iteration_times.append(elapsed_time) 

        # average_time = sum(iteration_times) / len(iteration_times)  # Promedio
        # max_time = max(iteration_times)
        # min_time = min(iteration_times)

        # print(f"\nMétricas de ejecución:")
        # print(f"Tiempo promedio por iteración: {average_time:.4f} segundos")
        # print(f"Tiempo máximo en una iteración: {max_time:.4f} segundos")
        # print(f"Tiempo mínimo en una iteración: {min_time:.4f} segundos")

    def hello(self):
        print(f"{GREEN}{self.__class__.__name__} Hello.{GRAY}")
            


if __name__ == "__main__":
    pass
    # receipt_api =  ReceiptApi("http://localhost:8080")
    # yaml_generator_api = YamlGeneratorApi("http://localhost:8080")
    # mongo_datasource = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    # invoice_repository = InvoiceRepository(mongo_datasource=mongo_datasource)
    # creditnote_repository = CreditNoteRepository(yaml_generator_api=yaml_generator_api)
    # receipt_repository = ReceiptRepository(mongo_datasource=mongo_datasource, receipt_api=receipt_api)

    # usecase = CreditNoteUseCases(
    #     invoice_repository=invoice_repository, 
    #     receipt_repository=receipt_repository,
    #     creditnote_repository=creditnote_repository
    #     )
    # usecase.generateCreditNotesYamlFromCsvForReceipts()