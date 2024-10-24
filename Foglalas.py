from Jarat import Jarat


class Foglalas:
    def __init__(self, jarat: Jarat, utas_nev: str):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def __str__(self):
        return f"{self.utas_nev} - {self.jarat.jaratszam} - {self.jarat.celallomas} - {self.jarat.jegyar} HUF"
