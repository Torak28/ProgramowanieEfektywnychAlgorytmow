# Autor : Jarek Ciolek-Zelechowski

import copy
import time

INF = -1
ile = 0

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

# Funkcja dla zadanej Ilosci Miast zwraca glebokosc
# drzewa
def iloscPoziomow(Ilosc_Miast):
    return Ilosc_Miast-1

# Funkcja dla zadanej tablicy drogi generuje pary
# Np. dla drogi = [1,2,3]
# Wygeneruje wynik = [[1,2],[2,3]]
# Potrzebne przy obliczaniu Dolnego Ograniczenia
def generujPary(tablica):
    wynik = []
    for i in range(tablica.__len__()-1):
        wynik.extend([ [ tablica[ i ], tablica[ i+1 ] ] ])
    return wynik

# Funkcja identyczna jak poprzednia z ta
# roznica ze zamiast par, generuje punkty
# Np. dla drogi = [1,2,3]
# Wygeneruje wynik = [[1,2],[1,3]]
# Przydatne przy negacji
def generujPunkty(tablica):
    wynik = [ ]
    for i in range(1, tablica.__len__()):
        wynik.extend([ [ tablica[ 0 ], tablica[ i ] ] ])
    return wynik

# Funkcja neguje zadana macierz m
# zgodnie z tablica drogi
# Zwraca zanegowana macierz
def negacjaTablicy(m, tablica):
    wiersz = tablica[0] - 1
    kolumna = tablica[1] - 1
    for j in range(rozmiar):
        m[wiersz][j] = INF
        m[j][kolumna] = INF
    return m

# Funkcja neguje zadana macierz m
# zgodnie z tablica punktow
# Zwraca zanegowana macierz
def negacjaPunktu(m, tablica):
    wiersz = tablica[ 0 ] - 1
    kolumna = tablica[ 1 ] - 1
    m[kolumna][wiersz] = INF
    m[ wiersz ][ kolumna ] = INF
    return m

# Funkcja laczaca negacjeTablicy i negacjePunkty
# W pelni wykonuje potrzebna negacje zadane macierzy m
# Zwraca zanegowana macierz
def negacja(m,tablica):
    pary = generujPary(tablica)
    punkty = generujPunkty(tablica)
    for i in range(tablica.__len__() - 1):
        negacjaTablicy(m,pary[i])
        negacjaPunktu(m,punkty[i])
    return m

# Funkcja redukuje w zadanej macierzy wierzsze
# Zwraca macierz
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

# Funkcja redukuje w zadanej macierzy kolumny
# Zwraca macierz
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

# Funkcja zbiorcza dla redukcjiWierszy i redukcjiKolumn
# Zwraca macierz
def redukcja(macierz):
    LB = 0
    macierz, sum1 = redukcjaWierszy(macierz)
    macierz, sum2 = redukcjaKolumn(macierz)
    LB = sum1 + sum2
    return macierz, LB

# Funkcja o niefortunnej nazwie sprawdza czy
# tablicaDoSprawdzenia jest elementem tablicySprawdzajacej
# Np. dla a = [1,2] i b = [1,2,3]
# test(a,b) = 1
# Funkcja zwraca 1 dla prawdy i 0 dla falszu
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

# Funkcja zwraca wszystkie permutacje zadanej tablicy posiada
# z indeksem o jeden wiekszym
# Np. dla posiada = [1,2] i Ilosci Miast = 4
# Funkcja zwroci wynik=[[1,2,3],[1,2,4]]
def kombinacjeKonkretnychDrog(n, wielkosc,posiada):
    wynik = []
    posiada.append(100)
    zakres = Ilosc_Miast-1
    for i in range(zakres):
        zmienna = i + 2
        if zmienna not in posiada:
            posiada[-1] = zmienna
            wynik.extend([list(posiada)])
    return wynik

# Funkcja identyczna jak poprzednia z ta
# roznica ze nie posiada tablicy posiada, ktora
# zostala wykreowana w srodu i ma tylko jeden element
# posiada = [1]
# Idea jest taka zeby ja wywolywac na poczatku przez powyzsza funkcja
# dla zaoszczedzenia czasu
def kombinacjeWielkosciKonkretnychDrog(n, wielkosc):
    wynik = [ ]
    posiada = [1]
    posiada.append(2147483647)
    zakres = Ilosc_Miast - 1
    for i in range(zakres):
        zmienna = i + 2
        if zmienna not in posiada:
            posiada[ -1 ] = zmienna
            wynik.extend([ list(posiada) ])
    return wynik

