"""
 Autor : Jarek Ciolek-Zelechowski
 Problem Komiwojazera rozwiazany algorytmem aproksymacyjnym flooda
 http://www.asdpb.republika.pl/wyk8z2.pdf
"""

import copy
import time

INF = 0
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

def generujMozliwosci(tablica, elem):
    wynikCalosci = []
    for i in range(1, len(tablica)):
        wynikCzesc = copy.deepcopy(tablica)
        wynikCzesc.insert(i,elem)
        wynikCalosci.append(wynikCzesc)
    return wynikCalosci

def wybierzWiercholek(dist):
    return dist.index(max(dist)) + 1

def wybierzNajlepsze(macierzWyniku):
    minDr = 2147483647
    wynik = []
    for i in range(len(macierzWyniku)):
        if(dlugoscDrogi(macierzWyniku[i],macierz) < minDr):
            minDr = dlugoscDrogi(macierzWyniku[i],macierz)
            wynik.append(macierzWyniku[i])
    return wynik[-1]

def aktualizujDist(wierzcholek, dist):
    dist[wierzcholek-1] = 0
    for i in range(len(dist)):
        if dist[i] == 0:
            dist[i] = 0
        else:
            if macierz[0][i] < macierz[wierzcholek-1][i]:
                dist[i] = macierz[0][i]
            else:
                dist[i] = macierz[wierzcholek-1][i]
    return dist

def ap(macierz):
    dist = []
    koszt = 0
    droga = [1,1]
    for i in range(Ilosc_Miast):
        dist.append(macierz[0][i])
    """
    Teoretyczna petla for
    TODO:
    aktalizacja dist
    liczenie kosztu
    Tablica do odwiedzenia(teoretycznie dist to zalatwi, we will see)
    Teortycnie liczenie odlegolosci jest bez sensu
    """
    for i in range(Ilosc_Miast-1):
        droga = wybierzNajlepsze(generujMozliwosci(droga, wybierzWiercholek(dist)))
        aktualizujDist(wybierzWiercholek(dist),dist)
    return droga, dlugoscDrogi(droga,macierz)

# Obsluga menu
pliczki = ["tsp4.txt", "tsp6_1.txt", "tsp6_2.txt", "tsp10.txt", "tsp12.txt", "tsp13.txt", "tsp14.txt", "tsp15.txt", "17.txt", "29.txt", "52.txt", "120.txt"]
for i in range(len(pliczki)):
    wybor = 2#int(input('Wybieramy!\n\t1.Wpisuje z palca(do dopisania obsluga)\n\t2.Wczytam z pliku\nHmm?\n'))
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
        nazwa = pliczki[i]#raw_input('Jak sie nazywa pliczek? ')
        print pliczki[i]
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
#print('Wypisanie:')
#for i in range(rozmiar):
#    print(macierz[ i ])

# Wypisanie wyniku
# Wraz z liczeniem czasu
    print "------------"
    start = time.clock()
    droga, dyst = ap(macierz)
    end = time.clock()
    total = end - start
    print "Najkrotsza droga: ", droga
    print "Jej dlugosc: ", dyst
    print("Czas pomiaru: {0:02f}s".format(total))
    print "------------"