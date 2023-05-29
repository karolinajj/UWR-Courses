from turtle import *
import random
from duze_cyfry import daj_cyfre

def move(x,y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(bok,kolor):
    pencolor('black')
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()


def cyfra(sx,sy,L):
    
    nowe = set()

    for i in range(5):
        for j in range(5):
            if L[i][j] == '#':
                nowe.add((sx + j,sy - i))

    return nowe


def rysuj():

    ILE_CYFR = 200
    WYMIARY = 40 #liczba kratek + 5
    PIKSELE = 20 #dl boku kratki
    kolory = ['green', 'blue', 'yellow', 'red', 'pink', 'purple', 'navy', 'magenta', 'orange']

    uzyte = set()

    for i in range(ILE_CYFR):
        sx = (random.randint(0,WYMIARY))
        sy = (random.randint(0,WYMIARY))
        
        n = random.randint(0,9)
        L = daj_cyfre(n)
        nowe = cyfra(sx,sy,L)

        if len(nowe & uzyte) == 0:
            kolor = random.choice(kolory)
            for x,y in nowe:
                move(PIKSELE*(x - WYMIARY//2),PIKSELE*(y - WYMIARY//2))
                kwadrat(PIKSELE, kolor)
                uzyte.add((x,y))


tracer(0,0)
rysuj()
update()

input()