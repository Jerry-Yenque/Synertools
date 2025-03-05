from dataclasses import dataclass
from typing import List
from decimal import Decimal
from src.data.model.receipt import TaxEntry

@dataclass
class Position:
    crossPrice: Decimal
    crossUnitPrice: Decimal
    netPrice: Decimal
    netUnitPrice: Decimal
    productOid: str
    quantity: int
    taxAmount: Decimal
    taxes: TaxEntry

@dataclass
class CalculatorResponse:
    crossTotal: Decimal
    netTotal: Decimal
    payableAmount: Decimal
    positions: List[Position]
    taxTotal: Decimal
    taxes: List[TaxEntry]