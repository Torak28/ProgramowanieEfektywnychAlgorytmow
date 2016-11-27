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

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def nastepna_kolejnosc(tablica):
    kolejnoscOstateczny = []
    # Krok 1
    # https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
    maxX = -1;
    for i in range(0, tablica.__len__() - 1):
        if (tablica[ i ] < tablica[ i + 1 ]):
            maxX = i
    if (maxX == -1) :
        return [0, 1]
    #Krok 2
    maxY = -1
    for j in range(0, tablica.__len__()):
        if (tablica[ maxX ] < tablica[ j ]) :
            maxY = j
    #Krok 3
    swap(tablica, maxX, maxY)
    #Krok 4
    kolejnoscOstateczny = tablica[maxX + 1:]
    tablica = tablica[:maxX + 1]
    kolejnoscOstateczny.reverse()
    tablica = tablica + kolejnoscOstateczny
    return tablica



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
    tabPlik = nastepna_kolejnosc(tabPlik)
    print "Nowa trasa: " +str(tabPlik)
    print "dystans: " + str(PoliczDroge(tabPlik, macierz))
    tabPlik = nastepna_kolejnosc(tabPlik)
    print "Nowa trasa: " + str(tabPlik)
    print "dystans: " + str(PoliczDroge(tabPlik, macierz))
    tabPlik = nastepna_kolejnosc(tabPlik)
    print "Nowa trasa: " + str(tabPlik)
    print "dystans: " + str(PoliczDroge(tabPlik, macierz))
    tabPlik = nastepna_kolejnosc(tabPlik)
    print "Nowa trasa: " + str(tabPlik)
    print "dystans: " + str(PoliczDroge(tabPlik, macierz))

# TODO:
# * Przeglad zupelny

# Drukiwanie dla obadania o co kaman
    print('Wypisanie:')
    for i in range(rozmiar):
        print(macierz[ i ])