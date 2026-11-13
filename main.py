from pannello import PannelloFotovoltaico
from impianto import ImpiantoSolare

def registra_impianto(self, impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) -> None:
    add = True
    for imp in impianti:
        if imp.codice == impianto.codice:
            add = False
    if add:
        self.impianti.append(impianto)
    if add == False:
        raise ValueError("Codice già presente")