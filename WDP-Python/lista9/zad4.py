import random
from turtle import *

def losuj_sasiad(i,j,N,M):

    potencjalni = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]] #lista potencjalnych sasiadow
    sasiedzi = [] #lista prawidlowych sasiadow

    for y,x in potencjalni:

        if y < 0 or x < 0 or y >= N or x >= M:
            continue
        else:
            sasiedzi.append([y,x])

    return random.choice(sasiedzi)

def pojedynek(s): #sprawdza czy pojedynek wygrany przez ij
    if s == 'pk' or s == 'kn' or s == 'np':
        return True
    else:
        return False


def kwadrat(x, y, kolor):
    BOK = 20
    SX = 0
    SY = 0

    fillcolor(kolor)
    pu()
    goto(SX + x * BOK, SY - y * BOK)
    pd()
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill() 


def rysuj(L,N,M):
    clear()
    tracer(0,0)
    for y in range(N):
        for x in range(M):
            if L[y][x] == 'p':
                kolor = 'white'
            if L[y][x] == 'k':
                kolor = 'black'
            if L[y][x] == 'n':
                kolor = 'red'
            if L[y][x] == '.':
                kolor = 'lightgreen'
            kwadrat(x, y, kolor)   
    update()


def gra(N,M,L,S):
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] != '.':
                ys,xs = losuj_sasiad(i,j,N,M)
                if S[i][j] > 1 and L[ys][xs] == '.': #zasiedlenie pustego pola
                    L[ys][xs] = L[i][j]
                    S[ys][xs] = S[i][j] - 1
                if L[ys][xs] != '.' and L[ys][xs] != L[i][j]: #pojedynek
                    if(pojedynek(L[i][j] + L[ys][xs])):
                        yw = i  #wspolrzedne wygranego
                        xw = j
                        yp = ys #wspolrzedne przegranego
                        xp = xs
                    else:
                        yw = ys
                        xw = ys
                        yp = i
                        xp = j
                    
                    S[yw][xw] = max(S[yw][xw]+1, 5)
                    S[yp][xp] = min(0, S[yp][xp] - 1)
                    
                    if( S[yp][xp] == 0):
                        L[yp][xp] = '.'
    rysuj(L,N,M)
    s = ''                      #zmiana tablicy na string zeby mozna bylo dac do seta
    for i in range(N):
        for j in range(M):
            s+= str(S[i][j])

    return s
    




def plansza():
    L = [list(wiersz) for wiersz in open('plansza.txt').read().split()]
    S = [[random.randint(1,5) for j in range(len(L[0]))] for i in range(len(L))]

    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == '.':
                S[i][j] = 0

    N = len(L)
    M = len(L[0])


    historia = set()
    historia.add(gra(N,M,L,S))

    while True:
        if gra(N,M,L,S) in historia:
            print('koniec')
            break
    input()

    
        
        
plansza()
