import math

def distanca2D(tacka1, tacka2):
   """Funkcija racuna udaljenost izmedju 2 tacke 
      u 2D koordinatnom sistemu"""
   return math.sqrt((tacka1[0] - tacka2[0])**2 + 
                    (tacka1[1] - tacka2[1])**2)


def distanca3D(tacka1, tacka2):
   """Funkcija racuna udaljenost izmedju 2 tacke 
      u 3D koordinatnom sistemu"""
   return math.sqrt((tacka1[0] - tacka2[0])**2 + 
                    (tacka1[1] - tacka2[1])**2 + 
                    (tacka1[2] - tacka2[2])**2)