from duze_cyfry import daj_cyfre



def dlc(n):
    for i in range(5):
        for j in range(len(n)):
            L = daj_cyfre(int(n[j]))
            print(L[i], end=" ")
        print('\n', end="")
    

n = input("Podaj n: ")
dlc(n)

