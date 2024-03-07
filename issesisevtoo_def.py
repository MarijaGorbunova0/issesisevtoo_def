from modul import *
kasutajad = []
paroolid = []
menu = input(" registreerimine - 1\n autoriseerimine - 2\n nime või parooli muutmine - 3\n ")
if menu == 1:
    nimi = input("registreerimine: kirjutage oma nimi")
    parool = input("registreerimine: kirjutage parool")
    zaregistr = registr(nimi, parool, kasutajad, paroolid)
    print(kasutajad)    
elif menu == 2:
    autoris(kasutajad,paroolid)
    if nimi in polzovateli
    menu2 = int(input("1 - nime või parooli muutmine "))
