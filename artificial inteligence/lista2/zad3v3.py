# Idea:
# Heuristic: We prirotize commandos that are the furthest from 
# the nearest possible end position.

# To opimize time, we precompute the table with the shortest path from
# each position to the nearest possible end position.
# We use BFS to do it.
# passes 20/21 cases

from collections import deque
import heapq

directions = [(0,1),(1,0),(0,-1),(-1,0)]
dir_to_char = {
    (0,1):'R',
    (1,0):'D',
    (0,-1):'L',
    (-1,0):'U'
}
def get_dist_map(walls, e_pos):
    rows, cols = len(walls), len(walls[0])
    dist_map = [[float('inf')] * cols for i in range(rows)]
    queue = deque()

    for end in e_pos:
        queue.append((end[0], end[1] , 0))
        dist_map[end[0]][end[1]] = 0
    
    while queue:
        row, col, dist = queue.popleft()
        for x, y in directions:
            new_row, new_col, new_dist = row+y, col+x, dist+1
            #print(new_row,new_col)
            if 0 <= new_row < rows and 0 <= new_col < cols and not (walls[new_row][new_col]) and dist_map[new_row][new_col] > new_dist:
                queue.append((new_row, new_col, dist+1))
                dist_map[new_row][new_col] = dist+1
    return dist_map
 
def heur(state: set, dist_map: list):
    # for row in dist_map:
    #     print(row)
    return max([dist_map[s[0]][s[1]] for s in state])

def finished(pos, e_pos):
    return all([(p in e_pos) for p in pos])

def move(state, direction, walls):
    res = set()
    for pos in state:
        new_pos = (pos[0]+direction[0], pos[1]+direction[1])
        if walls[new_pos[0]][new_pos[1]] or not(0 <= new_pos[0] < len(walls)) or not(0 <= new_pos[1] < len(walls[0])):
            res.add(pos)
        else:
            res.add(new_pos)
    return res

def a_star(s_pos: set, e_pos: set, walls: list, dist_map: list):
    visited = {}
    pq = []
    heapq.heappush(pq, (0,0,tuple(sorted(s_pos)),""))
    visited[tuple(sorted(s_pos))] = 0

    while pq:
        #print("pq len",len(pq))
        priority, cost, state, path = heapq.heappop(pq)
        state_set = set(state)

        if finished(state, e_pos):
            return path
        
        for direction in directions:
            new_state = move(state_set, direction, walls)
            #new_path = path + dir_to_char[direction]
            new_cost = cost + 1
            ns_tuple = tuple(sorted(new_state))
            #ns_hash =frozenset(new_state)

            if ns_tuple not in visited or new_cost < visited[ns_tuple]:
                visited[ns_tuple] = new_cost
                heapq.heappush(pq, (new_cost + heur(new_state, dist_map),
                                    new_cost,
                                    ns_tuple,
                                    path + dir_to_char[direction]))
    return ""

def solve(walls: list[list], s_pos: set, e_pos: set):
    dist_map = get_dist_map(walls, e_pos)
    # for e in dist_map:
    #     print(e)
    return a_star(s_pos, e_pos, walls, dist_map)

def read(input):
    walls = []
    starting_pos = set()
    ending_pos = set()
    with open(input,'r',encoding="utf-8") as f:
        for row, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            
            line_walls = []
            for col, char in enumerate(line):
                line_walls.append(char == '#')
                if char in {'G', 'B'}:
                    ending_pos.add((row, col))
                if char in {'S', 'B'}:
                    starting_pos.add((row, col))
            walls.append(line_walls)
    return walls, starting_pos, ending_pos

if __name__ == "__main__":
    walls, s_pos, e_pos = read("zad_input.txt")
    path = solve(walls, s_pos, e_pos)
    #print("PATH LENGTH:",len(path),"(",path,")")
    with open("zad_output.txt", "w") as output:
            output.write(path + "\n")