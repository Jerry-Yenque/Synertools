""" Simple Payment, used in: CreateReceiptRequest, OrderRequest(test) """
from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

@dataclass
class Payment:
    type: str
    amount: Decimal
    mappingKey: Optional[str]
    currency: str
    exchangeRate: str
    collectOrderId: Optional[str]