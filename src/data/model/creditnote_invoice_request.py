from dataclasses import dataclass, field

from src.data.model.invoice import InvoiceResponse
from src.data.model.receipt_response import Payment


@dataclass
class CreditNoteForInvoiceRequest(InvoiceResponse):
    type: str = field(init=False)
    sourceDocOid: str = field(init=False)

    @classmethod
    def from_invoice(cls, invoice: InvoiceResponse, balanceOid: str) -> "CreditNoteForInvoiceRequest":

        adjusted_payments = []

        for original_payment in invoice.payments:
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
            items=invoice.items,
            status=invoice.status,
            date=invoice.date,
            currency=invoice.currency,
            netTotal=invoice.netTotal,
            crossTotal=invoice.crossTotal,
            exchangeRate=invoice.exchangeRate,
            payableAmount=invoice.payableAmount,
            taxes=invoice.taxes,
            contactOid=invoice.contactOid,
            workspaceOid=invoice.workspaceOid,
            note=invoice.note,
            employeeRelations=invoice.employeeRelations,
            balanceOid=balanceOid,
            payments=adjusted_payments, 
            discount=invoice.discount,
             contact=invoice.contact,
            invoiceItems=invoice.invoiceItems,
        )

        # Establecer los campos adicionales
        instance.type = "CREDITNOTE"
        instance.sourceDocOid = invoice.oid or invoice.id

        return instance