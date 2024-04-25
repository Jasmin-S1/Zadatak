from ucitavanje_koordinata import ucitaj_koordinate
from proracun_distance import distanca2D
from provjera_tacke import provjeri_tacku_x_2D
import math


def provjeri_pravokutnik(datoteka):
   """Funkcija provjera da li za stranice vazi pitagorina teorema, a ako 
      vazi onda tacke A, B, C mogu biti vrhovi pravokutnika, zatim vrsi provjeru
      da li se tacka X nalazi unutar pravokutnika te proracun dijagonale 
      pravokutnika"""
   
   koordinate, broj_dimenzija = ucitaj_koordinate(datoteka)


   """Provjera pravokutnika kada imamo kvadar, tada se ekstraktuju samo 2d koordinate
      za provjeru pravokutnika"""
   if broj_dimenzija == 3:
      tacke_abc_3d = koordinate[:3]
      tacke_abc_2d = [koordinate_xy[:2] for koordinate_xy in tacke_abc_3d]
      koordinate = tacke_abc_2d
      return koordinate

   tacke = koordinate[:3]

   ab = distanca2D(tacke[0], tacke[1])
   bc = distanca2D(tacke[1], tacke[2])
   ac = distanca2D(tacke[0], tacke[2])
   distance = [ab, bc, ac]
   distance.sort()

   # Provjera pitagorine teoreme
   vrhovi_pravokutnika = math.isclose(distance[0]**2 + distance[1]**2, distance[2]**2)

   if not vrhovi_pravokutnika:
      print("Tacke A, B, C ne mogu biti vrhovi pravokutnika!")
      return False
   
   else: 
      print("Tacke A, B, C mogu biti vrhovi pravokutnika!")

      # Provjera da li se tacka X nalazi unutar pravokutnika
      tacka_x_pripada = provjeri_tacku_x_2D(datoteka)
      if tacka_x_pripada:
         print("Tacka X se nalazi unutar pravokutnika ABC!")
      else:
         print("Tacka X nije unutar pravokutnika ABC!")
      

      # Proracun dijagonale pravokutnika
      """Obzirom da za provjeru pravokutnika koristimo pitagorinu teoremu,
         to znaci da je najduza stranica zapravo dijagonala pravokutnika.
         Posto je vec izracunata, ovdje cemo samo koristiti "max" funkciju nad 
         listom "distance".
         """
      dijagonala_pravokutnika = max(distance)

      print("Dijagonala pravokutnika iznosi: ", round(dijagonala_pravokutnika, 2))
      
   

