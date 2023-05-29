

def kolko(n,s):
    #spacja oznacza przesunięcie
    a = n/2
    b = n/2
    for i in range(n):
        space = s*" "
        print(space, end="")
        for j in range(n):
            x = j+0.5
            y = (i+0.5)
            if (x - a)**2 + (y-b)**2 <= (n/2)**2:
                print("#",end="")
            else:
                print(" ", end="")
        print("")


def balwan(n): 

    k = 2
    kolko(n, 4)
    kolko(n+k, 3)
    kolko(n+k**3,0)



n = int(input("Podaj n: "))

balwan(n)

