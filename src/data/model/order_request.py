from src.data.model.receipt import TaxEntry, TaxDetail
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, List
from src.domain.model.receipt import Receipt, ReceiptItem
from src.data.model.calculator_response import CalculatorResponse, Position
import src.ui.theme.color as Color
from pprint import pprint

@dataclass
class OrderItem:
    index: int
    productOid: str
    quantity: int
    netUnitPrice: Decimal
    netPrice: Decimal
    crossUnitPrice: Decimal
    crossPrice: Decimal
    remark: Optional[str]
    taxes: List[TaxEntry]

@dataclass
class OrderRequest:
    items: List[OrderItem]
    status: str
    netTotal: Decimal
    crossTotal: Decimal
    payableAmount: Decimal
    taxes: List[TaxEntry]
    contactOid: Optional[str]

    @classmethod
    def from_receipt_and_calculator(cls, receipt: Receipt, calculator_response: CalculatorResponse) -> 'OrderRequest':
        order_items = []

        for receipt_item, calculator_position in zip(receipt.items, calculator_response.positions):
            if (receipt_item.productOid == calculator_position.productOid):
                # print(f"{Color.GREEN}Looks good..{Color.GRAY}")
                try:
                    order_item = OrderItem(
                        index=receipt_item.index,
                        productOid=calculator_position.productOid,
                        quantity=calculator_position.quantity,
                        netUnitPrice=calculator_position.netUnitPrice,
                        netPrice=calculator_position.netPrice,
                        crossUnitPrice=calculator_position.crossUnitPrice,
                        crossPrice=calculator_position.crossPrice,
                        remark=receipt_item.remark,
                        taxes=calculator_position.taxes
                    )
                    order_items.append(order_item)
                except Exception as e:
                    print(f"{Color.RED}Something happens mapping to OrderRequest...{e}{Color.GRAY}")
            else:
                print(f"{Color.RED}Sequence loss...{Color.GRAY}")
                raise ValueError(f"Sequence loss: productOid mismatch between receipt_item {receipt_item.productOid} and calculator_position {calculator_position.productOid}")

        # Lógica para transformar receipt y calculator_response en OrderRequest
        return cls(
            items= order_items,
            status = "OPEN",
            netTotal = calculator_response.netTotal,
            crossTotal = calculator_response.crossTotal,
            payableAmount = calculator_response.payableAmount,
            taxes= calculator_response.taxes,
            contactOid = receipt.contactOid
        )
    
if __name__ == "__main__": 
    receipt_mongo = Receipt(id='677bd3df2c6c472706a043f9', oid='14257.2965709', number='B908-00462092', items=[ReceiptItem(index=1, productOid='7044.57', quantity='1', remark=None), ReceiptItem(index=2, productOid='7044.2', quantity='1', remark='PIÑA\nLLVAR \nCARMEN MALCA \nPC PISO 2 ')], contactOid='5435.1')
    calculator_response = CalculatorResponse(crossTotal=Decimal('15.00'), netTotal=Decimal('13.64'), payableAmount=Decimal('15.00'), positions=[Position(productOid='7044.57', crossPrice=Decimal('1.9982'), crossUnitPrice=Decimal('1.9982'), netPrice=Decimal('1.8182'), netUnitPrice=Decimal('1.8182'), quantity=1, taxAmount=Decimal('0.18'), taxes=[TaxEntry(tax=TaxDetail(oid='14063.4', key='06e40be6-40d8-44f4-9d8f-585f2f97ce63', catKey='ed28d3c0-e55d-45e5-8025-e48fc989c9dd', name='I.G.V.', percent=Decimal('10.0000000000000000'), type='ADVALOREM', amount=None, currency='PEN', exchangeRate=1), base=Decimal('1.8182'), amount=Decimal('0.18'), currency='PEN', exchangeRate=1)]), Position(productOid='7044.2', crossPrice=Decimal('12.9980'), crossUnitPrice=Decimal('12.9980'), netPrice=Decimal('11.8180'), netUnitPrice=Decimal('11.8180'), quantity=1, taxAmount=Decimal('1.18'), taxes=[TaxEntry(tax=TaxDetail(oid='14063.4', key='06e40be6-40d8-44f4-9d8f-585f2f97ce63', catKey='ed28d3c0-e55d-45e5-8025-e48fc989c9dd', name='I.G.V.', percent=Decimal('10.0000000000000000'), type='ADVALOREM', amount=None, currency='PEN', exchangeRate=1), base=Decimal('11.8180'), amount=Decimal('1.18'), currency='PEN', exchangeRate=1)])], taxTotal=Decimal('1.36'), taxes=[TaxEntry(tax=TaxDetail(oid='14063.4', key='06e40be6-40d8-44f4-9d8f-585f2f97ce63', catKey='ed28d3c0-e55d-45e5-8025-e48fc989c9dd', name='I.G.V.', percent=Decimal('10.0000000000000000'), type='ADVALOREM', amount=None, currency='PEN', exchangeRate=1), base=Decimal('13.64'), amount=Decimal('1.36'), currency='PEN', exchangeRate=1)])

    # print(f"{Color.GREEN}{receipt_mongo}{Color.GRAY}\n\n")
    # print(f"{Color.YELLOW}{calculator_response}{Color.GRAY}")

    order_request = OrderRequest.from_receipt_and_calculator(receipt=receipt_mongo, calculator_response=calculator_response)