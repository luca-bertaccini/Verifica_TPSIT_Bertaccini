class PannelloFotovoltaico:
    MODELLI = {"Aurora", "Helios bifacciale"}
    def __init__(self, codice: str, modello: str, potenza_kw: float) -> None:
        if self.modello not in self.MODELLI:
            raise ValueError("Modello non valido")
        if self.potenza_kw < 0:
            raise ValueError("La potenza non può essere negativa")
        
        self.codice = codice
        self.modello = modello
        self.potenza_kw = potenza_kw
        
    