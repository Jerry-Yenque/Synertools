from src.domain.model.receipt import Receipt

# @DEPRECATED
# def receiptToDomain(data: dict) -> Receipt:
#     return Receipt(
#         id=str(data['_id']),
#         oid=data.get("oid", str(data['_id'])),
#         number=data["number"]
#         )

def invoiceToDomain(data: dict) -> Receipt:
    return Receipt(
        id=str(data['_id']),
        oid=data.get("oid", str(data['_id'])),
        number=data["number"]
        )