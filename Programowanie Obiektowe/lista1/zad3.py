#Karolina Jędraszek 
#lista 1: zad 3
#python3 zad3.py

def nowa_tablica():
    return [] #tablica

def dodaj(t, e, ind):

    if len(t) > 0:
        min = t[0][1]
        maks = t[len(t)-1][1]

        if ind > maks: #indeks wiekszy od maks. ind.
            for i in range(maks+1,ind):
                t.append((0,i))
            t.append((e,ind))
            
            return
        
        if ind < min:
            for i in range(ind+1,min):
                t.append((0,i))
            t.append((e,ind))
            t.sort(key=lambda x: x[1])

            return
        
        t[min + abs(ind - min)] = (e,ind) # wpp zamien wartosc
        
    else:
        t.append((e,ind))

def indeks(t,ind):
    if len(t) > 0:
        min = t[0][1]
        maks = t[len(t)-1][1]

        if ind > maks or ind < min:
            print('nie ma takiego indeksu')
        else:
            return t[ind + abs(min)][0]
        
    else:
        print('nie ma takiego indeksu')
    return

def show(t):
    print(t)

#--------------------------------------------------------------

t = nowa_tablica()
dodaj(t,1,0)
dodaj(t,3,4)
dodaj(t,7,2)
dodaj(t,8,-3)
print(indeks(t,-2))
show(t)





        
    




        
        

    

