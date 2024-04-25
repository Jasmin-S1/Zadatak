from ucitavanje_koordinata import ucitaj_koordinate
from pravokutnik import provjeri_pravokutnik
from kvadar import provjeri_kvadar

def main():
    datoteka = input("Unesite ime datoteke: ")

    _, broj_dimenzija = ucitaj_koordinate(datoteka)
    
    """Provjera da li tacke imaju 2D ili 3D koordinate, i nakon toga pozivanje 
       pripadajucih funkcija"""
    
    if broj_dimenzija == 2:
        provjeri_pravokutnik(datoteka)
    elif broj_dimenzija == 3: 
        provjeri_kvadar(datoteka)

    
if __name__ == "__main__":
    main()