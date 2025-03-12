from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, List

from src.data.model.receipt_response import Item, TaxEntry, EmployeeRelation, Payment, Contact


@dataclass
class InvoiceResponse:
    oid: Optional[str]
    id: str
    number: str
    items: List[Item]
    status: str
    date: str
    currency: str
    netTotal: Decimal
    crossTotal: Decimal
    exchangeRate: int
    payableAmount: Decimal
    taxes: List[TaxEntry]
    contactOid: str
    workspaceOid: str
    note: Optional[str]
    employeeRelations: List[EmployeeRelation]
    balanceOid: str
    payments: List[Payment]
    discount: Optional[Decimal]
    contact: Contact
    invoiceItems: List[Item]