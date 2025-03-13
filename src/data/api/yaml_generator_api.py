from dataclasses import asdict

import requests
import simplejson as json

from src.data.api.interceptor.auth_interceptor import Auth
from src.data.model.creditnote_invoice_request import CreditNoteForInvoiceRequest
from src.data.model.creditnote_receipt_request import CreditNoteForReceiptRequest
from src.ui.theme.color import GRAY, GREEN, RED, YELLOW


class YamlGeneratorApi:
    def __init__(self, host: str) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        self.host = host

    def generateCreditNoteYaml(self, workSpaceOid: str, body: CreditNoteForReceiptRequest | CreditNoteForInvoiceRequest) -> requests.Response:
        """ Generate the yaml file. """
        Auth.check_auth()

        headers = {
            'Authorization': f'Bearer {Auth.token}',  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            'Content-Type': 'application/json'
        }

        # url = f"{self.host}/api/creditnotes?workspaceOid={workSpaceOid}" # New Endpoint
        url = f"{self.host}/api/workspaces/{workSpaceOid}/documents/creditnotes" # Old Endpoint

        body_dict = asdict(body)
        json_data = json.dumps(body_dict, use_decimal=True)

        response = requests.post(url=url, headers=headers, data=json_data)
        if response.status_code == 200:
            print(f"{GREEN}Credit note done! -> {response.json()["number"]}{GRAY}")
        else:
            print(f"{RED}Something happens!{GRAY}")
        response.raise_for_status() 
        return response


