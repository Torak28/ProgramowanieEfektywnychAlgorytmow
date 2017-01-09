"""
 Autor : Jarek Ciolek-Zelechowski
 Problem Komiwojazera rozwiazany algorytmem dynamicznym Helda-Karpa
 przy pomocy wykladu Tushar'a Roy'a
 https://www.youtube.com/watch?v=-JjA4BLQyqE
"""

import copy
import time

INF = -1
ile = 0

# Funkcja dla zadanej tablicy drogi generuje pary
# Np. dla drogi = [1,2,3]
# Wygeneruje wynik = [[1,2],[2,3]]
# Potrzebne przy obliczaniu Dlugosci Drogi
def generujPary(tablica):
    wynik = []
    for i in range(tablica.__len__()-1):
        wynik.extend([ [ tablica[ i ], tablica[ i+1 ] ] ])
    return wynik

# Dla przyjetej tablicy drogi i zadanej macierzy przejscia
# wylicza i zwraca dlugosc drogi
def dlugoscDrogi(tablica, macierz):
    sum = 0
    pary = generujPary(tablica)
    for i in range(pary.__len__()):
        miastoAIndex = pary[i][0] - 1
        miastoBIndex = pary[ i ][ 1 ] - 1
        sum = sum + macierz[miastoAIndex][miastoBIndex]
    return sum

# Dla zadanej pary danych: cel i przejscie
# generuje minimalny koszt przejscia
# i np dla [3, {1,2}] jest to idea
# przejscia z 0 przez droge {1,2} do
# celu jakim jest 3
# Funkcja zwraca indeks w tablicy z policzonym kosztem
# Lub sama dopisuje sie do tablicy i podaje swoj
# dopisany indeks
def minimum(cel, przejscie):
    if (cel, przejscie) in krotkiPrzejscia:
        return krotkiPrzejscia[cel, przejscie]
    wartosci = []
    wszystkieMinima = []
    for j in przejscie:
        przegladanySet = copy.deepcopy(list(przejscie))
        przegladanySet.remove(j)
        wszystkieMinima.append([j, tuple(przegladanySet)])
        result = minimum(j, tuple(przegladanySet))
        wartosci.append(macierz[cel-1][j-1] + result)
    krotkiPrzejscia[cel, przejscie] = min(wartosci)
    permutacje.append(((cel, przejscie), wszystkieMinima[wartosci.index(krotkiPrzejscia[cel, przejscie])]))
    return krotkiPrzejscia[cel, przejscie]

# Rozwiazanie problemu poprzez stworzenie tablicy
# kosztow w linijce minimum(1, dane)
# A nastepnie przegladanie jej w celu
# znalezienia najepszego rozwiazania
def dp(macierz):
    dane = []
    for i in range(Ilosc_Miast):
        if i != 0:
            dane.append(i+1)
    dane = tuple(dane)
    for x in range(1, Ilosc_Miast):
        krotkiPrzejscia[x + 1, ()] = macierz[x][0]
    minimum(1, dane)
    droga = []
    droga.append(1)
    rozwiazanie = permutacje.pop()
    droga.append(rozwiazanie[1][0])
    for x in range(Ilosc_Miast - 2):
        for noweRozwiazanie in permutacje:
            if tuple(rozwiazanie[ 1 ]) == noweRozwiazanie[ 0 ]:
                rozwiazanie = noweRozwiazanie
                droga.append(rozwiazanie[1][0])
                break
    droga.append(1)
    return droga, dlugoscDrogi(droga, macierz)

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
droga, dyst = dp(macierz)
end = time.clock()
total = end - start
print "Najkrotsza droga: ", droga
print "Jej dlugosc: ", dyst
print("Czas pomiaru: {0:02f}s".format(total))