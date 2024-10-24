from typing import List
from Jarat import Jarat


class LegiTarsasag:
    def __init__(self, nev: str):
        self.nev = nev
        self.jaratok: List[Jarat] = []

    def add_jarat(self, jarat: Jarat):
        self.jaratok.append(jarat)

    def list_jaratok(self):
        for jarat in self.jaratok:
            print(f"{jarat.jaratszam} - {jarat.celallomas} ({jarat.jarat_tipus()}) - {jarat.jegyar} HUF")
