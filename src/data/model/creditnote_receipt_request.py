from src.data.model.receipt import ReceiptResponse, Payment
from dataclasses import dataclass, field

@dataclass
class CreditNoteForReceiptRequest(ReceiptResponse):
    type: str = field(init=False)
    sourceDocOid: str = field(init=False)

    @classmethod
    def from_receipt(cls, receipt: ReceiptResponse, balanceOid: str) -> "CreditNoteForReceiptRequest":

        adjusted_payments = []

        for original_payment in receipt.payments:
            adjusted_payment = Payment(
                oid=original_payment.oid,
                type=original_payment.type,
                amount=-original_payment.amount, # This is what we change
                currency=original_payment.currency,
                exchangeRate=original_payment.exchangeRate,
                cardTypeId=original_payment.cardTypeId,
                cardLabel=original_payment.cardLabel,
                mappingKey=original_payment.mappingKey,
                serviceProvider=original_payment.serviceProvider,
                authorization=original_payment.authorization,
                operationDateTime=original_payment.operationDateTime,
                operationId=original_payment.operationId,
                info=original_payment.info,
                cardNumber=original_payment.cardNumber,
                equipmentIdent=original_payment.equipmentIdent,
                collectOrderId=original_payment.collectOrderId
            )

            adjusted_payments.append(adjusted_payment)

        instance = cls(
            oid=None,
            id=None,
            number=None,
            items=receipt.items,
            status=receipt.status,
            date=receipt.date,
            currency=receipt.currency,
            netTotal=receipt.netTotal,
            crossTotal=receipt.crossTotal,
            exchangeRate=receipt.exchangeRate,
            payableAmount=receipt.payableAmount,
            taxes=receipt.taxes,
            contactOid=receipt.contactOid,
            workspaceOid=receipt.workspaceOid,
            note=receipt.note,
            employeeRelations=receipt.employeeRelations,
            balanceOid=balanceOid,
            payments=adjusted_payments, 
            discount=receipt.discount,
            receiptItems=receipt.receiptItems,
            contact=receipt.contact
        )

        # Establecer los campos adicionales
        instance.type = "CREDITNOTE"
        instance.sourceDocOid = receipt.oid or receipt.id

        return instance