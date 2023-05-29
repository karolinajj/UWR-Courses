
def sumy_podzbiorow(n,reszta,L):
    wynik = set()
    sum = 0

    for e in wynik:
        sum += e

    if n == 0: #warunek zakończenia rekurencji (suma podzbioru 0-el jest równa 0)
        return {0}
    else:
        for i in reszta: #dla każdego nieużytego indeksu obliczam sumę podzbioru n-1 elementowego
            sumy_podzbiorow(n-1,reszta - {i},L)
            e = L[i] + sum
            wynik = wynik | {e}

    return wynik #jak zwracam samą sumę to jest źle, ale jak dam return wynik, to jest błąd typów w lini 14



L = [1,2,3]
reszta = set([i for i in range(len(L))]) #reszta to zbiór indeksów czyli dla tablicy 3-el mamy {0,1,2}

print(sumy_podzbiorow(len(L), reszta,L))

