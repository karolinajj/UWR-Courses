alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
litery = [e for e in alfabet]

def cesar(slowo,k):

    litery_k = [alfabet[(i+k)%len(alfabet)] for i in range(len(alfabet))]
    slownik = dict(zip(litery, litery_k ))
    
    wynik = ""
    for s in slowo:
        wynik += slownik[s]
    
    return wynik


slowo = "azalie"
k = 7
print(cesar(slowo,k))