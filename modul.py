#1
from operator import index


def registr(nimi, parool, kasutajad:list, paroolid:list):
    """
    """
   if nimi in kasutajad:
       print("kirjutage uus nimi")
   else:
       kasutajad.append(nimi)
       paroolid.append(parool)
       return kasutajad,paroolid
#2
def autoris(kasutajad: list, paroolid: list, polzovateli):
    """
    """
    nimi = input("Kirjutage oma nimi: ")
    if nimi in kasutajad:
        nimiIndeks = kasutajad.index(nimi)
        parool = input("Kirjutage parool: ")
        if parool == paroolid[nimiIndeks]:
            print("Kõik on hästi")
            polzovateli.append(nimi)
            polzovateli.append(parool)
            return kasutajad, paroolid
        else:
            print("Vale parool")
            return kasutajad, paroolid
    else:
         print("Sulle vaja registreerida")   
         return kasutajad, paroolid
 #3 
 def uus_parool_nimi(polzovateli):
     zamena = input(int("kirjutage mida te tahate vahetada parol - 1, nimi - 2"))
     if zamena == 1:
         uusNimi = input("kirjutage uus nimi ")
         nimi == uusNimi
     elif zamena == 2: 
         uusParol = input("kirjutage uus parool ")
         parool == nimi
     