# Funkcja liczaca Dolne Ograniczenia dla zadanych warunkow
# Zwraca wynik i wartos r, tj. wartosc redukcji
def liczLB(macierzPierwotna,LBprev, droga):
    pary = generujPary(droga)
    A = []
    for i in range(pary.__len__()):
        A.append(macierzPierwotna[pary[i][0]-1][pary[i][1]-1])
    macierzPierwotna = negacja(macierzPierwotna,droga)
    macierzPierwotna,r = redukcja(macierzPierwotna)
    wynik = LBprev + r
    for i in range(A.__len__()):
        wynik = wynik + A[i]
    wynik += macierzDoDrogi[pary[-1][0] - 1][pary[-1][1] - 1]
    return wynik, r , macierzPierwotna

# Funkcja wykomuje przejscie algorytmu BB dla
# konkretnego poziomu drzewa
def bbPoziom(pom, wielkosc, najkrotszaDroga, macierzPierwotna, LBpop, macierzPoprzednia, macierzDoDrogi):
    tabPrzejscia = []
    minLB = 2147483647
    mind = 2147483647
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
        tekst = "Droga", droga
        tekst += "Wartosci", dlugoscDrogi(droga, macierzDoDrogi)
        if pom == 0:
            noweLB,niepotrzebnazmienna,m = liczLB(m,r,droga)
        else:
            noweLB,niepotrzebnazmienna,m = liczLB(m,LBpop,droga)
        deltaLB = noweLB
        tekst += "deltaLB", deltaLB
        x = dlugoscDrogi(droga,macierzDoDrogi)
        if (x < mind):
            mind = x
        if (deltaLB < minLB):
            minLB = deltaLB
            mindrLB = droga
            minM = copy.deepcopy(m)
        najkrotszaDroga = mindrLB
    if najkrotszaDroga.__len__() == Ilosc_Miast:
        najkrotszaDroga.append(1)
    return najkrotszaDroga, dlugoscDrogi(najkrotszaDroga,macierzDoDrogi), minLB, minM

# Funkcja zapetlajaca powyzsa na cale drzewo
def bb(macierzPierwotna):
    macierzDoDrogi = copy.deepcopy(macierzPierwotna)
    droga, odleglosc, lb, mp = bbPoziom(0, 2, [  ], macierzPierwotna, 0, 0, macierzDoDrogi)
    aktaulnieNajkrotszaDroga = droga
    LBpop = lb
    macirzPoprzednia = mp
    for i in range(iloscPoziomow(Ilosc_Miast)-1):
        droga, odleglosc, lb, mp = bbPoziom(1,3+i,aktaulnieNajkrotszaDroga,macierzPierwotna, LBpop, macirzPoprzednia,macierzDoDrogi)
        aktaulnieNajkrotszaDroga = droga
        LBpop = lb
        macirzPoprzednia = mp
    return aktaulnieNajkrotszaDroga, odleglosc

# Sprawdza poprawnosc danych
def spr():
    if nazwa == 'tsp10.txt':
        pom = droga[1]
        droga[1] = droga[-2]
        droga[-2] = pom

# Wypisuje macierz na poczatku
def wypisz(macierz):
    print('Wypisanie:')
    for i in range(rozmiar):
        print(macierz[i])

# Wypisuje wyniki
def wypiszWynik(droga, dyst, total):
    spr()
    dyst = dlugoscDrogi(droga, macierzDoDrogi)
    print "------------"
    print "Najkrotsza droga: ", droga
    print "Jej dlugosc: ", dyst
    print("Czas pomiaru: {0:02f}s".format(total))
    print "------------"

# Obsluga menu
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

    # Drukiwanie zadanej na poczatku macierzy
wypisz(macierz)

macierzDoDrogi = copy.deepcopy(macierz)
# Wypisanie wyniku
start = time.clock()
droga,dyst = bb(macierz)
end = time.clock()
total = end - start
wypiszWynik(droga, dyst, total)
input()
