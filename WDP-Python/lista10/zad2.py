alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
litery = [e for e in alfabet]

polskie = set(open('popularne_slowa.txt', encoding = 'utf8').read().split())
#polskie = set(['ala', 'ma', 'kota'])

def slownik_klucz(k):
    litery_k = [alfabet[(i+k)%len(alfabet)] for i in range(len(alfabet))]
    slownik = dict(zip(litery, litery_k ))
    return slownik

def cesar(slowo,k,slownik):
    wynik = ""
    for s in slowo:
        if s in slownik:
            wynik += slownik[s]
        else:
             return ""
    
    return wynik

def najdluzsze_cesarksie():
    wynik = ""
    
    for k in range(1,len(alfabet)):
        for slowo in polskie:
            #print(slowo)
            slownik = slownik_klucz(k)

            szyfr = cesar(slowo,k,slownik)
            
            if szyfr in polskie and len(szyfr) >= len(wynik):
                if len(szyfr) >  len(wynik):
                    L = []
                    wynik = ""
                    wynik += szyfr
                    L.append(szyfr)
                else:
                    L.append(szyfr)

                print(slowo,szyfr)
    return set(L)

print(najdluzsze_cesarksie())