if __name__ == "__main__":
    # 36937.4
    body = """{
    "oid": null,
    "id": null,
    "number": null,
    "items": [
        {
            "oid": null,
            "index": 1,
            "parentIdx": null,
            "productOid": "7044.145071",
            "standInOid": null,
            "quantity": 1,
            "netUnitPrice": 143.2203,
            "crossUnitPrice": 169.0003,
            "netPrice": 143.2203,
            "crossPrice": 169.0003,
            "currency": "PEN",
            "exchangeRate": 1,
            "taxes": [
                {
                    "tax": {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    },
                    "base": 143.2203,
                    "amount": 25.78,
                    "currency": "PEN",
                    "exchangeRate": 1
                }
            ],
            "remark": null,
            "bomOid": null,
            "product": {
                "oid": "7044.145071",
                "sku": "00322.82.2.E00",
                "type": "STANDART",
                "description": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "note": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "imageOid": null,
                "netPrice": 143.2203,
                "crossPrice": 168.99995400000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7004.196888",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "standIn": {
                "oid": "7004.196888",
                "sku": "8426880015576",
                "type": "BATCH",
                "description": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "note": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "imageOid": null,
                "netPrice": 143.2203,
                "crossPrice": 168.99995400000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7044.145071",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "description": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
            "sku": "00322.82.2.E00",
            "uoMCode": "NIU",
            "child": false,
            "parent": true
        },
        {
            "oid": null,
            "index": 2,
            "parentIdx": null,
            "productOid": "7044.61785",
            "standInOid": null,
            "quantity": 1,
            "netUnitPrice": 15.0000,
            "crossUnitPrice": 17.7000,
            "netPrice": 15.0000,
            "crossPrice": 17.7000,
            "currency": "PEN",
            "exchangeRate": 1,
            "taxes": [
                {
                    "tax": {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    },
                    "base": 15.0000,
                    "amount": 2.70,
                    "currency": "PEN",
                    "exchangeRate": 1
                }
            ],
            "remark": null,
            "bomOid": null,
            "product": {
                "oid": "7044.61785",
                "sku": "ZZZZ",
                "type": "STANDART",
                "description": "Givenchy Frag Irresi",
                "note": "Givenchy Frag Irresistible Edp 80 ml.",
                "imageOid": null,
                "netPrice": 15.0000,
                "crossPrice": 17.70000000000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7004.327295",
                        "quantity": null,
                        "type": "BATCH"
                    },
                    {
                        "label": null,
                        "productOid": "7004.61786",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [
                    {
                        "type": "Código de Barra",
                        "code": "1234567"
                    }
                ],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "standIn": {
                "oid": "7004.61786",
                "sku": "1-P036175",
                "type": "BATCH",
                "description": "Givenchy Frag Irresi",
                "note": "Givenchy Frag Irresistible Edp 80 ml",
                "imageOid": null,
                "netPrice": 15.0000,
                "crossPrice": 17.70000000000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7044.61785",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "description": "Givenchy Frag Irresi",
            "sku": "ZZZZ",
            "uoMCode": "NIU",
            "child": false,
            "parent": true
        }
    ],
    "status": "CLOSED",
    "date": "2025-02-21",
    "currency": "PEN",
    "netTotal": 158.22,
    "crossTotal": 186.70,
    "exchangeRate": 1,
    "payableAmount": 186.70,
    "taxes": [
        {
            "tax": {
                "oid": "14063.2",
                "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                "name": "I.G.V.",
                "percent": 18.0000000000000000,
                "type": "ADVALOREM",
                "amount": null,
                "currency": "PEN",
                "exchangeRate": 1
            },
            "base": 158.22,
            "amount": 28.48,
            "currency": "PEN",
            "exchangeRate": 1
        }
    ],
    "contactOid": "5435.274",
    "workspaceOid": "36937.4",
    "note": null,
    "employeeRelations": [
        {
            "type": "SELLER",
            "employeeOid": "9875.11"
        }
    ],
    "balanceOid": "36913.411",
    "payments": [
        {
            "amount": 186.70,
            "currency": "PEN",
            "exchangeRate": 1,
            "type": "CASH"
        }
    ],
    "discount": null,
    "contact": {
        "oid": "5435.274",
        "id": "677ed7814cab6601b26834fb",
        "name": "YENQUE CALERO, JERRY ALDAIR",
        "idType": "DNI",
        "idNumber": "76804040",
        "email": "",
        "forename": null,
        "firstLastName": null,
        "secondLastName": null
    },
    "receiptItems": [
        {
            "oid": null,
            "index": 1,
            "parentIdx": null,
            "productOid": "7044.145071",
            "standInOid": null,
            "quantity": 1,
            "netUnitPrice": 143.2203,
            "crossUnitPrice": 169.0003,
            "netPrice": 143.2203,
            "crossPrice": 169.0003,
            "currency": "PEN",
            "exchangeRate": 1,
            "taxes": [
                {
                    "tax": {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    },
                    "base": 143.2203,
                    "amount": 25.78,
                    "currency": "PEN",
                    "exchangeRate": 1
                }
            ],
            "remark": null,
            "bomOid": null,
            "product": {
                "oid": "7044.145071",
                "sku": "00322.82.2.E00",
                "type": "STANDART",
                "description": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "note": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "imageOid": null,
                "netPrice": 143.2203,
                "crossPrice": 168.99995400000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7004.196888",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "standIn": {
                "oid": "7004.196888",
                "sku": "8426880015576",
                "type": "BATCH",
                "description": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "note": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
                "imageOid": null,
                "netPrice": 143.2203,
                "crossPrice": 168.99995400000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7044.145071",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "description": "Majorica Aretes Cies 6mm Perla Tahiti Clásico",
            "sku": "00322.82.2.E00",
            "uoMCode": "NIU",
            "child": false,
            "parent": true
        },
        {
            "oid": null,
            "index": 2,
            "parentIdx": null,
            "productOid": "7044.61785",
            "standInOid": null,
            "quantity": 1,
            "netUnitPrice": 15.0000,
            "crossUnitPrice": 17.7000,
            "netPrice": 15.0000,
            "crossPrice": 17.7000,
            "currency": "PEN",
            "exchangeRate": 1,
            "taxes": [
                {
                    "tax": {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    },
                    "base": 15.0000,
                    "amount": 2.70,
                    "currency": "PEN",
                    "exchangeRate": 1
                }
            ],
            "remark": null,
            "bomOid": null,
            "product": {
                "oid": "7044.61785",
                "sku": "ZZZZ",
                "type": "STANDART",
                "description": "Givenchy Frag Irresi",
                "note": "Givenchy Frag Irresistible Edp 80 ml.",
                "imageOid": null,
                "netPrice": 15.0000,
                "crossPrice": 17.70000000000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7004.327295",
                        "quantity": null,
                        "type": "BATCH"
                    },
                    {
                        "label": null,
                        "productOid": "7004.61786",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [
                    {
                        "type": "Código de Barra",
                        "code": "1234567"
                    }
                ],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "standIn": {
                "oid": "7004.61786",
                "sku": "1-P036175",
                "type": "BATCH",
                "description": "Givenchy Frag Irresi",
                "note": "Givenchy Frag Irresistible Edp 80 ml",
                "imageOid": null,
                "netPrice": 15.0000,
                "crossPrice": 17.70000000000000000000,
                "currency": "PEN",
                "categories": [],
                "taxes": [
                    {
                        "oid": "14063.2",
                        "key": "06e40be6-40d8-44f4-9d8f-585f2f97ce63",
                        "catKey": "ed28d3c0-e55d-45e5-8025-e48fc989c9dd",
                        "name": "I.G.V.",
                        "percent": 18.0000000000000000,
                        "type": "ADVALOREM",
                        "amount": null,
                        "currency": "PEN",
                        "exchangeRate": 1
                    }
                ],
                "uoM": "item",
                "uoMCode": "NIU",
                "relations": [
                    {
                        "label": null,
                        "productOid": "7044.61785",
                        "quantity": null,
                        "type": "BATCH"
                    }
                ],
                "indicationSets": [],
                "barcodes": [],
                "bomGroupConfigs": [],
                "configurationBOMs": [],
                "individual": "BATCH"
            },
            "description": "Givenchy Frag Irresi",
            "sku": "ZZZZ",
            "uoMCode": "NIU",
            "child": false,
            "parent": true
        }
    ],
    "type" : "CREDITNOTE",
    "sourceDocOid": "14257.9094"
}"""
    yamp_generator_api = YamlGeneratorApi("http://localhost:8080")
    response = yamp_generator_api.generateCreditNoteYaml(workSpaceOid="36937.4", body=body)
    print(response)