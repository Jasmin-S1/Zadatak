from ucitavanje_koordinata import ucitaj_koordinate
from proracun_distance import distanca3D

def izracunaj_prostornu_dijagonalu(datoteka):
    """Funkcija racuna prostornu dijagonalu kvadra ABCD. Za proracun su potrebne koordinate 
       dva suprotna vrha kvadra. U ovoj funkciji se koristi vrh A i njemu suprotan vrh. Koordinate 
       suprotnog vrha vrhu A se mogu dobiti iz koordinata vrhova B, C, D, a to su maksimalne 
       vrijednosti koordinata x, y, z.
       """
    koordinate, _ = ucitaj_koordinate(datoteka)
    tacke_bcd = koordinate[1:4]

    # Koordinate x, y, z suprotnog vrha kvadra
    koordinata_x = max(tacke[0] for tacke in tacke_bcd)
    koordinata_y = max(tacke[1] for tacke in tacke_bcd)
    koordinata_z = max(tacke[2] for tacke in tacke_bcd)

    suprotni_vrh = [koordinata_x, koordinata_y, koordinata_z]
    prostorna_dijagonala = distanca3D(koordinate[0], suprotni_vrh)
    return f"Prostorna dijagonala kvadra iznosi: {round(prostorna_dijagonala, 2)}"