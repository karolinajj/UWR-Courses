def koperta(k):
   
    for i in range(k):
        for j in range(k):
            if j == 0 or j == k-1 or i == 0 or i == k-1:
                print("X", end="")
            elif j == i or j + i == k-1:
                print("X", end="")
            else:
                print(" ", end="")
        print("\n", end="")        

   
n = int(input("Podaj n: "))
koperta(2*n + 1)