# Autor : Jarek Ciolek-Zelechowski

import random

INF = -1

wybor = int(input('Wybieramy!\n\t1.Wpisuje z palca\n\t2.Losuje sobie sam\n\t3.Wczytam z pliku\nHmm?\n'))
if wybor == 1:
    Ilosc_Miast = int(input('Ilosc Miast = '))
    macierz = [[0 for i in range(Ilosc_Miast)] for j in range(Ilosc_Miast)]
    print('Koszty przejazdu? (Liczba i enter. Sam program rozkmini jak to leci)')
    for i in range(Ilosc_Miast):
        for j in range(Ilosc_Miast):
            # Wpisywanie z palca
            macierz[i][j] = int(input())

    rozmiar = len(macierz)
    for i in range(rozmiar):
        macierz[i][i] = INF
elif wybor == 2:
    Ilosc_Miast = int(input('Ilosc Miast = '))
    macierz = [[0 for i in range(Ilosc_Miast)] for j in range(Ilosc_Miast)]
    print("A zakres losowania?\n")
    a = int(input('Dolna granica = '))
    b = int(input('Gorna granica = '))
    for i in range(Ilosc_Miast):
        for j in range(Ilosc_Miast):
            # Losowanie z przedzialu
            macierz[i][j] = random.randint(a,b)

    rozmiar = len(macierz)
    for i in range(rozmiar):
        macierz[i][i] = INF
else:
    nazwa = raw_input('Jak sie nazywa pliczek? ')
    plik = open(nazwa)
    # Podzial pliku na liczby
    tab = [word for line in plik for word in line.split()]

    Ilosc_Miast = int(tab[0])
    macierz = [[0 for i in range(Ilosc_Miast)] for j in range(Ilosc_Miast)]

    # Usuniecie poczatku mowiacego o Ilosci miast
    tab.remove(tab[0])

    # Przepisanie tablicy liczb do macierzy
    pom = 0
    for i in range(Ilosc_Miast):
       for j in range(Ilosc_Miast):
            macierz[i][j] = tab[pom]
            pom += 1

    rozmiar = len(macierz)
    for i in range(rozmiar):
        macierz[i][i] = INF

# Drukiwanie dla obadania o co kaman
print('Wypisanie:')
for i in range(rozmiar):
   print(macierz[i])