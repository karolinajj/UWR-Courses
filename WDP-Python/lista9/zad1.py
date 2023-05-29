from turtle import *


def ramie(dl, kat):

    rt(-90)
    rt(kat)
    fd(dl)
    rt(180)
    fd(dl)
    rt(-kat)
    rt(-90)


def drzewo(n,dl):
    
    if n == 1:
        rt(-90)
        fd(dl)
        rt(90)
        ramie(dl, 20)
        ramie(dl, -20)
        rt(90)
        fd(dl)
        rt(-90)
        return 0

    rt(-90)
    fd(dl)
    rt(20)
    fd(dl)
    rt(20)
    rt(90)
    drzewo(n-1, 2 * (dl//3))
    rt(-90)
    rt(-20)
    rt(90)
    rt(-20)
    drzewo(n-1, 2 * (dl//3))
    rt(-90)
    rt(20)
    rt(180)
    fd(dl)
    rt(-20)
    rt(180)
    rt(-20)
    fd(dl)
    rt(20)
    rt(90)
    drzewo(n-1, 2 * (dl//3))
    rt(-90)
    rt(-20)
    rt(90)
    rt(-20)
    drzewo(n-1, 2 * (dl//3))
    rt(-90)
    rt(20)
    rt(180)
    fd(dl)
    rt(180)
    rt(20)
    rt(180)
    fd(dl)
    rt(-90)
    
tracer(0,0)

pendown()
drzewo(4,100)
update()
input()