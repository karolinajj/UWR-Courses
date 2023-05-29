def isprime(n):
    if n == 1: return False
    if n == 2: return True
    if n%2 == 0: return False

    i = 3
    while(i*i <= n):
        if n % i == 0: return False
        i += 2

    return True

def wytnij(a,b,slowo):
    w = ""
    for i in range(a,b):
        w += slowo[i]
    return w

def candidates(n,k):

    number = ""
    sevens = k*"7"
    w = 0
    tmp = 0

    for i in range(0, 10**(n-k),1):
        number = ""
        if (n == k) and isprime(int(sevens)):
            print(number)
            w+=1
        elif not("7" in str(i)):
            for j in range(n-k+1):
                if(len(str(i)) < n-k and j == 0):
                    pocz = ""
                    kon = "0"*(n-k-len(str(i))) + str(i)
                    number = pocz + sevens + kon
                    #print(number)
                    tmp += 1
                    if isprime(int(number)):
                        w+=1
                        print(number)

                elif(len(str(i)) == n-k):
                    pocz = wytnij(0, j, str(i))
                    kon = wytnij(j, n-k, str(i))
                    number = pocz + sevens + kon
                    if len(str(int(number))) == len(number):
                        #print(number)
                        tmp +=1
                        if isprime(int(number)):
                            w += 1
                            print(number)
    #print("Tmp ", tmp)
    return w


def hiperhappy(n,k):
    result = 0
    for i in range(k,n+1):
        result += candidates(n,i)
    return result

n = int(input("Ile cyfr ma miec liczba? "))
k = int(input("Podaj liczbe '7' "))
print("Wynik: ",hiperhappy(n,k))

