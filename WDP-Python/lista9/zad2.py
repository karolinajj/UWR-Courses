from collections import defaultdict as dd

def slownik(s):
    his = dd(int)
    
    for e in s:
        if(e not in his):
            his[e] = 1
        else:
            his[e] = his[e] + 1
    return his

def rowne_slowniki(slownik1, slownik2):
    
    if len(slownik1) != len(slownik2):
        return False
    
    for e in slownik1:
        if e not in slownik2:
            return False

        if slownik1[e] != slownik2[e]:
            return False
        
    return True

def zagadka(s):
    slownik1 = slownik(s)
    
    S = open('popularne_slowa.txt', encoding = 'utf-8').read().split()
    S_new = set()
    #S = open('dane.txt', encoding = 'utf-8').read().split()
    
    
    uzyte = set()
    
    for slowo in S:
        if len(set(slowo) - set(s)) > 0: continue
        S_new.add(slowo)

    
    for slowo1 in S_new:
        for slowo2 in S_new:
            for slowo3 in S_new:

                slownik2 = slownik(slowo1+slowo2+slowo3)
                
                if rowne_slowniki(slownik1,slownik2) and len(set([slowo1+slowo2+slowo3, slowo1+slowo3+slowo2, slowo2+slowo1+slowo3, slowo2+slowo3+slowo1, slowo3+slowo1+slowo2, slowo3+slowo2+slowo1]).intersection(uzyte)) == 0:
                    print(slowo1, slowo2, slowo3)
                    uzyte.add(slowo1+slowo2+slowo3)
                    uzyte.add(slowo2+slowo1+slowo3)
                    uzyte.add(slowo1+slowo3+slowo2)
                    uzyte.add(slowo2+slowo3+slowo1)
                    uzyte.add(slowo3+slowo1+slowo2)
                    uzyte.add(slowo3+slowo2+slowo1)
                    #print(slownik1, slownik2)



imie = 'Bolesław'
nazwisko = 'Prus'

s = imie.lower() + nazwisko.lower() #sklejam i zamieniam wszystkie litery na małe, żeby zgadzały się w słowniku
zagadka(s)