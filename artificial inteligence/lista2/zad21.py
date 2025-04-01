# How?
# let say that the dimensions of maze are X*Y
# first we do X moves left, Y moves down, X moves right, Y moves up
# and then we few times we do some random moves 
# to get fewer possible position of hero (naive? how better?)
# next we run BFS from every left possible pos and we end if every instance
# is at some end point
# (passes 9-10/11 tests)

import copy
from collections import deque
import random
import time

SOLUTION=""

checked_positions = set()

def modify_pos(pos, maze, dir): #check
    # print("MODIFY POS =", pos, "dir =", dir)
    x,y = 0,0

    match dir:
        case "L":
            x = -1
        case "R":
            x = 1
        case "U":
            y = -1
        case "D":
            y = 1
    # print("NEW POS =", (pos[0]+y, pos[1]+x),"and maze =",maze[pos[0]+y][pos[1]+x],"\n")
    if maze[pos[0]+y][pos[1]+x] != '#':
        return (pos[0]+y, pos[1]+x)
    return pos
    
def move(maze, option): # check
    x,y = 0,0
    global SOLUTION

    match option:
        case "left":
            x = -1
            SOLUTION += 'L'
        case "right":
            x = 1
            SOLUTION += 'R'
        case "up":
            y = -1
            SOLUTION += 'U'
        case "down":
            y = 1
            SOLUTION += 'D'
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[0])-1):
            #print("in move:",i,j," -> ",i+y,j+x)
            if maze[i][j] == 'S':
                match maze[i+y][j+x]:
                    case ' ':
                        maze[i+y][j+x] = 'S'
                        maze[i][j] = ' '
                    case 'G':
                        maze[i+y][j+x] = 'B'
                        maze[i][j] = ' '
                    case 'B':
                        maze[i][j] = ' '
                    case 'S':
                        maze[i][j] = ' '
            if maze[i][j] == 'B':
                match maze[i+y][j+x]:
                    case ' ':
                        maze[i+y][j+x] = 'S'
                        maze[i][j] = 'G'
                    case 'G':
                        maze[i+y][j+x] = 'B'
                        maze[i][j] = 'G'
                    case 'B':
                        maze[i][j] = 'G'
                    case 'S':
                        maze[i][j] = 'G'

def kill_comandos(maze): #check
    for i in range(len(maze[0])-3):
        move(maze,"right")
    for i in range(len(maze)-3):
        move(maze,"down")
    for i in range(len(maze[0])-3):
        move(maze,"left")
    for i in range(len(maze)-3):
        move(maze,"up")
    
    # global  SOLUTION
    
    # print("BEFORE RANDOM: ")
    # print(SOLUTION)
    # print("len of sol", len(SOLUTION))
    # print_maze(maze)

    # for i in range(10):
    #     dir = random.choice(["left","up","right","down"])
    #     print("i ==========", i,",",dir)
    #     print("before")
    #     print_maze(maze)
    #     move(maze,dir)
    #     print("after")
    #     print_maze(maze)
    
    # print("AFTER RANDOM: ")
    # print(SOLUTION)
    # print("len of sol", len(SOLUTION))
    # print_maze(maze)

def get_state(maze): # check
    global SOLUTION
    solution = SOLUTION[:]
    # for row in maze:
    #     print(row)
    positions = []
    state = [[], solution]
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[0])-1):
            if maze[i][j] == 'S' or maze[i][j] == 'B':
                positions.append((i,j))
    return (tuple(positions),solution)

def new_states(state,maze): # state is ((positions), "PATH")
    new_states = []
    global checked_positions

    for dir in ["L", "R", "U", "D"]: # ["L", "R", "T", "B"] error for few hours :))
        positions = []
        for pos in state[0]:
            positions.append(modify_pos(pos,maze,dir))
        positions = tuple(positions)
        if positions not in checked_positions:
            checked_positions.add(positions)
            new_states.append((positions, state[1] + dir))
    # print(new_states, "new states from", state, ';;;')
    return new_states

def correct_state(positions,maze):
    for pos in positions:
        if maze[pos[0]][pos[1]] != 'G' and maze[pos[0]][pos[1]] != 'B':
            return False
    return True

def print_maze(maze):
    print("--------------------------")
    for row in maze:
        for char in row:
            print(char,end="")
        print()

def do_random_moves(k,maze,state, option):
    #print(state)
    prev = ""
    for i in range(k):
        if option == 1:
            dir = random.choice(["R","U"])# random.choice(["L","R","U","D"])
        else:
            dir = random.choice(["D","L"])
        # if dir == prev:
        #     continue
        positions = []
        for pos in state[0]:
            positions.append(modify_pos(pos,maze,dir))
        positions = tuple(positions)
        state = (positions, state[1] + dir)
    
    new_state = []
    for el in state[0]:
        if el not in new_state:
            new_state.append(el)
    return (tuple(new_state),state[1])


def solve(maze):
    first_state = get_state(maze)
    best_state = copy.deepcopy(first_state)

    for i in range(25000):
        try_state = do_random_moves(55,maze,copy.deepcopy(first_state), 1)
        if(len(try_state[0]) < len(first_state[0])):
            best_state = copy.deepcopy(try_state)

    first_state = best_state
    best_state = copy.deepcopy(first_state)

    for i in range(25000):
        try_state = do_random_moves(15,maze,copy.deepcopy(first_state), 2)
        if(len(try_state[0]) < len(first_state[0])):
            best_state = copy.deepcopy(try_state)

    queue = deque()
    queue.append(first_state) # state is ((positions), "PATH")

    while queue:
        state = queue.popleft()
        for ns in new_states(state,maze):
            if correct_state(ns[0],maze):
                return ns[1]
            queue.append(ns)

    return "D"

def read(input, output):
    with open(input,'r',encoding="utf-8") as f:
        maze = [list(el.strip()) for el in f.readlines()]
    
    kill_comandos(maze)

    solution = solve(maze)

    # print("LENGTH OF PATH =", len(solution))
    with open(output,'w',encoding="utf-8") as f:
        f.write(solution)

if __name__ == "__main__":
    read("zad_input.txt", "zad_output.txt")
    