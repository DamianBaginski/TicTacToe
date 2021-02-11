#!/usr/bin/env python
# coding: utf-8

# In[5]:


def plansza():
    """Stworzenie planszy do gry"""
    print('|' + pozycja[0] + '|' + pozycja[1] + '|' + pozycja[2] +'|') 
    print('-------')
    print('|' + pozycja[3] + '|' + pozycja[4] + '|' + pozycja[5] +'|')
    print('-------')
    print('|' + pozycja[6] + '|' + pozycja[7] + '|' + pozycja[8] +'|')
    print('-------')

def wpisanie(pozycja_nr, zajety):
    """Proces dopasowywania wybranego znaku do miejsca na planszy pamiętając o sprawdzeniu czy dane miejsce jest już zajęte"""
    a = int(input('Wpisz pozycje: '))
    if a < 1 or a > 9:
        print('Nie ma takiej pozycji')
    if zajety[a - 1] == False:
        if stage % 2 == 1:
            pozycja_nr[a - 1] = 'o'
            zajety[a - 1] = True
        elif stage % 2 == 0:
            pozycja_nr[a - 1] = 'x'
            zajety[a - 1] = True
        return pozycja_nr, zajety
    else:
        print('Nie da rady byczku')
    
def check_win(win, gdzie_wartosci):
    """Sprawdzenie wygranej"""
    for i in win:
        if all(j in gdzie_wartosci for j in i) == True:
            if stage % 2 == 0:
                print('Wygranko x')
                plansza()
                raise SystemExit(0)
            elif stage % 2 == 1:
                print('Wygranko o')
                plansza()
                raise SystemExit(0)
    plansza()

def indeksy_o(pozycja_nr, indeksy):
    """Pobranie indeksow, na ktorych miejscach stoja 'o'"""
    for index in range(len(pozycja_nr)):
        value=pozycja_nr[index]
        if value == 'o':
            indeksy.append(index)

def indeksy_x(pozycja_nr, indeksy):
    """Pobranie indeksow, na ktorych miejscach stoja 'x'"""
    for index in range(len(pozycja_nr)):
        value=pozycja_nr[index]
        if value == 'x':
            indeksy.append(index)

pas=[] #lista, do ktorej beda wpisywane odpowiednio indeksy o lub x; oprozniana gdy brak zwyciestwa
pozycja = ['1','2','3','4','5','6','7','8','9'] #numery, na ktore mozna wpisac o lub x
stage = 0 #zwieksza sie z kolejnymi ruchami graczy
wygransko = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #pozycje wygrywajace na planszy dla tych samych znakow
zajetosc = [False, False, False, False, False, False, False, False, False] #sprawdza czy zajete miejsce na planszy

while stage <= 4: #dla pierwszych 4 ruchow nie sprawdza zwyciestwa, nie ma mozliwosci, zeby wygrac
    stage+=1
    plansza()
    wpisanie(pozycja,zajetosc)
indeksy_o(pozycja, pas)
check_win(wygransko, pas)
pas.clear()

while stage <= 8:
    stage+=1
    wpisanie(pozycja, zajetosc)
    if stage % 2 == 1:
        indeksy_o(pozycja, pas)
    elif stage % 2 == 0:
        indeksy_x(pozycja, pas)
    check_win(wygransko, pas)
    pas.clear()
    
print('REMIS')

raise SystemExit(0)


# In[ ]:




