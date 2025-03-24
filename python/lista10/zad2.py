#Karolina Jędraszek
#lista 10, zadanie 2
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate

def neighbors(tab, i, j):
    alive = 0
    coordinates = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (-1, 1), (1, -1), (1, 1)]
    
    for e in coordinates:
        if tab[i + e[0]][j + e[1]] == 1 :
            alive += 1

    return alive

def random_set():
    tab = [[-1 for i in range(N+2)] for j in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if random.randint(1, 100) <= 35:  
                tab[i][j] = 0
            else:
                tab[i][j] = 1
    return tab

def play(tab):
    new_tab = np.copy(tab)
    for i in range(1, N+1):
        for j in range(1, N+1):
            tmp = neighbors(tab, i, j)
            if tab[i][j] == 0 and tmp == 3:
                new_tab[i][j] = 1
            elif tab[i][j] == 1 and (tmp < 2 or tmp > 3):
                new_tab[i][j] = 0
    
    return new_tab

#-------------------------------------

N = 60 #board dimensions
tab = random_set()

fig, ax = plt.subplots()
img = ax.imshow(np.array(tab)[1:N+1, 1:N+1], cmap='gray', interpolation='nearest')

def update(frame):
    global tab
    tab = play(tab)
    img.set_array(np.array(tab)[1:N+1, 1:N+1])
    return img,

ani = animate.FuncAnimation(fig, update, interval=100, blit=True)

plt.show()
