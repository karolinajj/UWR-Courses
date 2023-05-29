
def czy_pierwsza(n):
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3,int(n**(1/2))+1,2):
        if n % i == 0: return False

    return True

def dzielniki_pierwsze(n):
    L=[]
    if(n % 2 == 0): L.append(2)
    for i in range(3,n,2):
        if(n%i == 0) and (czy_pierwsza(i)):
            L.append(i)

    print(L)


n = int(input("Podaj n: "))
dzielniki_pierwsze(n)