from dataclasses import dataclass
from typing import List
from decimal import Decimal
from src.data.model.receipt import TaxEntry

@dataclass
class Position:
    productOid: str
    crossPrice: Decimal
    crossUnitPrice: Decimal
    netPrice: Decimal
    netUnitPrice: Decimal
    quantity: int
    taxAmount: Decimal
    taxes: List[TaxEntry]

@dataclass
class CalculatorResponse:
    crossTotal: Decimal
    netTotal: Decimal
    payableAmount: Decimal
    positions: List[Position]
    taxTotal: Decimal
    taxes: List[TaxEntry]