from abc import ABC, abstractmethod


class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass


class BelföldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi"


class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi"
