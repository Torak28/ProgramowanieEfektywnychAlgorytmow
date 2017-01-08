"""
 Autor : Jarek Ciolek-Zelechowski
 Problem Komiwojazera rozwiazany algorytmem Littla z ksiazki
 "An Algorithm For The TSP"(1963)
 https://goo.gl/am5JFf
 oraz z pomoca wykladu Prof. G. Srinivasan
 (https://www.youtube.com/watch?v=nN4K8xA8ShM)
"""


import time

INF = 1000000
nalepsza_cena = 0

def redukuj(rozmiar, macierz, wiersz, kolumna, wiersz_usuwany, kolumna_usuwana):
    redukcja = 0
    for i in range(rozmiar):
        temp = INF
        for j in range(rozmiar):
            temp = min(temp, macierz[wiersz[i]][kolumna[j]])
        if temp > 0:
            for j in range(rozmiar):
                if macierz[wiersz[i]][kolumna[j]] < INF:
                    macierz[wiersz[i]][kolumna[j]] -= temp
            redukcja += temp
        wiersz_usuwany[i] = temp
    for j in range(rozmiar):
        temp = INF
        for i in range(rozmiar):
            temp = min(temp, macierz[wiersz[i]][kolumna[j]])
        if temp > 0:
            for i in range(rozmiar):
                if macierz[wiersz[i]][kolumna[j]] < INF:
                    macierz[wiersz[i]][kolumna[j]] -= temp
            redukcja += temp
        kolumna_usuwana[j] = temp
    return redukcja


def nalepsza_krawedz(rozmiar, macierz, wiersz, kolumna):
    mosti = -INF
    xi = 0
    yi = 0
    for i in range(rozmiar):
        for j in range(rozmiar):
            if not macierz[wiersz[i]][kolumna[j]]:
                wiersz_min = INF
                zeroes = 0
                for k in range(rozmiar):
                    if not macierz[wiersz[i]][kolumna[k]]:
                        zeroes += 1
                    else:
                        wiersz_min = min(wiersz_min, macierz[wiersz[i]][kolumna[k]])
                if zeroes > 1:
                    wiersz_min = 0
                kolumna_min = INF
                zeroes = 0
                for k in range(rozmiar):
                    if not macierz[wiersz[k]][kolumna[j]]:
                        zeroes += 1
                    else:
                        kolumna_min = min(kolumna_min, macierz[wiersz[k]][kolumna[j]])
                if zeroes > 1:
                    kolumna_min = 0
                if wiersz_min + kolumna_min > mosti:
                    mosti = wiersz_min + kolumna_min
                    xi = i
                    yi = j
    return mosti, xi, yi


def przeszukaj(n, macierz, krawedzie, koszt, wiersz, kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl):
    global nalepsza_cena

    kolumna_usuwana = [0 for c in range(n)]
    wiersz_usuwany = [0 for c in range(n)]
    rozmiar = n - krawedzie
    koszt += redukuj(rozmiar, macierz, wiersz, kolumna, wiersz_usuwany, kolumna_usuwana)
    if koszt < nalepsza_cena:
        if krawedzie == n - 2:
            for i in range(n):
                najlepsza[i] = wskaznik_w_przod[i]
            if macierz[wiersz[0]][kolumna[0]] >= INF:
                omin = 0
            else:
                omin = 1
            najlepsza[wiersz[0]] = kolumna[1 - omin]
            najlepsza[wiersz[1]] = kolumna[omin]
            nalepsza_cena = koszt
        else:
            mostv, xv, yv = nalepsza_krawedz(rozmiar, macierz, wiersz, kolumna)
            LB = koszt + mostv
            wskaznik_w_przod[wiersz[xv]] = kolumna[yv]
            wskaznik_w_tyl[kolumna[yv]] = wiersz[xv]
            ostatni = kolumna[yv]
            while wskaznik_w_przod[ostatni] != INF:
                ostatni = wskaznik_w_przod[ostatni]
            pierwszy = wiersz[xv]
            while wskaznik_w_tyl[pierwszy] != INF:
                pierwszy = wskaznik_w_tyl[pierwszy]
            wartosc_kolumny_i_wiersza = macierz[ostatni][pierwszy]
            macierz[ostatni][pierwszy] = INF
            nowa_kolumna = [INF for _ in range(rozmiar)]
            nowy_wiersz = [INF for _ in range(rozmiar)]
            for i in range(xv):
                nowy_wiersz[i] = wiersz[i]
            for i in range(xv, rozmiar - 1):
                nowy_wiersz[i] = wiersz[i + 1]
            for i in range(yv):
                nowa_kolumna[i] = kolumna[i]
            for i in range(yv, rozmiar - 1):
                nowa_kolumna[i] = kolumna[i + 1]
            przeszukaj(n, macierz, krawedzie + 1, koszt, nowy_wiersz, nowa_kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl)
            macierz[ostatni][pierwszy] = wartosc_kolumny_i_wiersza
            wskaznik_w_tyl[kolumna[yv]] = INF
            wskaznik_w_przod[wiersz[xv]] = INF
            if LB < nalepsza_cena:
                macierz[wiersz[xv]][kolumna[yv]] = INF
                przeszukaj(n, macierz, krawedzie, koszt, wiersz, kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl)
                macierz[wiersz[xv]][kolumna[yv]] = 0

        for i in range(rozmiar):
            for j in range(rozmiar):
                macierz[wiersz[i]][kolumna[j]] = macierz[wiersz[i]][kolumna[j]] + wiersz_usuwany[i] + kolumna_usuwana[j]

def bb(macierz):
    global nalepsza_cena
    rozmiar = len(macierz)
    for i in range(rozmiar):
        macierz[i][i] = INF
    kolumna = [i for i in xrange(rozmiar)]
    wiersz = [i for i in xrange(rozmiar)]
    najlepsza = [0 for c in xrange(rozmiar)]
    droga = [0 for c in xrange(rozmiar)]
    wskaznik_w_przod = [INF for c in xrange(rozmiar)]
    wskaznik_w_tyl = [INF for c in xrange(rozmiar)]
    nalepsza_cena = INF

    przeszukaj(rozmiar, macierz, 0, 0, wiersz, kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl)

    index = 0
    for i in xrange(rozmiar):
        droga[i] = index
        index = najlepsza[index]
    index = []
    koszt = 0
    index.append(1)

    for i in xrange(rozmiar):
        if i != rozmiar - 1:
            src = droga[i]
            dst = droga[i + 1]
        else:
            src = droga[i]
            dst = 0
        koszt += macierz[src][dst]
        index.append(dst+1)
    return koszt, index


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
print('Wypisanie:')
for i in range(rozmiar):
    print(macierz[ i ])

# Wypisanie wyniku
print "\n"
start = time.clock()
droga, dyst = bb(macierz)
end = time.clock()
total = end - start
print "Najkrotsza droga: ", dyst
print "Jej dlugosc: ", droga
print("Czas pomiaru: {0:02f}s".format(total))