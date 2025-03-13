# This script is to generate yaml files for credit notes for invoices from .csv.
from src.synertools import Synertools

if __name__ == "__main__":

    synertools = Synertools()
    creditNotesUseCases = synertools.container.creditNoteUseCases

    creditNotesUseCases.generate_credit_notes_yaml_from_csv_for_invoices(
        filepath = r"data\input\Invoices.csv",
        workspace_oid="36937.1",
        balance_oid="67bf79057c7343444851ecb0" # oid or ObjectId, An open balance
        )