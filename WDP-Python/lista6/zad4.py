def podziel(s):
    L = []
    fragment = ""

    for e in s:
        if (e != ' ' and e != '\n'):
            fragment += e
        else:
            if fragment != '':
                L.append(fragment)
                fragment =""
    
    if fragment != '':
        L.append(fragment)
        fragment =""

    return L

s = "Ala   ma    kota"
print(podziel(s))