from src.data.api.receipt_api import ReceiptApi
from src.data.api.yaml_generator_api import YamlGeneratorApi
from src.data.api.invoice_api import InvoiceApi
from src.data.datasource.mongo_datasource import MongoDataSource
from src.domain.usecase.creditnote_usecases import CreditNoteUseCases
from src.data.repository.invoice_repository import InvoiceRepository
from src.data.repository.receipt_repository import ReceiptRepository
from src.data.repository.creditnote_repository import CreditNoteRepository
from dotenv import load_dotenv
import os

class AppContainer:
    _instance = None # This is a static variable (class variable)

    def __init__(self) -> None:
        load_dotenv("local.env", override=-True)
        self.host_local = os.getenv("HOST_LOCAL")

    def __new__(cls):
        """ It is responsible for creating an instance of the class. This custom __new__ uses singleton """
        """ The cls parameter is a Python convention for referring to the class and is analogous to self used for instances. """
    
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_dependencies()
        return cls._instance
    
    # def _initialize_dependencies(self):
    #     """ Here you initialize all the necessary dependencies. """
    #     self.receiptApiService = ReceiptApi()

    
    # ========= THIS IS AN EXAMPLE OF LAZY INIT ===============
    def _initialize_dependencies(self):
        # Inicialmente no se crea la instancia, se marca como None.
        self.yaml_generator_api_service = None
        self._receipt_api_service = None
        self._mongo_datasource = None
        self.creditnote_usecases = None
        self.receipt_repository = None
        self.invoice_repository = None
        self.creditnote_repository = None
        self.invoice_api_service = None

    @property
    def invoiceApiService(self):
        if self.invoice_api_service is None:
            self.invoice_api_service = InvoiceApi(host=self.host_local)
        return self.invoice_api_service
    
    @property
    def yamlGeneratorApiService(self):
        if self.yaml_generator_api_service is None:
            self.yaml_generator_api_service = YamlGeneratorApi(host=self.host_local)
        return self.yaml_generator_api_service
    
    @property
    def creditNoteRepository(self):
        if self.creditnote_repository is None:
            self.creditnote_repository = CreditNoteRepository(yaml_generator_api=self.yamlGeneratorApiService)
        return self.creditnote_repository
    
    @property
    def invoiceRepository(self):
        if self.invoice_repository is None:
            self.invoice_repository = InvoiceRepository(mongo_datasource=self.mongoDataSource, invoice_api=self.invoiceApiService)
        return self.invoice_repository
    
    @property
    def receiptRepository(self):
        if self.receipt_repository is None:
            self.receipt_repository = ReceiptRepository(mongo_datasource=self.mongoDataSource, receipt_api=self.receiptApiService)
        return self.receipt_repository

    @property
    def creditNoteUseCases(self):
        if self.creditnote_usecases is None:
            self.creditnote_usecases = CreditNoteUseCases(
                invoice_repository=self.invoiceRepository, 
                receipt_repository=self.receiptRepository,
                creditnote_repository=self.creditNoteRepository
                )
        return self.creditnote_usecases

    @property
    def receiptApiService(self):
        if self._receipt_api_service is None:
            self._receipt_api_service = ReceiptApi(host=self.host_local)
        return self._receipt_api_service
    
    @property
    def mongoDataSource(self):
        if self._mongo_datasource is None:
            self._mongo_datasource = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
        return self._mongo_datasource
    # ========= END EXAMPLE OF LAZY INIT ===============