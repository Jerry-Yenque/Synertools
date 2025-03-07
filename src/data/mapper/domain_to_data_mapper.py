from src.domain.model.receipt import Receipt, ReceiptItem
from src.data.model.calculator_request import CalculatorRequest
from src.data.model.calculator_request import Position
from decimal import Decimal
from pprint import pprint

def receipt_to_calculator_request(receipt: Receipt) -> CalculatorRequest:
    positions = []
    for item in receipt.items:
        try:
            quantity_int = int(item.quantity)
        except ValueError:
            raise ValueError(f"El valor '{item.quantity}' en OrderItem con productOid '{item.productOid}' no se puede convertir a entero")
        except:
            raise ValueError(f"Something happens")
        position = Position(
            quantity=quantity_int,
            productOid=item.productOid
        )
        positions.append(position)
    return CalculatorRequest(positions=positions)


if __name__ == "__main__":
    # Creando datos de ejemplo
    order_item_1 = ReceiptItem(
        index=2,
        productOid="prod-321",
        quantity="2",
        netUnitPrice=Decimal("10.00"),
        crossUnitPrice=Decimal("12.00"),
        netPrice=Decimal("50.00"),
        crossPrice=Decimal("60.00"),
        currency="USD",
        exchangeRate="1.0",
        remark="Con descuento"
    )

    order_item_2 = ReceiptItem(
        index=1,
        productOid="prod-123",
        quantity="5",
        netUnitPrice=Decimal("10.00"),
        crossUnitPrice=Decimal("12.00"),
        netPrice=Decimal("50.00"),
        crossPrice=Decimal("60.00"),
        currency="USD",
        exchangeRate="1.0",
        remark="Sin descuento"
    )
    
    receipt = Receipt(
        id="r-001",
        oid="o-001",
        number="1001",
        items=[order_item_1, order_item_2]
    )
    
    pprint(receipt)

    # Mapping Receipt to CalculatorRequest
    calculator_request = receipt_to_calculator_request(receipt)
    pprint(calculator_request)
