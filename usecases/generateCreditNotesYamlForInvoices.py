# This script is to generate yaml files for credit notes for invoices from .csv.
from src.synertools import Synertools

if __name__ == "__main__":

    synertools = Synertools()
    creditNotesUseCases = synertools.container.creditNoteUseCases

    creditNotesUseCases.generateCreditNotesYamlFromCsvForInvoices(
        filepath = r"data\input\Invoices.csv",
        workSpaceOid="36937.1",
        balanceOid="67bf79057c7343444851ecb0" # oid or ObjectId, An open balance
        )