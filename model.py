import random

wys = 100
szer = 100
lista = [0]*wys
nowa_lista = [0]*wys

for i in range(wys):
    lista[i] = [0]*szer
    nowa_lista[i]=[0]*szer


def losuj(lista, szer, wys):
    for i in range(wys):
        for j in range(szer):
            lista[i][j] = random.randint(0,1)


def policz_sasiadow(lista, i, j):
    global wys, szer
    licznik_sasiadow = 0
    if i-1 >=0:
        if j - 1 >= 0:
            licznik_sasiadow = licznik_sasiadow + lista[i-1][j-1]
        if j >=0:
            licznik_sasiadow = licznik_sasiadow + lista[i-1][j]
        if j +1 < szer:
            licznik_sasiadow = licznik_sasiadow +lista[i-1][j+1]
    if j - 1 >= 0:
        licznik_sasiadow = licznik_sasiadow + lista[i][j-1]
    if j+1 < szer:
        licznik_sasiadow = licznik_sasiadow + lista[i][j+1]
    if i+1 < wys:
        if j-1 >= 0:
            licznik_sasiadow = licznik_sasiadow + lista[i+1][j-1]
        licznik_sasiadow = licznik_sasiadow + lista[i+1][j]
        if j+1 < szer:
            licznik_sasiadow = licznik_sasiadow + lista[i+1][j+1]
    return licznik_sasiadow

def nastepne_pokolenie():
    global lista, nowa_lista, wys, szer
    for i in range(wys):
        for j in range(szer):
            liczba_sasiadow = policz_sasiadow(lista, i, j)
            if (lista[i][j] == 1 and (liczba_sasiadow == 2 or liczba_sasiadow == 3)):
                nowa_lista[i][j] = 1
            elif (lista[i][j] == 0 and liczba_sasiadow == 3):
                nowa_lista[i][j] = 1
            else:
                nowa_lista[i][j] = 0
    tymczasowa = lista
    lista = nowa_lista
    nowa_lista = tymczasowa
    print(nowa_lista, lista)
    return lista

def wczytaj_wzorzec(wzorzec, odstep_x = 0, odstep_y = 0):
    global lista
    for i in range(wys):
        for j in range(szer):
            lista[i][j] = 0
    j = odstep_y

    for rzad in wzorzec:
        i = odstep_x
        for wartosc in rzad:
            lista[i][j] = wartosc
            i = i+1
        j=j+1

    
wzorzec_szybowiec = [[0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 0, 1, 0],
                     [0, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0]]

wzorzec_dzialo_szybowiec = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



if __name__ == '__main__':
    nastepne_pokolenie()









                
            
