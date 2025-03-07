from dataclasses import dataclass
from typing import List

@dataclass
class Position:
    quantity: int
    productOid: str

@dataclass
class CalculatorRequest:
    positions: List[Position]
