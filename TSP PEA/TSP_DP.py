# Autor : Jarek Ciolek-Zelechowski

import copy
import itertools
import time

INF = -1
ile = 0

def dp(macierz):
    dane = []
    for i in range(Ilosc_Miast):
        dane.append(i+1)
    print len(dane) #rowne Ilosc_Miast
    
def minimum(celDrogi ,sciezkaPrzejscia):
    if (celDrogi ,sciezkaPrzejscia) in krotkiPrzejscia:
        return krotkiPrzejscia[celDrogi ,sciezkaPrzejscia]
    wartosci = [ ]
    minimalnePrzejscie = [ ]
    for j in sciezkaPrzejscia:
        przejscie = copy.deepcopy(list(sciezkaPrzejscia))
        przejscie.remove(j)
        minimalnePrzejscie.append([ j, tuple(przejscie) ])
        wynik = minimum(j, tuple(przejscie))
        wartosci.append(macierz[ celDrogi - 1 ][ j - 1 ] + wynik)

    # get minimun value from set as optimal solution for
    krotkiPrzejscia[ celDrogi, sciezkaPrzejscia ] = min(wartosci)
    permutacje.append(((celDrogi, sciezkaPrzejscia), minimalnePrzejscie[ wartosci.index(krotkiPrzejscia[ celDrogi, sciezkaPrzejscia ]) ]))

    return krotkiPrzejscia[ celDrogi, sciezkaPrzejscia ]
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
print "\n"
start = time.clock()
# droga,dyst = dp(macierz)
dp(macierz)
end = time.clock()
total = end - start
print "Najkrotsza droga: ", #droga
print "Jej dlugosc: ", #dyst
print("Czas pomiaru: {0:02f}s".format(total))