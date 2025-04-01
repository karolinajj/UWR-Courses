# Idea:
# In every start position we put a commando. We will be moving them simultaniosly, 
# making the same move for each of them.

# Fisrt we make random moves to get 2-3 commandos
# (we want as many of them to merge as possible).

# Then we run bfs to find the remaining path, trying to make every possible move.
# If a move is not possible (due to a wall) for a certain commando, 
# they stay in the same possition.
# passes 8-9/11 cases

import random

walls = list()
start_positions = set()
end_positions  = set()
moves_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
moves_names = ['D', 'U', 'R', 'L']

def read_input():
    row = 0
    with open("zad_input.txt", "r") as input:
        for line in input:
            line = (line.rstrip('\r')).rstrip('\n')
            if len(line) == 0: continue

            col = 0
            temp_walls = list()
            for i in line:
                if i == '#': temp_walls.append(True)
                else: temp_walls.append(False)

                if i == 'G': end_positions.add((row, col))
                elif i == 'S': start_positions.add((row, col))
                elif i == 'B':
                    end_positions.add((row, col))
                    start_positions.add((row, col))
                col += 1

            walls.append(temp_walls)
            row += 1


def is_safe(move): 
    return (not walls[move[0]][move[1]]) and (move[0] < len(walls) and move[0] >= 0) and (move[1] < len(walls[0]) and move[0] >= 0)

def make_move(positions, dir):
    new_state = set()
    for commando in positions:
        new_move = (commando[0] + dir[0], commando[1] + dir[1])
        if is_safe(new_move):
            new_state.add(new_move)
        else: new_state.add(commando)
    return new_state

def  are_all_on_end(positions): 
    for commando in positions:
        if commando not in end_positions: return False
    return True

def make_random_moves(start_state, count, commandos_alive = 1):
    previous_move = -1
    path = ""
    for i in range(0, count):
        next_move = random.randint(0, 3)

        # preventing opposite moves
        while((previous_move == 0 and next_move == 1) or 
              (previous_move == 2 and next_move == 3)):
                next_move = random.randint(0, 3)

        start_state = make_move(start_state, moves_directions[next_move])
        previous_move = next_move
        path += moves_names[next_move]

        if len(start_state) <= commandos_alive: break

    return (start_state, path)


def hash_state(positions):
    positions = sorted(positions)
    hash = 0
    mult = 1
    for i in positions:
        hash += mult * ((i[0] * len(walls)) + i[1])
        mult *= len(walls) * len(walls[0])

    return hash

def bfs(start_state):
    queue = []
    visited = [False] * (pow((len(walls)*len(walls[0])), 3) + 1000)
    queue.append((start_state, ""))
    visited[hash_state(start_state)] = True
    
    while len(queue) != 0:
        current_state, path = queue.pop(0)
        if len(path) >= 150 - RAND_MOVES : return (False, "")
        if  are_all_on_end(current_state): return (current_state, path)

        for d in range(0, 4):
            new_state = make_move(current_state, moves_directions[d])
            if not visited[hash_state(new_state)]:
                queue.append((new_state, path+moves_names[d]))
                visited[hash_state(new_state)] = True

    return (False, "")

def print_board(positions):
    for row in range(0, len(walls)):
        for col in range(0, len(walls[row])):
            if walls[row][col]: print("#", end='')
            elif (row, col) in positions and (row, col) in end_positions: print("B", end='')
            elif (row, col) in positions: print("S", end='')
            elif (row, col) in end_positions: print("G", end='')
            else: print(" ", end='')

        print()


read_input()

res = False
path1 = ""
path2 = ""    
while res == False:
    positions = start_positions
    max_comm = 2
    iter = 0
    while len(positions) > max_comm:
        positions, path1 = make_random_moves(start_positions, 80, max_comm)
        iter += 1
        if iter == 100: max_comm = 3
    
    global RAND_MOVES
    RAND_MOVES = len(path1)
    res, path2 = bfs(positions)


output = open("zad_output.txt", "w")
output.write(path1 + path2)
output.close()