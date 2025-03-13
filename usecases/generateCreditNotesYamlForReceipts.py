# This script is to generate yaml files for credit notes for receipts from .csv.
from src.synertools import Synertools

if __name__ == "__main__":

    synertools = Synertools()
    creditNotesUseCases = synertools.container.creditNoteUseCases

    creditNotesUseCases.generate_credit_notes_yaml_from_csv_for_receipts(
        filepath = r"data\input\Receipts.csv",
        workspace_oid="36937.1", # This workspaceOid is only used in the url request, the creditnote will take the oid from the original document
        balance_oid="67bf79057c7343444851ecb0" # oid or ObjectId, An open balance, this will be part of the creditnote
        )