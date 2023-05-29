
def litery_slowa(slowo):
    litery = set(slowo)
    
    return litery


def ile_liter(slowo):
    wynik = 0
    for litera in slowo:
        if (litera >= 'a' and litera <= 'z') or (litera >= 'A' and litera <= 'Z'):
            wynik+=1
    return wynik

tekst = open("lalka-tom-pierwszy.txt", encoding = 'UTF-8').read().split()
polskie = set('ąćęłńóśżź')

#tekst = list('ala ma kota bądź dwa golobki i psa...')

aktualna_dl = 0
fragment =''
max_dl = 0
max_fragment = ''

for e in tekst:
    #print(litery_slowa(e), polskie)
    
    if len(litery_slowa(e) & polskie) == 0:
        aktualna_dl += ile_liter(e)
        fragment = fragment + ' '+e
    else:
        
        if aktualna_dl >= max_dl:
            max_dl = max(max_dl, aktualna_dl)
            max_fragment = ''
            max_fragment += fragment
            
            #print(max_fragment)
            #print('\n')
        aktualna_dl = 0
        fragment = ''      
if aktualna_dl >= max_dl:
    max_dl = max(max_dl, aktualna_dl)
    max_fragment = fragment


print(max_fragment)

