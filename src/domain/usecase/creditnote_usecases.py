import pandas as pd

from src.data.repository.creditnote_repository import CreditNoteRepository
from src.data.repository.invoice_repository import InvoiceRepository
from src.data.repository.receipt_repository import ReceiptRepository
from src.ui.theme.color import GREEN, BLUE, WHITE, GRAY, YELLOW


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

    def generate_credit_notes_yaml_from_csv_for_invoices(self, filepath: str, workspace_oid: str, balance_oid: str):
        df = pd.read_csv(filepath_or_buffer=filepath, dtype={'oid': str, 'number': str}, sep=">")
        for i, number in enumerate(df['number'], start=1):
            invoice_mmongo = self.__invoice_repository.get_invoice_by_number(number=number)
            print(f"{YELLOW}{i}- {BLUE}{number} -> {WHITE}{invoice_mmongo.number} : {invoice_mmongo.id}{GRAY}")
            invoice_remote = self.__invoice_repository.get_remote_invoice_by_id(mongo_id=invoice_mmongo.id)
            print(f"{WHITE}InvoiceRemote: {GREEN}{invoice_remote.number}{GRAY}")
            self.__creditnote_repository.generateCreditNoteYamlForInvoice(workSpaceOid=workspace_oid, body=invoice_remote, balanceOid=balance_oid)

    def generate_credit_notes_yaml_from_csv_for_receipts(self, filepath: str, workspace_oid: str, balance_oid: str):
        df = pd.read_csv(filepath_or_buffer=filepath, dtype={'oid': str, 'number': str}, sep="\t")
        # iteration_times = []
        for i, number in enumerate(df['number'].iloc[5324:], start=1):
            # start_time = time.perf_counter()
            receipt_mongo = self.__receipt_repository.get_receipt_by_number(number=number)
            print(f"{YELLOW}{i}- {BLUE}{number} -> {WHITE}{receipt_mongo.number} : {receipt_mongo.id}{GRAY}")
            receipt_remote = self.__receipt_repository.get_remote_receipt_by_id(mongo_id=receipt_mongo.id)
            print(f"{WHITE}ReceiptRemote: {GREEN}{receipt_remote.number}{GRAY}")
            self.__creditnote_repository.generateCreditNoteYamlForReceipt(workSpaceOid=workspace_oid, body=receipt_remote, balanceOid=balance_oid)

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