from ucitavanje_koordinata import ucitaj_koordinate

def provjeri_tacku_x_2D(datoteka):
    """Funkcija provjerava da li se tacka X nalazi unutar pravokutnika
       kojeg cine tacke A, B, C. To radi na nacin da prvo pronadje minimalne i
       maksimalne koordinate za x i y tacaka A, B, C, a zatim provjerava
       uslov, da su i x i y koordinata tacke X unutar tih granica."""
    
    koordinate, _ = ucitaj_koordinate(datoteka)
    tacke_abc = koordinate[:3]   # lista sa koordinatama tacaka A, B, C
    tacka_x = koordinate[-1]     # koordinate tacke X

    # Odredjivanje minimalne i maksimalne koordinate za x i y tacaka A, B, C
    min_x = min(tacka[0] for tacka in tacke_abc)
    max_x = max(tacka[0] for tacka in tacke_abc)
    min_y = min(tacka[1] for tacka in tacke_abc)
    max_y = max(tacka[1] for tacka in tacke_abc)

    if  min_x < tacka_x[0] < max_x and min_y < tacka_x[1] < max_y:
        return True
    else:
        return False



def provjeri_tacku_x_3D(datoteka):
    """Funkcija provjerava da li se tacka X nalazi unutar kvadra ABCD.
       Potrebno je prvo provjeriti da li su x i y koordinata tacke X
       unutar granica ravni pravokutnika ABC, a zatim i unutar granica [min, max] 
       koordinate z tacke D.
    """
    koordinate, _ = ucitaj_koordinate(datoteka)

    # Min i Max vrijednost z-koordinate tacaka A, B, C, D
    koordinate_z_abcd = [tacke[2] for tacke in koordinate[:4]]
    min_z_abcd = min(koordinate_z_abcd)
    max_z_abcd = max(koordinate_z_abcd)
    
    # z-koordinata tacke X
    koordinata_z_x = koordinate[4][2]
    
    # Provjera da li se tacka X nalazi unutar granica ravni pravokutnika ABC
    tacka_x_3d = provjeri_tacku_x_2D(datoteka)
     
    # Dalja provjera se vrsi samo ako se tacka X nalazi unutar ravni pravokutnika
    if tacka_x_3d:
        # provjera da li je z koordinata tacke X unutar granica [min, max] z-koordinata A, B, C, D
        if min_z_abcd < koordinata_z_x < max_z_abcd:
            return f"Tacka X se nalazi unutar kvadra ABCD!"
        else:
            return f"Tacka X se ne nalazi unutar kvadra ABCD!"
    else:
        return f"Tacka X se ne nalazi unutar kvadra ABCD!"
