# Autor : Jarek Ciolek-Zelechowski
# Problem Komiwojazera rozwiazany algorytmem Littla z ksiazki
# "An Algorithm For The TSP"(1963)
# oraz z pomoca wykladu Prof. G. Srinivasan
# (https://www.youtube.com/watch?v=nN4K8xA8ShM)


import time

inf = 10000000
nalepsza_cena = 0

def redukuj(rozmiar, matrix, wiersz, kolumna, wiersz_usuwany, kolumna_usuwana):
    rvalue = 0
    for i in range(rozmiar):
        temp = inf
        for j in range(rozmiar):
            temp = min(temp, matrix[wiersz[i]][kolumna[j]])
        if temp > 0:
            for j in range(rozmiar):
                if matrix[wiersz[i]][kolumna[j]] < inf:
                    matrix[wiersz[i]][kolumna[j]] -= temp
            rvalue += temp
        wiersz_usuwany[i] = temp
    for j in range(rozmiar):
        temp = inf
        for i in range(rozmiar):
            temp = min(temp, matrix[wiersz[i]][kolumna[j]])
        if temp > 0:
            for i in range(rozmiar):
                if matrix[wiersz[i]][kolumna[j]] < inf:
                    matrix[wiersz[i]][kolumna[j]] -= temp
            rvalue += temp
        kolumna_usuwana[j] = temp
    return rvalue


def nalepsza_krawedz(rozmiar, matrix, wiersz, kolumna):
    mosti = -inf
    xi = 0
    yi = 0
    for i in range(rozmiar):
        for j in range(rozmiar):
            if not matrix[wiersz[i]][kolumna[j]]:
                wiersz_min = inf
                zeroes = 0
                for k in range(rozmiar):
                    if not matrix[wiersz[i]][kolumna[k]]:
                        zeroes += 1
                    else:
                        wiersz_min = min(wiersz_min, matrix[wiersz[i]][kolumna[k]])
                if zeroes > 1:
                    wiersz_min = 0
                kolumna_min = inf
                zeroes = 0
                for k in range(rozmiar):
                    if not matrix[wiersz[k]][kolumna[j]]:
                        zeroes += 1
                    else:
                        kolumna_min = min(kolumna_min, matrix[wiersz[k]][kolumna[j]])
                if zeroes > 1:
                    kolumna_min = 0
                if wiersz_min + kolumna_min > mosti:
                    mosti = wiersz_min + kolumna_min
                    xi = i
                    yi = j
    return mosti, xi, yi


def przeszukaj(n, matrix, krawedzie, koszt, wiersz, kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl):
    global nalepsza_cena

    kolumna_usuwana = [0 for c in range(n)]
    wiersz_usuwany = [0 for c in range(n)]
    rozmiar = n - krawedzie
    koszt += redukuj(rozmiar, matrix, wiersz, kolumna, wiersz_usuwany, kolumna_usuwana)
    if koszt < nalepsza_cena:
        if krawedzie == n - 2:
            for i in range(n): 
                najlepsza[i] = wskaznik_w_przod[i]
            if matrix[wiersz[0]][kolumna[0]] >= inf:
                omin = 0
            else:
                omin = 1
            najlepsza[wiersz[0]] = kolumna[1 - omin]
            najlepsza[wiersz[1]] = kolumna[omin]
            nalepsza_cena = koszt
        else:
            mostv, xv, yv = nalepsza_krawedz(rozmiar, matrix, wiersz, kolumna)
            LB = koszt + mostv
            wskaznik_w_przod[wiersz[xv]] = kolumna[yv]
            wskaznik_w_tyl[kolumna[yv]] = wiersz[xv]
            ostatni = kolumna[yv]
            while wskaznik_w_przod[ostatni] != inf:
                ostatni = wskaznik_w_przod[ostatni]
            pierwszy = wiersz[xv]
            while wskaznik_w_tyl[pierwszy] != inf:
                pierwszy = wskaznik_w_tyl[pierwszy]
            wartosc_kolumny_i_wiersza = matrix[ostatni][pierwszy]
            matrix[ostatni][pierwszy] = inf
            nowa_kolumna = [inf for _ in range(rozmiar)]
            nowy_wiersz = [inf for _ in range(rozmiar)]
            for i in range(xv):
                nowy_wiersz[i] = wiersz[i]
            for i in range(xv, rozmiar - 1):
                nowy_wiersz[i] = wiersz[i + 1]
            for i in range(yv):
                nowa_kolumna[i] = kolumna[i]
            for i in range(yv, rozmiar - 1):
                nowa_kolumna[i] = kolumna[i + 1]
            przeszukaj(n, matrix, krawedzie + 1, koszt, nowy_wiersz, nowa_kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl)
            matrix[ostatni][pierwszy] = wartosc_kolumny_i_wiersza
            wskaznik_w_tyl[kolumna[yv]] = inf
            wskaznik_w_przod[wiersz[xv]] = inf
            if LB < nalepsza_cena:
                matrix[wiersz[xv]][kolumna[yv]] = inf
                przeszukaj(n, matrix, krawedzie, koszt, wiersz, kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl)
                matrix[wiersz[xv]][kolumna[yv]] = 0

        for i in range(rozmiar):
            for j in range(rozmiar):
                matrix[wiersz[i]][kolumna[j]] = matrix[wiersz[i]][kolumna[j]] + wiersz_usuwany[i] + kolumna_usuwana[j]

#  code for branch & bound
def bb(matrix):
    global nalepsza_cena
    rozmiar = len(matrix)
    for i in range(rozmiar):
        matrix[i][i] = inf
    print('Macierz przejscia:')
    for i in range(rozmiar):
        print(matrix[i])
    kolumna = [i for i in xrange(rozmiar)]
    wiersz = [i for i in xrange(rozmiar)]
    najlepsza = [0 for c in xrange(rozmiar)]
    droga = [0 for c in xrange(rozmiar)]
    wskaznik_w_przod = [inf for c in xrange(rozmiar)]
    wskaznik_w_tyl = [inf for c in xrange(rozmiar)]
    nalepsza_cena = inf

    przeszukaj(rozmiar, matrix, 0, 0, wiersz, kolumna, najlepsza, wskaznik_w_przod, wskaznik_w_tyl)

    index = 0
    for i in xrange(rozmiar):
        droga[i] = index
        index = najlepsza[index]
    index = []
    koszt = 0

    for i in xrange(rozmiar):
        if i != rozmiar - 1:
            src = droga[i]
            dst = droga[i + 1]
        else:
            src = droga[i]
            dst = 0
        koszt += matrix[src][dst]
        index.append([src, dst])
    return koszt, index


# Program
n = int(input('Ilosc Miast = '))
a = [[0 for i in range(n)]for j in range(n)]
print('Koszty przejazdu? (Liczba i enter. Sam program rozkmini jak to leci)')
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

czas_start = time.time()
koszt, droga = bb(a)
print "Koszt = ", koszt
print "Droga = ", droga
print "Czas (s) = ", time.time() - czas_start