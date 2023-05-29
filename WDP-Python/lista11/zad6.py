from turtle import pendown
import turtle
from turtle import *

def move(x, y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(x,y,bok,kolor):
    begin_fill()
    fillcolor(kolor)
    move(x,y)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()


def rysunek(n,bok,x,y,k):
    if n == 0:
        kwadrat(x,y,bok,kolor[k])
    else:
        rt(30)
        kwadrat(x,y,bok,kolor[k])
        rysunek(n-1,bok/2,x + bok/4, y + bok/2,k+1) #góra
        rysunek(n-1,bok/2,x - bok/2, y - bok/4,k+1) #lewy
        rysunek(n-1,bok/2,x + bok, y - bok/4,k+1)
        rysunek(n-1,bok/2,x + bok/4, y - bok,k+1)



turtle.tracer(0)
kolor = ['black', 'blue', 'green', 'yellow', 'red', 'gold', 'purple']
rt(30)
rysunek(4,100,10,10,0)
input()