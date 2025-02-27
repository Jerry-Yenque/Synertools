from dataclasses import dataclass
from typing import Optional, List, Any
from decimal import Decimal

@dataclass
class TaxDetail:
    oid: str
    key: str
    catKey: str
    name: str
    percent: Decimal
    type: str
    amount: Optional[Decimal]
    currency: str
    exchangeRate: int

@dataclass
class TaxEntry:
    tax: TaxDetail
    base: Decimal
    amount: Decimal
    currency: str
    exchangeRate: int

@dataclass
class Barcode:
    type: str
    code: str

@dataclass
class Relation:
    label: Optional[str]
    productOid: str
    quantity: Optional[Decimal] ####### DECIMAL OR INTEGER????????
    type: str

@dataclass
class Category:
    categoryOid: str
    weight: int

@dataclass 
class Indication:
    oid: str
    value: str
    description: str
    imageOid: Optional[str]

@dataclass
class IndicationSet:
    oid: str
    name: str
    description: str
    required: bool
    multiple: bool
    imageOid: Optional[str]
    indications: List[Indication]

@dataclass
class Product:
    oid: str
    sku: str
    type: str
    description: str
    note: Optional[str]
    imageOid: Optional[str]
    netPrice: Decimal
    crossPrice: Decimal
    currency: str
    categories: List[Category]
    taxes: List[TaxDetail]
    uoM: str
    uoMCode: str
    relations: List[Relation]
    indicationSets: List[IndicationSet]
    barcodes: List[Barcode]
    bomGroupConfigs: List[Any]
    configurationBOMs: List[Any]
    # individual: str # For new versions


@dataclass
class Item:
    oid: Optional[str]
    index: int
    parentIdx: Optional[int]
    productOid: str
    # standInOid: Optional[str] # For new versions
    quantity: int
    netUnitPrice: Decimal
    crossUnitPrice: Decimal
    netPrice: Decimal
    crossPrice: Decimal
    currency: str
    exchangeRate: int
    taxes: List[TaxEntry]
    remark: Optional[str]
    # bomOid: Optional[str] # For new versions
    product: Product
    # standIn: Product # For new versions
    description: str
    uoMCode: str
    sku: str
    child: bool
    parent: bool

@dataclass
class EmployeeRelation:
    type: str
    employeeOid: str

@dataclass
class Payment:
    oid: Optional[str]
    type: str
    amount: Decimal
    currency: str
    exchangeRate: int
    cardTypeId: Optional[int]
    cardLabel: Optional[str]
    mappingKey: Optional[str]
    serviceProvider: Optional[str]
    authorization: Optional[str]
    operationDateTime: Optional[str]
    operationId: Optional[str]
    info: Optional[str]
    cardNumber: Optional[str]
    equipmentIdent: Optional[str]
    collectOrderId: Optional[str]

@dataclass
class Contact:
    oid: str
    id: str
    name: str
    idType: str
    idNumber: str
    email: Optional[str]
    # forename: Optional[str]
    # firstLastName: Optional[str]
    # secondLastName: Optional[str]

@dataclass
class ReceiptResponse:
    oid: Optional[str]
    id: str
    number: str
    items: List[Item]
    status: str
    date: str
    currency: str
    netTotal: Decimal
    crossTotal: Decimal
    exchangeRate: int
    payableAmount: Decimal
    taxes: List[TaxEntry]
    contactOid: str
    workspaceOid: str
    note: Optional[str]
    employeeRelations: List[EmployeeRelation]
    balanceOid: str
    payments: List[Payment]
    discount: Optional[Decimal]
    contact: Contact
    receiptItems: List[Item]