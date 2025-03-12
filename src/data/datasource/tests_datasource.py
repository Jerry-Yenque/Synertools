from decimal import Decimal

from src.data.model.calculator_request import CalculatorRequest, Position
from src.data.model.create_receipt_request import CreateReceiptRequest, Payment, TaxDetail, TaxEntry
from src.data.model.order_request import OrderRequest, OrderItem
from src.data.model.receipt_response import TaxDetail as TaxDetailPlus


def get_create_receipt_request() -> CreateReceiptRequest:
    payment1 = Payment(
        type="ELECTRONIC",
        amount=Decimal("1"),
        mappingKey="IZIPACARD",
        currency="PEN",
        exchangeRate="1",  # aunque en el JSON viene como "1", aquí se instancia como int
        collectOrderId="67ae3b33fa0f9264c1fdb2cf"
    )

    global_tax_entry = TaxEntry(
        tax=TaxDetail(
            oid="14063.5",
            key="06e40be6-40d8-44f4-9d8f-585f2f97ce63",
            catKey="ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
            name="I.G.V.",
            percent=Decimal("18.0000000000000000"),
            type="ADVALOREM"
        ),
        base=Decimal("33.47"),
        amount=Decimal("6.03"),
        currency="PEN",
        exchangeRate=1
    )

    item2 = OrderItem(
        index=2,
        productOid="7044.117",
        quantity=1,  # "1" convertido a int
        netUnitPrice=Decimal("8.0510"),
        netPrice=Decimal("8.0510"),
        crossUnitPrice=Decimal("9.5010"),
        crossPrice=Decimal("9.5010"),
        # currency="PEN",
        # exchangeRate="1",  # se mantiene como string
        remark="Para llevar (+ S/ 1.50)",
        taxes=[
            TaxEntry(
                tax=TaxDetail(
                    oid="14063.5",
                    key="06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                    catKey="ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                    name="I.G.V.",
                    percent=Decimal("18.0000000000000000"),
                    type="ADVALOREM"
                ),
                base=Decimal("8.0510"),
                amount=Decimal("1.45"),
                currency="PEN",
                exchangeRate=1
            )
        ]
    )

    # Item con index 3
    item3 = OrderItem(
        index=3,
        productOid="7044.35",
        quantity=1,
        netUnitPrice=Decimal("15.2540"),
        netPrice=Decimal("15.2540"),
        crossUnitPrice=Decimal("18.0040"),
        crossPrice=Decimal("18.0040"),
        # currency="PEN",
        # exchangeRate="1",
        remark="Para llevar (+ S/ 1.50)",
        taxes=[
            TaxEntry(
                tax=TaxDetail(
                    oid="14063.5",
                    key="06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                    catKey="ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                    name="I.G.V.",
                    percent=Decimal("18.0000000000000000"),
                    type="ADVALOREM"
                ),
                base=Decimal("15.2540"),
                amount=Decimal("2.75"),
                currency="PEN",
                exchangeRate=1
            )
        ]
    )

    # Item con index 1
    item1 = OrderItem(
        index=1,
        productOid="7044.54",
        quantity=1,
        netUnitPrice=Decimal("10.1610"),
        netPrice=Decimal("10.1610"),
        crossUnitPrice=Decimal("11.9910"),
        crossPrice=Decimal("11.9910"),
        # currency="PEN",
        # exchangeRate="1",
        remark="Para llevar (+ S/ 1.50)",
        taxes=[
            TaxEntry(
                tax=TaxDetail(
                    oid="14063.5",
                    key="06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                    catKey="ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                    name="I.G.V.",
                    percent=Decimal("18.0000000000000000"),
                    type="ADVALOREM"
                ),
                base=Decimal("10.1610"),
                amount=Decimal("1.83"),
                currency="PEN",
                exchangeRate=1
            )
        ]
    )

    # Instancia final de CreateReceiptRequest
    return CreateReceiptRequest(
        payments=[payment1],
        balanceOid="67cb6b759e16661c53e0f572",
        status="OPEN",
        workspaceOid="36937.12",
        netTotal=Decimal("33.47"),
        crossTotal=Decimal("39.50"),
        payableAmount=Decimal("39.50"),
        taxes=[global_tax_entry],
        items=[item2, item3, item1],
        contactOid="5435.3488"
    )

def get_calculator_request() -> CalculatorRequest:
    position_1 = Position(quantity=1, productOid="7044.57")
    position_2 = Position(quantity=1, productOid="7044.2")
    return CalculatorRequest(positions=[position_1, position_2])

def get_order_request() -> OrderRequest:
    return OrderRequest(items=[OrderItem(index=1,
                                  productOid='7044.57',
                                  quantity=1,
                                  netUnitPrice=Decimal('1.8182'),
                                  netPrice=Decimal('1.8182'),
                                  crossUnitPrice=Decimal('1.9982'),
                                  crossPrice=Decimal('1.9982'),
                                  remark=None,
                                  taxes=[TaxEntry(tax=TaxDetailPlus(oid='14063.4',
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
                                  taxes=[TaxEntry(tax=TaxDetailPlus(oid='14063.4',
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
                 taxes=[TaxEntry(tax=TaxDetailPlus(oid='14063.4',
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