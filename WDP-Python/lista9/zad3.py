
L = open('dane.txt').readlines()
maks = 0
aktualne = 0


for wiersz in L:
    if(wiersz != "\n"):
        aktualne += int(wiersz)
    else:
        if aktualne > maks:
            maks = aktualne
            aktualne = 0

if aktualne > maks:
    maks = aktualne

print(maks)
    

        

