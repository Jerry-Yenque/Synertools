from dataclasses import dataclass
from typing import Optional, List

from src.data.model.Payment import Payment


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
    payments: List[Payment]
    items: List[ReceiptItem]
    crossTotal: str
    contactOid: str
    user: str

    def __post_init__(self) -> None:
        self.sort_by_item_index()

    def sort_by_item_index(self) -> None:
        """Sort the 'items' array by 'index' field in ascending order."""
        self.items.sort(key=lambda item: item.index)
