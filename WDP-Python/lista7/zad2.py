import random
from turtle import *
import numpy as np


def move(x, y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(x, y, bok, kolor):
    move(x, y)
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()   
    
def rysuj(piksel, x,y,bok):
    
    kolor = []
    for e in eval(piksel):
        kolor.append(e/256)

    x *= bok
    y *= bok
    
    kwadrat(x - 300,y + 300, bok, kolor)



def losowo(x,y,L):
    
    uzyte = set()
    ile_narysowano = 0

    while(ile_narysowano < x*y):
        new_y = random.randint(0,62)
        new_x = random.randint(0,51)
        
        kolor = L[new_y][new_x]
        
        if(new_x,new_y) not in uzyte:
            uzyte.add((new_x,new_y))
            rysuj(kolor,new_x,-new_y,bok)
            ile_narysowano += 1

        


speed = 'fastest'
#tracer(0,0)
x = 0
y = 0
bok = 10
plik = open('niespodzianka.txt').readlines()
L = []

for wiersz in plik:
    lista_kolorow = wiersz.split(" ")
    L.append(lista_kolorow)
    
    for kolor in lista_kolorow:
        #print(kolor)
        #rysuj(kolor,x,y,bok)
        x += 1
    y += 1


losowo(int(x/y),y,L)


#update()
input()