from losowanie_fragmentow import losuj_fragment


def losuj_haslo(n):
    

    for i in range(10):
        dl = 0
        tmp = 0
        haslo = ''
        while(dl < n):
            frag = losuj_fragment()
            tmp = len(frag)
            if(tmp + dl <= n):
                haslo += frag
                dl += tmp
            if dl == n - 1:
                haslo = haslo.removesuffix(frag)
                dl -= tmp
        print(haslo)      


print("Hasla dlugosci 8:")
losuj_haslo(8)

print("Hasla dlugosci 12:")
losuj_haslo(12)
