"""
 Autor : Jarek Ciolek-Zelechowski
 Problem Komiwojazera rozwiazany algorytmem aproksymacyjnym flooda
 http://www.asdpb.republika.pl/wyk8z2.pdf
"""

import copy
import time

INF = 0
ile = 0

def ap(macierz):
    return 1,2

# Obsluga menu
wybor = int(input('Wybieramy!\n\t1.Wpisuje z palca(do dopisania obsluga)\n\t2.Wczytam z pliku\nHmm?\n'))
if wybor == 1:
    tabWpisywanie = []
    wszystkieSubsety = [ ]
    krotkiPrzejscia = {}
    permutacje = [ ]
    Ilosc_Miast = int(input('Ilosc Miast = '))
    macierz = [[0 for i in range(Ilosc_Miast)] for j in range(Ilosc_Miast)]
    print('Koszty przejazdu? (Liczba i enter. Sam program rozkmini jak to leci)')
    for i in range(Ilosc_Miast):
        for j in range(Ilosc_Miast):
            macierz[i][j] = int(input())

    rozmiar = len(macierz)
    for i in range(rozmiar):
        macierz[i][i] = INF

    for i in range(Ilosc_Miast):
        tabWpisywanie.append(i)
elif wybor == 2:
    tabPlik = []
    wszystkieSubsety = []
    krotkiPrzejscia = {}
    permutacje = []
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

    macierz = [ map(int, x) for x in macierz ]

    rozmiar = len(macierz)
    for i in range(rozmiar):
        macierz[i][i] = INF
    for i in range(Ilosc_Miast):
        tabPlik.append(i)

# Drukiwanie zadanej na poczatku macierzy
print('Wypisanie:')
for i in range(rozmiar):
    print(macierz[ i ])

# Wypisanie wyniku
# Wraz z liczeniem czasu
print "\n"
start = time.clock()
droga, dyst = ap(macierz)
end = time.clock()
total = end - start
print "Najkrotsza droga: ", droga
print "Jej dlugosc: ", dyst
print("Czas pomiaru: {0:02f}s".format(total))
input()