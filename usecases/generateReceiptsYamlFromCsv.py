# This script is to generate yaml files for Receipts from .csv.
from src.synertools import Synertools

if __name__ == "__main__":

    synertools = Synertools()
    receiptUseCases = synertools.container.receiptUseCases

    receiptUseCases.generate_receipts_yaml_from_csv(
        filepath = r"data\input\Receipts.csv",
        workspace_oid="36937.2",
        balance_oid="67bf79057c7343444851ecb0"
        )
