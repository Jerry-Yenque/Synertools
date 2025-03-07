
# class Receipt:
#     def __init__(self, id: str, oid: str, number: str) -> None:
#         self.id = id
#         self.oid = oid
#         self.number = number

#     def __repr__(self) -> str:
#         # Devuelve una cadena útil para depuración (debug)
#         return f"Receipt(id='{self.id}', oid='{self.oid}', number='{self.number}')"

from dataclasses import dataclass
from typing import Optional, List
from decimal import Decimal

@dataclass
class ReceiptItem:
    index: int
    productOid: str
    quantity: str
    # netUnitPrice: Decimal # Not needed yet
    # crossUnitPrice: Decimal # Not needed yet
    # netPrice: Decimal # Not needed yet
    # crossPrice: Decimal # Not needed yet
    # currency: str # Not needed yet
    # exchangeRate: str # Not needed yet
    remark: Optional[str]

@dataclass
class Receipt:
    id: str
    oid: str
    number: str
    items: List[ReceiptItem]
    crossTotal: str
    contactOid: str
    user: str

    def __post_init__(self) -> None:
        self.sort_by_item_index()

    def sort_by_item_index(self) -> None:
        """Sort the 'items' array by 'index' field in ascending order."""
        self.items.sort(key=lambda item: item.index)