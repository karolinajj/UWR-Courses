def biale(k,n): 

    b = "" 

    for i in range(2*n): 

        if i % 2 == 0: 
            b += k*" " 
        else: 
            b+= k*"#" 
    return b 

def czarne(k,n): 
    c = "" 

    for i in range(2*n): 

        if i % 2 == 1: 
            c += k*" " 
        else: 
            c+= k*"#" 
    return c 

def szachownica(n,k): 

    for i in range(2*n): 
        if i % 2 == 0: 
            wiersz = biale(k,n) 
        else: 
            wiersz = czarne(k,n) 

        for j in range(k): 
            print(wiersz) 

n = 4 
k = 3 

szachownica(n,k) 