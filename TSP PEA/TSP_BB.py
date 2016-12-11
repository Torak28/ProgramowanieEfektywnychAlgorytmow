# Autor : Jarek Ciolek-Zelechowski

import copy
import itertools
import time

INF = -1
ile = 0

def dlugoscDrogi(tablica, macierz):
    sum = 0
    pary = generujPary(tablica)
    for i in range(pary.__len__()):
        miastoAIndex = pary[i][0] - 1
        miastoBIndex = pary[i][1] - 1
        sum = sum + macierz[miastoAIndex][miastoBIndex]
    return sum

def iloscPoziomow(Ilosc_Miast):
    return Ilosc_Miast-1

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

def test(tabliceDoSprawdzenia, tabliceSprawdzajaca):
    pom = 0
    for i in range(tabliceDoSprawdzenia.__len__()):
        if tabliceSprawdzajaca[i] == tabliceDoSprawdzenia[i]:
            pom = pom + 1
        else:
            pom = pom + 0
    if pom == tabliceDoSprawdzenia.__len__():
        return 1
    else:
        return 0

# def kombinacjeKonkretnychDrog(n, wielkosc,posiada):
#     print Ilo
#     len = posiada.__len__()
#     tablica = []
#     for i in range(n):
#         tablica.append(i+1)
#     wynik = []
#     for L in range(0, tablica.__len__() + 1):
#         for subset in itertools.permutations(tablica, L):
#             if subset.__len__() == wielkosc and subset[0] == 1:
#                 if test(posiada,subset) == 1:
#                     subset = list(subset)
#                     subset = [subset]
#                     wynik.extend(subset)
#             else:
#                 break
#     print wynik
#     return wynik

def kombinacjeKonkretnychDrog(n, wielkosc,posiada):
    wynik = []
    posiada.append(100)
    for i in range(Ilosc_Miast - wielkosc + 2):
        posiada[-1] = i+2
        if posiada[-1] != posiada[-2]:
            wynik.extend([list(posiada)])
    print wynik
    print "---"
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

def liczLB(macierzPierwotna,LBprev, droga):
    pary = generujPary(droga)
    A = macierzPierwotna[pary[-1][0]-1][pary[-1][1]-1]
    macierzPierwotna = negacja(macierzPierwotna,droga)
    macierzPierwotna,r = redukcja(macierzPierwotna)
    return LBprev + A + r, r , macierzPierwotna

def bbPoziom(pom, wielkosc, najkrotszaDroga, macierzPierwotna, LBpop, macierzPoprzednia, macierzDoDrogi):
    tabPrzejscia = []
    minLB = 2147483647
    if pom == 0:
        a, r = redukcja(macierzPierwotna)
        tabPrzejscia.extend(kombinacjeWielkosciKonkretnychDrog(Ilosc_Miast,wielkosc))
    else:
        a, r = redukcja(macierz)
        najkrotszaDroga = copy.deepcopy(najkrotszaDroga)
        tabPrzejscia.extend(kombinacjeKonkretnychDrog(Ilosc_Miast,wielkosc,najkrotszaDroga))
    for i in range(tabPrzejscia.__len__()):
        m = copy.deepcopy(a)
        droga = tabPrzejscia[i]
        if pom == 0:
            noweLB,niepotrzebnazmienna,m = liczLB(m,r,droga)
        else:
            noweLB,niepotrzebnazmienna,m = liczLB(m,LBpop,droga)
        deltaLB = noweLB - LBpop
        if(deltaLB < minLB):
            minLB = deltaLB
            najkrotszaDroga = droga
        if najkrotszaDroga.__len__() == Ilosc_Miast:
            najkrotszaDroga.append(1)
    return najkrotszaDroga, m, dlugoscDrogi(najkrotszaDroga,macierzDoDrogi), minLB, m

def bb(macierzPierwotna):
    macierzDoDrogi = copy.deepcopy(macierzPierwotna)
    droga, m, odleglosc, lb, mp = bbPoziom(0, 2, [  ], macierzPierwotna, 0, 0, macierzDoDrogi)
    aktaulnieNajkrotszaDroga = droga
    LBpop = lb
    macirzPoprzednia = mp
    for i in range(iloscPoziomow(Ilosc_Miast)-1):
        droga, m, odleglosc, lb, mp = bbPoziom(1,3+i,aktaulnieNajkrotszaDroga,macierzPierwotna, LBpop, macirzPoprzednia,macierzDoDrogi)
        aktaulnieNajkrotszaDroga = droga
        LBpop = lb
        macirzPoprzednia = mp
    return aktaulnieNajkrotszaDroga, odleglosc


wybor = int(input('Wybieramy!\n\t1.Wpisuje z palca(do dopisania obsluga)\n\t2.Wczytam z pliku\nHmm?\n'))
if wybor == 1:
    tabWpisywanie = []
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

# TODO:
# * ograniczyc przeszukania jako ze pierwszy i tak jest zawsze 0(zrobic to zalezne od wywolania funkcji tak zeby mozna bylo nadal liczyc buteforca), Napewno?!
# * przerwanie kmbinacji w zaleznosci od wilkosci permutacji(zeby nie genreowac wszystkiego)

# Drukiwanie dla obadania o co kaman
print('Wypisanie:')
for i in range(rozmiar):
    print(macierz[ i ])




print "\n"
start = time.clock()
droga,dyst = bb(macierz)
end = time.clock()
total = end - start
print "Najkrotsza droga: ", droga
print "Jej dlugosc: ", dyst
print("Czas pomiaru: {0:02f}s".format(total))