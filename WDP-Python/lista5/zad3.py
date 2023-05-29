from turtle import *
import random
from duze_cyfry import daj_cyfre

def move(x,y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(bok,kolor):
    pencolor(kolor)
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()


def cyfra(L,poz, ile_cyfr):
    bok = 20
    tmp = int(-ile_cyfr/2 * 5 * bok) #przesunięcie rysunku w lewo
    kolor = [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)]


    for i in range(5):
        for j in range(5):
            if L[i][j] == '#':
                x = bok*j + 5*bok*poz + poz*bok + tmp #musimy dodać trzeci składnik, żeby była przerwa między cyframi
                y = -bok*i
                move(x,y) 
                kwadrat(bok,kolor)


def rysuj(n):
    n_napis = str(n)
    for i in range(len(str(n))):
        L = daj_cyfre(int(n_napis[i]))
        cyfra(L,i, len(str(n)))


n = int(input("Podaj n: "))
speed('fastest')
rysuj(n)
input()