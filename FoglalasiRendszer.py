from typing import List, Optional
from Foglalas import Foglalas
from Jarat import Jarat


class FoglalasiRendszer:
    def __init__(self):
        self.foglalasok: List[Foglalas] = []

    def jegy_foglalasa(self, jarat: Jarat, utas_nev: str) -> Foglalas:
        foglalas = Foglalas(jarat, utas_nev)
        self.foglalasok.append(foglalas)
        return foglalas

    def foglalas_lemondasa(self, foglalas: Foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True
        return False

    def list_foglalasok(self):
        for foglalas in self.foglalasok:
            print(foglalas)
