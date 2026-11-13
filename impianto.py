from pannello import PannelloFotovoltaico

class ImpiantoSolare:
    LOCALITA = {"Bologna", "Parma"}
    STATO = {"in installazione", "in collaudo", "attivo"}
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        if self.localita not in self.LOCALITA:
            raise ValueError("Località non valida")
        if self.stato in self.STATO:
            raise ValueError("Stato non valido")
        
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli: list[PannelloFotovoltaico] = []
        
    def aggiungi_pannello(self, pannello_nuovo: PannelloFotovoltaico) -> None:
        pot_attuale = potenza_pannelli()
        agg = True
        for pannello in self.pannelli:
            if pannello.codice == pannello_nuovo.codice:
                agg = False
                
        if agg:
            if pot_attuale + pannello_nuovo.potenza_kw <= self.potenza_massima_kw:
                self.pannelli.append(pannello_nuovo)
        
    def potenza_pannelli(self) -> float:
        pot = 0
        for pannelo in self.pannelli:
            pot = pot + pannelo.potenza_kw
        return pot
    
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico:
        return[pannello for pannello in self.pannelli if codice == pannello.codice]
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico:
        p: PannelloFotovoltaico
        for pannello in self.pannelli:
            if codice == pannello.codice:
                p = pannello
                self.pannelli.remove(pannello)
            return p
        return None
    
    def pannelli_sotto_potenza(self, potenza_massima: float) -> list[PannelloFotovoltaico]:
        return[pannello for pannello in self.pannelli if pannello <= potenza_massima]
