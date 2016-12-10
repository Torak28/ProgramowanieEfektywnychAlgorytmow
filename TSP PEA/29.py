# Autor : Jarek Ciolek-Zelechowski

import random
import itertools

INF = -1
ile = 0

#Macierz to tablica zawierajaca
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

# Kolejnosc Leksykograficzna(Raczej niepotrzebna)
def nastepna_kolejnosc(tablica):
    global ile
    ile += 1
    kolejnoscOstateczny = []
    # Krok 1
    # https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
    maxX = -1;
    for i in range(0, tablica.__len__() - 1):
        if (tablica[ i ] < tablica[ i + 1 ]):
            maxX = i
    if (maxX == -1) :
        return 0
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

def silnia(n):
    if (n == 1):
        return 1
    else:
        return n * silnia(n - 1)

def iloscDrog(n):
    if (n == 1):
        return 1
    else:
        return (n-1) * iloscDrog(n-1) + 1

def iloscLisci(n):
    if n == 1:
        return 1
    else:
        return (n-1) * iloscLisci(n-1)

def generujGraf(n):
    x = iloscDrog(n)
    tab = [ ]
    for i in range(x):
        tab.append(i + 1)
    return tab

def generujPary(tablica):
    wynik = []
    for i in range(tablica.__len__()-1):
        wynik.extend([ [ tablica[ i ], tablica[ i+1 ] ] ])
    return wynik

# def Negacja(macierz, tablica):

def redukcjaWierszy(macierz):
    sum = 0
    for i in range(rozmiar):
        min = 2147483647
        for j in range(rozmiar):
            if(macierz[i][j] != INF and macierz[i][j] < min):
                min = macierz[i][j]
        sum = sum + min
        for k in range(rozmiar):
            if(macierz[i][k] != INF and macierz[i][k] != 0):
                macierz[i][k] = macierz[i][k] - int(min)
    return macierz, sum

def redukcjaKolumn(macierz):
    sum = 0
    for i in range(rozmiar):
        min = 2147483647
        for j in range(rozmiar):
            if(macierz[j][i] != INF and macierz[j][i] < min):
                min = macierz[j][i]
        sum = sum + min
        for k in range(rozmiar):
            if(macierz[k][i] != INF and macierz[k][i] != 0):
                macierz[k][i] = macierz[k][i] - int(min)
    return macierz, sum

def redukcja(macierz):
    LB = 0
    macierz, sum1 = redukcjaWierszy(macierz)
    macierz, sum2 = redukcjaKolumn(macierz)
    LB = sum1 + sum2
    return macierz, LB

def kombinacjeDrog(n):
    tablica = []
    for i in range(n):
        tablica.append(i+1)
    wynik = []
    for L in range(0, len(tablica) + 1):
        for subset in itertools.permutations(tablica, L):
            subset = list(subset)
            if subset != []:
                if subset[0] == 1:
                    subset = [subset]
                    wynik.extend(subset)
    return wynik

wybor = int(input('Wybieramy!\n\t1.Wpisuje z palca(do dopisania obsluga)\n\t2.Wczytam z pliku\nHmm?\n'))
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

    macierz = [ map(int, x) for x in macierz ]

    rozmiar = len(macierz)
    for i in range(rozmiar):
        macierz[i][i] = INF
    for i in range(Ilosc_Miast):
        tabPlik.append(i)
    iloscMozliwosci = silnia(Ilosc_Miast)
    nalepszaTrasa = []
    najkrotszyDystans = 2147483647
    dychaW = 0
    while tabPlik != 0:
        tabPlik.append(tabPlik[0])
        d = PoliczDroge(tabPlik, macierz)
        if(d < najkrotszyDystans):
            nalepszaTrasa = tabPlik
            najkrotszyDystans = PoliczDroge(tabPlik, macierz)
        tabPlik = tabPlik[:tabPlik.__len__()-1]
        tabPlik = nastepna_kolejnosc(tabPlik)
        procent = 100 * ile/float(iloscMozliwosci)
        if procent > dychaW:
            print "|",
            dychaW += 10
    print ""
    print "Najlepsza trasa: " +str(nalepszaTrasa)
    print "dystans: " + str(PoliczDroge(nalepszaTrasa, macierz))

# TODO:
# * ograniczyc przeszukania jako ze pierwszy i tak jest zawsze 0(zrobic to zalezne od wywolania funkcji tak zeby mozna bylo nadal liczyc buteforca), Napewno?!
# * Nie potrzebny if == 1, albo go pozmieniac tak zeby sypal dobre wyniki
# * Dodaj INF w macierzy dla zadanej tablicy drogi
# * Liscie to taki niby zapis przejscia

# Drukiwanie dla obadania o co kaman
print('Wypisanie:')
for i in range(rozmiar):
    print(macierz[ i ])

#Test
macierz, sum = redukcja(macierz)
print macierz
print sum

t = [1,4,3]
e = generujPary(t)
print e

print "\n"
# Wiersz, Kolumna
print macierz[0][2]