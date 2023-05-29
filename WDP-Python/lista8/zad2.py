
from collections import defaultdict as dd

def slownik(s):
    his = dd(int)
    
    for e in s:
        if(e not in his):
            his[e] = 1
        else:
            his[e] = his[e] + 1
    return his
        


def czy_ukladalne(slowo1, slowo2):
    
    slownik1 = slownik(slowo1)
    slownik2 = slownik(slowo2)
    
    for e in slowo1:
        if (e in slownik2) and (slownik1[e] <= slownik2[e]):
            continue
        else:
            return False
    return True




slowo1 = "ali"
slowo2 = "alikot"

if(czy_ukladalne(slowo1, slowo2) == True):
    print("tak")
else:
    print("nie")