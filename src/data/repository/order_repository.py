from decimal import Decimal
from pprint import pprint

import src.ui.theme.color as color
from src.data.api.order_api import OrderApi
from src.data.model.create_receipt_request import TaxEntry
from src.data.model.order_request import OrderRequest, OrderItem
from src.data.model.receipt_response import TaxDetail


class OrderRepository:
    def __init__(self, order_api: OrderApi) -> None:
        print(f"{color.YELLOW}{self.__class__.__name__} Init.{color.GRAY}")
        self.__order_api = order_api

    def create_order(self, body: OrderRequest) -> dict:
        return self.__order_api.create_order_old(body=body)
    
if __name__ == "__main__": 
    order_api_test =  OrderApi("http://localhost:8080")

    order_repository = OrderRepository(order_api=order_api_test)

    order_request = OrderRequest(items=[OrderItem(index=1,
                                                  productOid='7044.57',
                                                  quantity=1,
                                                  netUnitPrice=Decimal('1.8182'),
                                                  netPrice=Decimal('1.8182'),
                                                  crossUnitPrice=Decimal('1.9982'),
                                                  crossPrice=Decimal('1.9982'),
                                                  remark=None,
                                                  taxes=[TaxEntry(tax=TaxDetail(oid='14063.4',
                                                                                    key='06e40be6-40d8-44f4-9d8f-585f2f97ce63',
                                                                                    catKey='ed28d3c0-e55d-45e5-8025-e48fc989c9dd',
                                                                                    name='I.G.V.',
                                                                                    percent=Decimal('10.0000000000000000'),
                                                                                    type='ADVALOREM',
                                                                                    amount=None,
                                                                                    currency='PEN',
                                                                                    exchangeRate=1),
                                                                  base=Decimal('1.8182'),
                                                                  amount=Decimal('0.18'),
                                                                  currency='PEN',
                                                                  exchangeRate=1)]),
                                        OrderItem(index=2,
                                                  productOid='7044.2',
                                                  quantity=1,
                                                  netUnitPrice=Decimal('11.8180'),
                                                  netPrice=Decimal('11.8180'),
                                                  crossUnitPrice=Decimal('12.9980'),
                                                  crossPrice=Decimal('12.9980'),
                                                  remark='PIÑA\nLLVAR \nCARMEN MALCA \nPC PISO 2 ',
                                                  taxes=[TaxEntry(tax=TaxDetail(oid='14063.4',
                                                                                    key='06e40be6-40d8-44f4-9d8f-585f2f97ce63',
                                                                                    catKey='ed28d3c0-e55d-45e5-8025-e48fc989c9dd',
                                                                                    name='I.G.V.',
                                                                                    percent=Decimal('10.0000000000000000'),
                                                                                    type='ADVALOREM',
                                                                                    amount=None,
                                                                                    currency='PEN',
                                                                                    exchangeRate=1),
                                                                  base=Decimal('11.8180'),
                                                                  amount=Decimal('1.18'),
                                                                  currency='PEN',
                                                                  exchangeRate=1)])],
                                 status='OPEN',
                                 netTotal=Decimal('13.64'),
                                 crossTotal=Decimal('15.00'),
                                 payableAmount=Decimal('15.00'),
                                 taxes=[TaxEntry(tax=TaxDetail(oid='14063.4',
                                                                   key='06e40be6-40d8-44f4-9d8f-585f2f97ce63',
                                                                   catKey='ed28d3c0-e55d-45e5-8025-e48fc989c9dd',
                                                                   name='I.G.V.',
                                                                   percent=Decimal('10.0000000000000000'),
                                                                   type='ADVALOREM',
                                                                   amount=None,
                                                                   currency='PEN',
                                                                   exchangeRate=1),
                                                 base=Decimal('13.64'),
                                                 amount=Decimal('1.36'),
                                                 currency='PEN',
                                                 exchangeRate=1)],
                                 contactOid='5435.1')
    response = order_repository.create_order(body=order_request)
    
    pprint(response)