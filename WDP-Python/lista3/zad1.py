def prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range( 3, int(n**(1/2) + 1), 2):
        if n % i == 0:
            return False

    return True

def liczby(a,b):

    w = 0
    for i in range(a,b+1,1):
        if('777' in str(i)) and (prime(i)):
            print(i, end=", ")
            w += 1
    print("Tych liczba jest: ", w)


a = int(input("Podaj poczatek zakresu: "))
b = int(input("Podaj koniec zakresu: "))
liczby(a,b)
