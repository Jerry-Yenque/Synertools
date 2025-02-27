class Receipt:
    def __init__(self, id: str, oid: str, number: str) -> None:
        self.id = id
        self.oid = oid
        self.number = number

    def __repr__(self) -> str:
        # Devuelve una cadena útil para depuración (debug)
        return f"Receipt(id='{self.id}', oid='{self.oid}', number='{self.number}')"