from turtle import *
import random

pensize(4)
speed('fastest')


def move(x, y):
    pu()
    goto(x, y)
    pd()


def square(x, y, bok):
    move(x, y)
    for i in range(4):
        fd(bok)
        rt(90)

def paint():
    tmp = 5
    k = 2
    for i in range(10):
        square(-10*i - k*tmp ,10*i + k*tmp,30+20*i + 2*k*tmp)
        tmp += k*i
    input("zakoncz")

paint()