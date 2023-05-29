import random
def randperm(n):
    L = []
    for i in range(n):
        L.append(i)
    
    for i in range(n):
       indeks = random.randint(0,n-1) #losuje indeks do zmiany wartosci w tablicy
       wartosc = L[i]
       L[i] = L[indeks] 
       L[indeks] = wartosc

    return L  

n = int(input("Podaj n: "))
print(randperm(n))