from decimal import Decimal
from pprint import pprint

from src.data.model.Payment import Payment
from src.data.model.calculator_request import CalculatorRequest
from src.data.model.calculator_request import Position
from src.domain.model.receipt import Receipt, ReceiptItem


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
    
    receipt_test = Receipt(id='677bd3df2c6c472706a043f9', oid='14257.2965709', number='B908-00462092', payments=[Payment(type='CASH', amount=Decimal('15'), mappingKey=None, currency='PEN', exchangeRate='0', collectOrderId=None)], items=[ReceiptItem(index=1, productOid='7044.57', quantity='1', remark=None), ReceiptItem(index=2, productOid='7044.2', quantity='1', remark='PIÑA\nLLVAR \nCARMEN MALCA \nPC PISO 2 ')], crossTotal='15', contactOid='5435.1', user='UL - Lita Arellano')
    
    pprint(receipt_test)

    # Mapping Receipt to CalculatorRequest
    calculator_request = receipt_to_calculator_request(receipt_test)
    pprint(calculator_request)
