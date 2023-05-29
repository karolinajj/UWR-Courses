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
    
    kwadrat(x,y, bok, kolor)

  
tracer(0,0)
  
bok = 10
plik = open('niespodzianka.txt').readlines()

x = 0
y = 0 + 32

for wiersz in plik:

    lista_kolorow = wiersz.split(" ")
    x = 0 - 25
    
    for kolor in lista_kolorow:
        rysuj(kolor,x,y,bok)
        x += 1
    y -= 1

update()
input()