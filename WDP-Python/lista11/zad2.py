def stworz_slownik(slowo):
    slownik = {}
    
    i = 1
    for e in slowo:
        if e not in slownik:
            slownik[e] = i
            i+=1
    return slownik

def ppn(slowo):
    
    slownik = stworz_slownik(slowo)
    wynik = ""
    for e in slowo:
        wynik += str(slownik[e]) + '-'
    wynik = wynik[:len(wynik)-1]
    
    return wynik

print(ppn('tata'))
        
    

    
        
        