n = int(input("Podaj n: "))

space = 3*" "
dot = 3*"*"

for i in range(3*n):
    if i >= n and i <= 2*n - 1:
        print(f'{dot} {dot} {dot}')
    else:
        print(f'{space} {dot} {space}')
