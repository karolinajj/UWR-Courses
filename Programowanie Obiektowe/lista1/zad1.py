#Karolina Jędraszek 
#lista 1: zad 1
#python3 zad1.py

import math

def poprawnosc(T): #funkcja sprawdza czy z podanych pkt mozna utworzyc trojkat
    T.sort(key=lambda x: x[1])

    if T[0][1] == T[2][1] or len(set(T)) < 3: #tzn ze pkt sa wspoliniowe
        print('blad')
        return False
    return True

#--------------------------------------------------------------

def new_square(p1,p2): #dane: p1,p2 - dwa punkty tworzace 'dolny' bok kwadratu
    x_1, y_1 = p1
    x_2, y_2 = p2
    bok = abs(x_1 - x_2)
    
    if y_1 != y_2 or p1 == p2:
        print('blad')
        return []
    else:
        p3 = (x_2,y_2+bok)
        p4 = (x_1, y_1+bok)

    return list(['square',p1,p2,p3,p4])

def new_triangle(p1,p2,p3):

    T = [p1,p2,p3]
    if(poprawnosc(T)):
        return list(['triangle',p1,p2,p3])
    return []

def new_circle(p1,r):
    if r == 0:
        print('blad')
        return []
    return list(['circle',p1, r])

#--------------------------------------------------------------

def pole(f):

    if len(f) < 1:
        print('podano nieprawidlowe dane')
        return 0

    if f[0] == 'square':
        a = abs(f[1][0] - f[2][0])
        
        return a*a
    
    if f[0] == 'triangle':
        x_a, y_a = f[1]
        x_b, y_b = f[2]
        x_c, y_c = f[3]

        return abs((x_b - x_a)*(y_c - y_a) - (y_b - y_a)*(x_c - x_a))/2
    else:
        return math.pi*f[2]

def show(f):
    if len(f) < 1:
        print('podano nieprawidlowe dane')
    else:
        print('type: ', f[0], end=', ')
        if f[0] == 'circle':
            print('srodek okregu: ', f[1], "r: ", f[2])
        else:
            for i in range(1,len(f)):
                print(f[i], end=' ')
            print()
    
        
def sumapol(F,size):

    sum = 0
    for e in F:
        sum += pole(e)
    return sum

def przesun(f,x,y):
    if f[0] == 'circle':
        f[1] = f[1][0] + x, f[1][1] + y

    else:
        for i in range(1,len(f)):
            f[i] = f[i][0] + x, f[i][1] + y

#--------------------------------------------------------------    

f1 = new_circle((0,0),1) #dane: wspolrzedne srodka okregu, promien
f2 = new_triangle((1,0), (-1,0), (0,3)) #dane: wspolrzedne wierzcholkow trojkata
f3 = new_square((1,0),(2,0)) #dane: wspolrzedne A,B kwadratu ABCD (gdzie y_C > y_B)


show(f1)
print('pole f1 wynosi: ', pole(f1))
przesun(f1,2,3)
show(f1)
print()

show(f2)
print('pole f2 wynosi: ', pole(f2))
przesun(f2,2,3)
show(f2)
print()

show(f3)
print('pole f3 wynosi: ', pole(f3))
przesun(f3,2,3)
show(f3)


F = list([f1,f2,f3])
size = len(F)

print('suma pol wynosi: ', sumapol(F,size))







