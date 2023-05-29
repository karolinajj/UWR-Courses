
def klucz(e):
    return e[1]


def usun_duplikaty(L):
    
    L.sort()
    L_copy = []
    L_copy.append(L[0])

    for i in range(1,len(L)):
        if L[i-1][0] != L[i][0]:
            L_copy.append(L[i])

    L_copy.sort(key= klucz)
    L.clear()
    for i in range(len(L_copy)):
        L.append(L_copy[i][0]) 

    return L


def dodaj_i(L):
    for i in range(len(L)):
        L[i] = [L[i],i]
    #print(L)



L = [1,2,3,1,2,3,8,2,2,2,9,9,4]
dodaj_i(L) #zamienia liste na dwuwymiarowa
print(usun_duplikaty(L))
