from dataclasses import dataclass
from decimal import Decimal
from typing import List

from src.data.model.Payment import Payment
from src.data.model.calculator_response import CalculatorResponse
from src.data.model.order_request import OrderItem, OrderRequest
from src.domain.model.receipt import Receipt


@dataclass
class TaxDetail:
    oid: str
    key: str
    catKey: str
    name: str
    percent: Decimal
    type: str


@dataclass
class TaxEntry:
    tax: TaxDetail
    base: Decimal
    amount: Decimal
    currency: str
    exchangeRate: int # it could be str either 

# @dataclass
# class CreateReceiptItem:
#     index: int
#     productOid: str
#     quantity: int # Evaluate if it could be int
#     netUnitPrice: Decimal
#     netPrice: Decimal
#     crossUnitPrice: Decimal
#     crossPrice: Decimal
#     currency: str
#     exchangeRate: str
#     remark: Optional[str]
#     taxes: List[TaxEntry]

# @dataclass
# class Payment:
#     type: str
#     amount: Decimal
#     mappingKey: Optional[str]
#     currency: str
#     exchangeRate: str
#     collectOrderId: Optional[str]

@dataclass
class CreateReceiptRequest:
    payments: List[Payment]
    balanceOid: str
    status: str
    workspaceOid: str
    netTotal: Decimal
    crossTotal: Decimal
    payableAmount: Decimal
    taxes: List[TaxEntry]
    items: List[OrderItem]
    contactOid: str

    @classmethod
    def from_mongo_receipt_and_calculator(cls, receipt: Receipt, calculator_response: CalculatorResponse, create_order_request: OrderRequest, workspace_oid: str, balance_oid: str) -> 'CreateReceiptRequest':

        # Lógica para transformar receipt y calculator_response en OrderRequest
        return cls(
            payments=receipt.payments,
            balanceOid=balance_oid,
            status="OPEN",
            workspaceOid=workspace_oid,
            netTotal = calculator_response.netTotal,
            crossTotal = calculator_response.crossTotal,
            payableAmount = calculator_response.payableAmount,
            taxes= calculator_response.taxes,

            contactOid = receipt.contactOid,
            items= create_order_request.items
        )