from tkinter import *
import model

wielkosc_komorki = 5

uruchomiony = False

def ustawienia():
    global wielkosc_komorki, okno_glowne, start, wyczysc, widok_siatki, opcja, wybor
    okno_glowne = Tk()
    okno_glowne.title('Gra w życie')
    start = Button(okno_glowne, text = 'Start', width = 12)
    start.bind('<Button-1>', handler_start)
    start.grid(row = 1, column = 0, sticky =W, padx=20, pady=20)
    wyczysc = Button(okno_glowne, text='Wyczyść', width = 12)
    wyczysc.bind('<Button-1>', handler_wyczysc)
    wyczysc.grid(row = 1, column =2, sticky =E, padx=20, pady=20)
    widok_siatki = Canvas(okno_glowne, width = model.szer*wielkosc_komorki, height = model.wys*wielkosc_komorki, borderwidth = 0, highlightthickness = 0, bg = 'white')
    widok_siatki.bind('<Button-1>', handler_widok_siatki)
    widok_siatki.grid(row = 0, columnspan = 3, padx=20, pady=20)
    wybor = StringVar(okno_glowne)
    wybor.set('Wybierz wzorzec')
    opcja = OptionMenu(okno_glowne, wybor, 'Wybierz wzorzec', 'szybowiec', 'działo/szybowiec', 'losowy', command = handler_opcji)
    opcja.config(width = 20)
    opcja.grid(row=1, column=1, padx=20)



def handler_start(zdarzenie):
    global start, uruchomiony
    if uruchomiony:
        uruchomiony = False
        start.configure(text='Start')
    else:
        uruchomiony = True
        start.configure(text='Pauza')
        aktualizacja()
        
def handler_wyczysc(zdarzenie):
    global widok_siatki, wyczysc, uruchomiony
    if uruchomiony:
        uruchomiony = False
        start.configure(text='Start')
    for i in range(model.wys):
        for j in range(model.szer):
            model.lista[i][j] = 0
    aktualizacja()

def handler_widok_siatki(zdarzenie):
    global wielkosc_komorki
    x = int(zdarzenie.x/wielkosc_komorki)
    y = int(zdarzenie.y/wielkosc_komorki)
    if model.lista[x][y] == 1:
        model.lista[x][y] = 0
        narysuj_komorke(x, y, 'white')
    elif model.lista[x][y] == 0:
        model.lista[x][y] = 1
        narysuj_komorke(x,y,'black')

def handler_opcji(zdarzenie):
    global wybor, uruchomiony, start
    uruchomiony = False
    start.configure(text = "Start")
    wzor = wybor.get()
    if wzor == 'szybowiec':
        model.wczytaj_wzorzec(model.wzorzec_szybowiec, 10, 10)
    elif wzor == 'działo/szybowiec':
        model.wczytaj_wzorzec(model.wzorzec_dzialo_szybowiec, 10, 10)
    elif wzor == 'losowy':
        model.losuj(model.lista, model.szer, model.wys)
    aktualizacja()

def aktualizacja():
    global widok_siatki, okno_glowne, uruchomiony
    widok_siatki.delete(ALL)
    model.nastepne_pokolenie()
    for i in range(model.wys):
        for j in range(model.szer):
            if model.lista[i][j] == 1:
                narysuj_komorke(i, j, 'black')
    if uruchomiony:
        okno_glowne.after(1000, aktualizacja)
                

def narysuj_komorke(i,j,kolor):
    global widok_siatki, wielkosc_komorki
    if kolor == 'black':
        outline = 'grey'
    else:
        outline = 'white'
    widok_siatki.create_rectangle(i*wielkosc_komorki, j*wielkosc_komorki, i*wielkosc_komorki+wielkosc_komorki, j*wielkosc_komorki+wielkosc_komorki, fill=kolor, outline=outline)


if __name__ == '__main__':
    ustawienia()
    model.losuj(model.lista, model.szer, model.wys)
    aktualizacja()
    mainloop()  
    

