import random
from turtle import *

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

def srednia(x,y, N, L):
    tmp = 1
    wynik = L[x][y]
    wspolrzedne = [[-1,-1],[-1,0], [0,-1], [0,1], [1,0], [1,1], [-1,1], [1,-1]]
    
    for sx,sy in wspolrzedne:
        
        if x + sx < N and y + sy < N and x + sx >= 0 and y + sy >= 0:
            wynik += L[x + sx][y + sy]*(1.2)
            tmp +=1
    return wynik/(tmp-1)
  
def id_kolory(L,N,dl):
    
    for i in range(N):
        for j in range(N):
            L[i][j] = min( int(L[i][j] / (1.2/dl)), 5)
    return L

def mapa(L,N):
    kolory =  ['green', (0.5, 1, 0) , 'yellow', 'orange', 'red', (0.5, 0,0) ]
    wzgorza = 20
    bok = 10
    
    for i in range(wzgorza):
        x = random.randint(0,N-1)
        y = random.randint(0,N-1)
        L[x][y] = 1
        wspolrzedne = [[-1,-1],[-1,0], [0,-1], [0,1], [1,0], [1,1], [-1,1], [1,-1]]
        for sx, sy in wspolrzedne:
            #tmp = random.choice(True, False)
            tmp = False
            if x + sx < N and y + sy < N and x + sx >= 0 and y + sy >= 0 and tmp == True:
                L[x+sx][y+sy] = 1
                
    
    for i in range(170000):
        x = random.randint(0,N-1)
        y = random.randint(0,N-1)
        L[x][y] = srednia(x,y, N,L)
    
    
    L = id_kolory(L,N, len(kolory))
    
    for i in range(N):
        for j in range(N):
            x = i*bok - 400
            y = -j*bok + 400
            kwadrat(x,y,bok,kolory[L[i][j]])
    
    
tracer(0,0)
N = 100
L = [[0 for j in range(N)] for i in range(N)]
mapa(L,N)
update()
input()

