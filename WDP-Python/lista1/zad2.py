
n = int(input("Podaj liczbe: "))
w = 1
dl = 0

for i in range(n):
    w = w*(i+1)
    dl = len(str(w))
    tmp = dl%10
   
    if dl == 1:
        cyfr_y = "cyfre"
    if dl > 4 and dl <= 21:
        cyfr_y = "cyfr"
    elif tmp > 1 and tmp < 5:
        cyfr_y = "cyfry"
    else:
        cyfr_y = "cyfr"
    
    if i+1 >= 4:
        print(f'{i+1}! ma {dl}', cyfr_y)

