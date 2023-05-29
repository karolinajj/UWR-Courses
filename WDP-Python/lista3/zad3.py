def usun_w_nawiasach(s):
    tmp = 0
    w = ""
    for i in range(len(s)):
        if s[i] == '(':
            tmp = 1
        if tmp == 0:
            w = w + s[i]
        if s[i] == ')':
            tmp = 0
    return w

print(usun_w_nawiasach("Ala ma kota (perskiego)!"))
print(usun_w_nawiasach("Ala ma kota (perskiego) i psa (dużego)!"))
print(usun_w_nawiasach("(Tekst)"))
print(usun_w_nawiasach("test(Tekst)"))
    