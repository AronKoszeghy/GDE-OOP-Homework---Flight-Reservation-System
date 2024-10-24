from LegiTarsasag import LegiTarsasag
from FoglalasiRendszer import FoglalasiRendszer
from Jarat import BelföldiJarat, NemzetkoziJarat

tarsasag = LegiTarsasag("Példa Légitársaság")

jarat1 = BelföldiJarat("ABC100", "Budapest", 10000)
jarat2 = BelföldiJarat("ABC101", "Szombathely", 9000)
jarat3 = NemzetkoziJarat("ABC102", "Stockholm", 50000)

tarsasag.add_jarat(jarat1)
tarsasag.add_jarat(jarat2)
tarsasag.add_jarat(jarat3)

rendszer = FoglalasiRendszer()

foglalas1 = rendszer.jegy_foglalasa(jarat1, "Törpapa")
foglalas2 = rendszer.jegy_foglalasa(jarat2, "Törpilla")
foglalas3 = rendszer.jegy_foglalasa(jarat3, "Törperős")
foglalas4 = rendszer.jegy_foglalasa(jarat1, "Törpicur")
foglalas5 = rendszer.jegy_foglalasa(jarat2, "Ügyifogyi")
foglalas6 = rendszer.jegy_foglalasa(jarat3, "Hókuszpók")

while True:
    print("\nElérhető műveletek:")
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("\nAdja meg a választott művelet számát: ")

    if valasztas == "1":
        utas_nev = input("Adja meg az utas nevét: ")
        tarsasag.list_jaratok()
        jaratszam = input("Adja meg a járatszámot: ")

        jarat = next((j for j in tarsasag.jaratok if j.jaratszam == jaratszam), None)

        if jarat is not None:
            foglalas = rendszer.jegy_foglalasa(jarat, utas_nev)
            print(f"Sikeres foglalás: {foglalas}")
        else:
            print("Hibás járatszám!")

    elif valasztas == "2":
        utas_nev = input("Adja meg az utas nevét: ")

        foglalas = next((f for f in rendszer.foglalasok if f.utas_nev == utas_nev), None)

        if foglalas is not None:
            rendszer.foglalas_lemondasa(foglalas)
            print("Foglalás sikeresen törölve!")
        else:
            print("Nem található a foglalás.")

    elif valasztas == "3":
        rendszer.list_foglalasok()

    elif valasztas == "4":
        break

    else:
        print("Érvénytelen választás!")
