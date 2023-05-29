import random
from collections import defaultdict as dd

pol_ang = dd(list)

for x in open('pol_ang.txt', encoding = 'utf8'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue
    pol, ang = L
    pol_ang[pol].append(ang)


S = open('brown.txt').read().split()
#S = ['dog', 'dog', 'cat']

slowa = dd(int)
for e in S:
    if (e not in slowa):
        slowa[e] = 1
    else:
        slowa[e] += 1
    


def najczestsze(tlumaczenia):
    
    maks = 0
    maks_slowo = tlumaczenia[0]

    for e in tlumaczenia:
        
        if slowa[e] > maks:
            maks_slowo = ""
            maks = slowa[e]
            maks_slowo += e
    return maks_slowo
        
    
def tlumacz(polskie):
    wynik = []
    for p in polskie:
        if p in pol_ang:
            wynik.append(najczestsze(pol_ang[p]))
        else:
            wynik.append('[*]')
    return ' '.join(wynik)        
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

print (tlumacz(zdanie))  