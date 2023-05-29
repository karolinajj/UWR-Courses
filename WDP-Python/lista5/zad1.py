def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def energia_collatza(n,i):
    if(n == 1):
        return i
    else:
        n = F(n)
        i += 1
        return energia_collatza(n,i)

def srednia(E):
    wynik = 0
    for i in range(len(E)):
        wynik += E[i]
    wynik /= len(E)
    print("srednia: ", wynik)

def mediana(E):
    E.sort()
    if(len(E) % 2 == 1): wynik = E[len(E)//2]
    else: wynik = (E[len(E)//2] + E[len(E)//2 - 1])/2
    print("mediana: ", wynik)

def analiza_collatza(a,b):
    E = [] #lista energii
    for i in range(a,b+1): #[a,b]
        E.append(energia_collatza(i,0))
    
    print(E)

    srednia(E)
    mediana(E)
    maks =  E[len(E)-1]
    mini = E[0]

    print("maksimum: ",maks)
    print("minimum: ",mini)

a = int(input("Podaj a: "))
b = int(input("podaj b: "))
analiza_collatza(a,b)
