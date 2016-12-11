# Autor : Jarek Ciolek-Zelechowski

import copy
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

def generujPunkty(tablica):
    wynik = [ ]
    for i in range(1, tablica.__len__()):
        wynik.extend([ [ tablica[ 0 ], tablica[ i ] ] ])
    return wynik

def negacjaTablicy(m, tablica):
    wiersz = tablica[0] - 1
    kolumna = tablica[1] - 1
    for j in range(rozmiar):
        m[wiersz][j] = INF
        m[j][kolumna] = INF
    return m

def negacjaPunktu(m, tablica):
    wiersz = tablica[ 0 ] - 1
    kolumna = tablica[ 1 ] - 1
    m[kolumna][wiersz] = INF
    return m

def negacja(m,tablica):
    pary = generujPary(tablica)
    punkty = generujPunkty(tablica)
    for i in range(tablica.__len__() - 1):
        negacjaTablicy(m,pary[i])
        negacjaPunktu(m,punkty[i])
    return m

def redukcjaWierszy(macierz):
    sum = 0
    for i in range(rozmiar):
        min = 2147483647
        for j in range(rozmiar):
            if(macierz[i][j] != INF and macierz[i][j] < min):
                min = macierz[i][j]
        if min != 2147483647:
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
        if min != 2147483647:
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

def kombinacjeDrog(n, wielkosc):
    tablica = []
    for i in range(n):
        tablica.append(i+1)
    wynik = []
    for L in range(0, len(tablica) + 1):
        for subset in itertools.permutations(tablica, L):
            if subset.__len__() == wielkosc:
                subset = list(subset)
                if subset[0] == 1:
                    subset = [subset]
                    wynik.extend(subset)
    return wynik

def kombinacjeKonkretnychDrog(n, wielkosc,posiada):
    len = posiada.__len__()
    tablica = []
    for i in range(n):
        tablica.append(i+1)
    wynik = []
    for L in range(0, tablica.__len__() + 1):
        for subset in itertools.permutations(tablica, L):
            if subset.__len__() == wielkosc:
                subset = list(subset)
                i = 1
                if subset[0] == 1 and subset[i] == posiada[i]:
                    subset = [subset]
                    wynik.extend(subset)
                    i = i + 1
    return wynik

def kombinacjeWielkosciKonkretnychDrog(n, wielkosc):
    tablica = []
    for i in range(n):
        tablica.append(i+1)
    wynik = []
    for L in range(0, tablica.__len__() + 1):
        for subset in itertools.permutations(tablica, L):
            if subset.__len__() == wielkosc:
                subset = list(subset)
                if subset[0] == 1:
                    subset = [subset]
                    wynik.extend(subset)
    return wynik

def liczLB(macierzPierwotna, macierz, LBprev, tablica):
    A = macierzPierwotna[tablica[0]-1][tablica[1]-1]
    macierz, r = redukcja(macierz)
    return LBprev + A + r, macierz

def bbPoziom(pom, wielkosc, najkrotszaDroga, macierzPierwotna):
    pom = pom
    tabPrzejscia = []
    wielkosc = wielkosc
    minLB = 2147483647
    macierz, LBMACIERZY = redukcja(macierzPierwotna)
    if pom == 0:
        tabPrzejscia.extend(kombinacjeWielkosciKonkretnychDrog(Ilosc_Miast,wielkosc))
    else:
        najkrotszaDroga = copy.deepcopy(najkrotszaDroga)
        tabPrzejscia.extend(kombinacjeKonkretnychDrog(Ilosc_Miast,wielkosc,najkrotszaDroga))
    for i in range(tabPrzejscia.__len__()):
        m = copy.deepcopy(macierz)
        droga = tabPrzejscia[i]
        negacja(m,droga)
        noweLB, m = liczLB(macierz,m,LBMACIERZY,droga)
        deltaLB = noweLB - LBMACIERZY
        if(deltaLB < minLB):
            minLB = deltaLB
            najkrotszaDroga = droga
    return najkrotszaDroga, m

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
# * Liscie to taki niby zapis przejscia
# * przerwanie kmbinacji w zaleznosci od wilkosci permutacji(zeby nie genreowac wszystkiego)

# Drukiwanie dla obadania o co kaman
print('Wypisanie:')
for i in range(rozmiar):
    print(macierz[ i ])

#Test
# macierz, LBMACIERZY = redukcja(macierz)
# LB = LBMACIERZY
# print macierz
# print LB
# LB = 3
# print LBMACIERZY
# print LB
# t = [1,4,3]z
# m = copy.deepcopy(macierz)
# negacja(m,t)
# print macierz
# print m
# x = liczLB(macierz,m,LBMACIERZY,[4,3])
# print x
# print m
# print macierz
print "\n"
# macierz to zawsze wstepniak z ktory podajemy do liczenia LB
# m bedziemy wykorzystywac

droga,m = bbPoziom(1,3,[1,4],macierz)
print droga
print m