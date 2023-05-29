
####################################
# Program:  dziennik.py
####################################

from collections import defaultdict as dd

przedmiot = 'nieznany'


dziennik = dd(lambda : dd(list))
# dziennik = dd(lambda : dd(lambda: []))  # To samo, co powyżej


for x in open('dziennik.txt'):
    if x[0] == '#':
        continue
    L = x.split()
    if len(L) < 2:
        continue
        
    if L[0].lower() == 'przedmiot:':
        przedmiot = ' '.join(L[1:])
    else:
        if len(L) != 3: continue
        osoba = L[0] + ' ' + L[1]
        oceny = [int(n) for n in L[2].split(',')]
            
        dziennik[przedmiot][osoba] += oceny    
        
osoby = {o for p in dziennik for o in dziennik[p]}

for o in osoby:
    print ('UCZEŃ:', o)
    for p in dziennik:
        oceny = dziennik[p][o]
        if oceny:
            print ('   ',p, *oceny, 'ŚREDNIA=', sum(oceny) / len(oceny))
        #else:
        #    print ('   ', p, 'BRAK OCEN') 
    print ()        


####################################
# Program:  dziennik.py
####################################

przedmiot = 'nieznany'

dziennik = {}

for x in open('dziennik.txt'):
    if x[0] == '#':
        continue
    L = x.split()
    if len(L) < 2:
        continue
        
    if L[0].lower() == 'przedmiot:':
        przedmiot = ' '.join(L[1:])
    else:
        if len(L) != 3: continue
        osoba = L[0] + ' ' + L[1]
        oceny = [int(n) for n in L[2].split(',')]
        
        if przedmiot not in dziennik:
            dziennik[przedmiot] = {}
        
        if osoba not in dziennik[przedmiot]:
            dziennik[przedmiot][osoba] = []
            
        dziennik[przedmiot][osoba] += oceny    
        

for p in dziennik:
    print ('PRZEDMIOT:', p)
    for osoba in dziennik[p]:
        print ('   ', osoba, *dziennik[p][osoba])
    print ()   
    

#################################################
# kwadrat.py
#################################################
                                 
from turtle import *

BOK = 15
SX = -100
SY = 0

def kwadrat(x, y, kolor):
    fillcolor(kolor)
    pu()
    goto(SX + x * BOK, SY + y * BOK)
    pd()
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill() 

tracer(0,1)
print ('Zmienna __name__ =', __name__)    

if __name__ == '__main__':
    speed('fastest')    
    kolory = ['red', 'green', 'blue']
        
    for i in range(10):
        kwadrat(i,i, kolory[i % 3])    

    
    input()    


####################################
# Program:  zycie.py
####################################

from kwadrat import kwadrat
from turtle import update, clear
import random
import sys
import time


txt = """
......................
......................
..............###.....
......................
......................
..............##......
..............##......
..###.................
....#.................
...#...........##.....
......................
"""

txt = """
......................
...............###....
..............##......
..............##......
......................
...............###....
..............##......
..............##......
......................
......................
......................
....###...............
......#...............
.....#................
......................
......................
..###.................
....#.................
...#...........##.....
......................
"""


tab = [list(wiersz) for wiersz in txt.split()]
tab.reverse()

MY = len(tab)
MX = len(tab[0])

def rysuj_plansze(tab):
    clear()
    for y in range(MY):
        for x in range(MX):
            if tab[y][x] == '#':
                kolor = 'green'
            else:
                kolor = 'lightgreen'
            kwadrat(x, y, kolor)
            
            
    update() 
    
rysuj_plansze(tab)


KIERUNKI = [ (1,0), (0,1), (-1, 0), (0, -1), (1,1), (-1,1), (1,-1), (-1,-1)]

def liczba_sasiadow(x, y):
    ls = 0  
    for dx, dy in KIERUNKI:
        nx = (x + dx) % MX
        ny = (y + dy) % MY
        if tab[ny][nx] == '#':
            ls += 1
    return ls
   
def pusta_plansza():
    return [ MX * ['.']  for y in range(MY)]
            
# reguły gry w życie:
# jeżeli komórka pełna ma 2 lub 3 sąsiadów przeżywa, wpp ginie
# jeżeli komórka pusta ma 3 sąsiadów, to rodzi się nowa
#
#

historia = set()

while True:
    
    
    rysuj_plansze(tab)
    nowa = pusta_plansza()
    
    for x in range(MX):
        for y in range(MY):
            ls = liczba_sasiadow(x, y)
            if tab[y][x] == '.' and ls == 3:
                nowa[y][x] = '#'
            if tab[y][x] == '#' and ls in [2,3]:
                nowa[y][x] = '#'
    
    if tab == nowa:
        break                
    tab = nowa  
    time.sleep(0.03)         
    
print ('Koniec')
input()

