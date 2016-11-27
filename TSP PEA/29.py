# Autor : Jarek Ciolek-Zelechowski

import random

INF = -1

def PoliczDroge(tablica, macierz):
    sum = 0
    for i in range(0,tablica.__len__() - 1):
        miastoAIndex = tablica[i]
        miastoBIndex = tablica[i + 1]
        sum += int(macierz[miastoAIndex][miastoBIndex])
    return sum

wybor = int(input('Wybieramy!\n\t1.Wpisuje z palca\n\t2.Wczytam z pliku\nHmm?\n'))
if wybor == 1:
    tabWpisywanie = []
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

    for i in range(Ilosc_Miast):
        tabWpisywanie.append(i)
elif wybor == 2:
    tabPlik = []
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
    for i in range(Ilosc_Miast):
        tabPlik.append(i)
    print "trasa: " + str(tabPlik)
    print "dystans: " + str(PoliczDroge(tabPlik, macierz))


# TODO:
# * Dopisanie porzadku leksykograficznego

# Drukiwanie dla obadania o co kaman
    print('Wypisanie:')
    for i in range(rozmiar):
        print(macierz[ i ])