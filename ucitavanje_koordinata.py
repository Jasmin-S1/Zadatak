def ucitaj_koordinate(datoteka):
    """
    Funkcija sluzi za ucitavanje txt fajla sa koordinatama, a nakon
    toga vrsi ekstrakciju koordinata kao integer-e i pohranjuje 
    ih u listu "koordinate". Funkcija takodjer ima implementirane except-e 
    ukoliko navedena datoteka nije pronadjena ili ako se jednostavno desi neka 
    druga greska prilikom ucitavanja koordinata.
    """
    try:
        with open(datoteka, 'r') as fajl:
            linije_datoteke = fajl.readlines()
            koordinate = [list(map(int, linija.strip().split(','))) for linija in linije_datoteke]
            broj_dimenzija = len(koordinate[0])
            return koordinate, broj_dimenzija
        
    except FileNotFoundError:
        print("Datoteka nije pronadjena!")
        return None
    
    except Exception as e:
        print("Greska prilikom ucitavanja datoteke:", e)
        return None
