from ucitavanje_koordinata import ucitaj_koordinate
from pravokutnik import provjeri_pravokutnik
from proracun_distance import distanca3D
from provjera_tacke import provjeri_tacku_x_3D
from prostorna_dijagonala import izracunaj_prostornu_dijagonalu
import math

def provjeri_kvadar(datoteka):
    """Funkcija prvo provjerava da li tacke A, B, C cine vrhove pravokutnika(baza kvadra),
       zatim provjerava duzine dijagonala stranica kvadra, tj. provjera da li su
       uglovi izmedju strana kvadra jednaki 90, sto znaci da je tacka D vrh kvadra.    
    """
     
    koordinate, _ = ucitaj_koordinate(datoteka)

    pravokutnik_abc = provjeri_pravokutnik(datoteka)

    
    """Provjera za tacku D, da li je vrh kvadra. Provjera se radi samo ako su tacke A, B, C
       vrhovi pravokutnika, tj. baze kvadra."""
    
    if pravokutnik_abc:
        tacke = koordinate[:4]
        
        ivica_ab = distanca3D(tacke[0], tacke[1])
        ivica_ac = distanca3D(tacke[0], tacke[2])
        ivica_ad = distanca3D(tacke[0], tacke[3])
        dijagonala_bd = distanca3D(tacke[1], tacke[3])
        dijagonala_cd = distanca3D(tacke[2], tacke[3])

        # Provjera pitagorine teoreme (pravog ugla obje strane kvadra)
        strana_kvadra_acd = math.isclose(ivica_ac**2 + ivica_ad**2, dijagonala_cd**2)
        strana_kvadra_abd = math.isclose(ivica_ab**2 + ivica_ad**2, dijagonala_bd**2)
        
        if strana_kvadra_acd and strana_kvadra_abd:
            print("Tacke A, B, C, D mogu biti vrhovi kvadra!")

            """Provjera da li se tacka X nalazi unutar kvadra i izracun prostorne dijagonale
               samo u slucaju da su A, B, C, D vrhovi kvadra."""
            print(provjeri_tacku_x_3D(datoteka))
            print(izracunaj_prostornu_dijagonalu(datoteka))
            
            
        else:
            print("Tacke A, B, C, D ne mogu biti vrhovi kvadra!")
            return False
    else:
        print("Tacke A, B, C, D ne mogu biti vrhovi kvadra!")
        return False
   
   