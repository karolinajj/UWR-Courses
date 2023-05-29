######################################
#  czeste_slowa2.py
######################################


cnt = {}

for wiersz in open('lalka-tom-pierwszy.txt', encoding='utf8'):
    for p in ',.:?!':
        wiersz = wiersz.replace(p, ' ')
        
    for w in wiersz.split():
        if len(w) <= 5:
            continue
            
        if w not in cnt:    
            cnt[w] = 0
        cnt[w] += 1
            
    
#for w in sorted(cnt.keys(), key=lambda k:cnt[k], reverse=True)[:10]:
for w in sorted(cnt.keys(), key=cnt.get, reverse=True)[:10]:
    print (w, cnt[w])
        


######################################
#  czeste_slowa3.py
######################################

from collections import defaultdict as dd


#cnt = dd(lambda:0)
cnt = dd(int)

for wiersz in open('lalka-tom-pierwszy.txt', encoding='utf8'):
    for p in ',.:?!':
        wiersz = wiersz.replace(p, ' ')
        
    for w in wiersz.split():
        if len(w) <= 5:
            continue
            
        cnt[w] += 1
            
    
#for w in sorted(cnt.keys(), key=lambda k:cnt[k], reverse=True)[:10]:
for w in sorted(cnt.keys(), key=cnt.get, reverse=True)[:10]:
    print (w, cnt[w])
        

######################################
#  czeste_slowa.py
######################################


slowa = open('lalka-tom-pierwszy.txt', encoding='utf8').read().split()

cnt = {}

"""
for w in slowa:
    if w in cnt:
        cnt[w] += 1  # cnt[w] = cnt[w] + 1
    else:
        cnt[w] = 1
"""

for w in slowa:
    if len(w) <= 5:
        continue
        
    if w not in cnt:    
        cnt[w] = 0
    cnt[w] += 1
            
    
#for w in sorted(cnt.keys(), key=lambda k:cnt[k], reverse=True)[:10]:
for w in sorted(cnt.keys(), key=cnt.get, reverse=True)[:10]:
    print (w, cnt[w])
        


####################################
# Program:  kwadraty.py
####################################

from turtle import *
import random
import numpy as np

tracer(0,1)

BOK = 18

def move(x, y):
    pu()
    goto(x, y)
    pd()
    
def kwadracik(x, y, kolor): # x,y = numery kratek
    fillcolor([float(x) for x in kolor])
    move(BOK * x, BOK * y)
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()
    
uzyte = set()

for i in range(50000):
    bok = random.randint(4, 8)
    sx = random.randint(-25, 25)
    sy = random.randint(-25, 25)
    
    nowe = { (sx+x, sy+y) for x in range(bok) 
                          for y in range(bok) }
                   
    if len(nowe & uzyte) == 0:
        uzyte |= nowe   #  uzyte = uzyte | nowe    --- '|' oznacza sumę zbiorów
        kolor = np.random.rand(3)
        for x,y in nowe:
            kat = random.randint(-15,15)
            rt(kat)
            kwadracik(x,y,kolor)
            rt(-kat)
input()               


######################################
#  qsort.py
######################################

import random

def losowa(N, K):
    return [random.randint(0,K) for i in range(N)]

##########################

def wstaw(L, e, klucz):
    for i in range(len(L)):
        if klucz(e) < klucz(L[i]):
            return L[:i] + [e] + L[i:]
    return L + [e]        

def posortowana(L, klucz):
    wynik = []
    for e in L:
        wynik = wstaw(wynik, e, klucz)
    return wynik
        
    
def identycznosc(x):
    return x
###########################


def qsort(L):
    if L == []:
        return []
    x = L[0]
    mniejsze = [e for e in L[1:] if e <= x]
    wieksze = [e for e in L[1:] if e > x]
    return qsort(mniejsze) + [x] + qsort(wieksze)
    
print (qsort([5,4,3,1,2,2,2,8,9,11,62,1]))    

N = 1_000_000
L = losowa(N, 10000)

print ('Start')
print ('qsort', len(qsort(L)))
print ('posortuj', len(posortowana(L, identycznosc)))



######################################
#  slowniki.py
######################################

# coding: utf-8
