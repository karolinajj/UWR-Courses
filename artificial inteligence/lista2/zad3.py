# Idea:
# Heuristic: We prirotize commandos that are the furthest from 
# the nearest possible end position.

# To opimize time, we precompute the table with the shortest path from
# each position to the nearest possible end position.
# We use BFS to do it.
# passes 20/21 cases
import heapq
from collections import deque

moves_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
moves_names = ['D', 'U', 'R', 'L']

def read_input(file_path="zad_input.txt"):
    walls = []
    start_positions = set()
    end_positions = set()
    
    with open(file_path, "r") as input_file:
        for row, line in enumerate(input_file):
            line = line.strip()
            if not line:
                continue
            
            temp_walls = []
            for col, char in enumerate(line):
                temp_walls.append(char == '#')
                if char in {'G', 'B'}:
                    end_positions.add((row, col))
                if char in {'S', 'B'}:
                    start_positions.add((row, col))
            
            walls.append(temp_walls)
    
    return walls, start_positions, end_positions

def is_safe(move, walls):
    return 0 <= move[0] < len(walls) and 0 <= move[1] < len(walls[0]) and not walls[move[0]][move[1]]

def make_move(positions, direction, walls):
    return {(pos[0] + direction[0], pos[1] + direction[1]) if is_safe((pos[0] + direction[0], pos[1] + direction[1]) , walls) else pos for pos in positions}

def are_all_on_end(positions, end_positions):
    return all(pos in end_positions for pos in positions)

# calculates the shortest distance from each traversable cell to the nearest goal (G or B)
# To do this we use bfs exploring by level from all goal positions
def precompute_heuristic(walls, end_positions):
    rows, cols = len(walls), len(walls[0])
    heuristic_map = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()
    
    for goal in end_positions:
        queue.append((goal[0], goal[1], 0))
        heuristic_map[goal[0]][goal[1]] = 0
    
    while queue:
        row, col, dist = queue.popleft()
        for row_dir, col_dir in moves_directions:
            new_row, new_col = row + row_dir, col + col_dir
            if 0 <= new_row < rows and 0 <= new_col  < cols and not walls[new_row][new_col] and heuristic_map[new_row][new_col] == float('inf'):
                heuristic_map[new_row][new_col] = dist + 1
                queue.append((new_row, new_col, dist + 1))
    
    return heuristic_map

def heuristic(positions, heuristic_map):
    return max(heuristic_map[pos[0]][pos[1]] for pos in positions)

def a_star(start_state, walls, end_positions, heuristic_map, max_steps=150):
    pq = [] #uses heapq to expand the cheapest node
    visited = {} #stores the minimum cost to reach a given state
    heapq.heappush(pq, (0, 0, start_state, ""))
    visited[frozenset(start_state)] = 0

    while pq:
        # priority is len of path made up to this point and cost of heuristic(for the current_state)
        # cost is a len of path

        priority, cost, current_state, path = heapq.heappop(pq)
        if are_all_on_end(current_state, end_positions):
            return path

        if len(path) >= max_steps:
            continue

        for d, direction in enumerate(moves_directions):
            new_state = make_move(current_state, direction, walls)
            state_hash = frozenset(new_state)
            new_cost = cost + 1

            if state_hash not in visited or new_cost < visited[state_hash]:
                heapq.heappush(pq, (new_cost + heuristic(new_state, heuristic_map), new_cost, new_state, path + moves_names[d]))
                visited[state_hash] = new_cost

    return ""

def main():
    walls, start_positions, end_positions = read_input()
    heuristic_map = precompute_heuristic(walls, end_positions)
    solution_path = a_star(start_positions, walls, end_positions, heuristic_map)
    
    if solution_path and len(solution_path) < 150:
        with open("zad_output.txt", "w") as output_file:
            output_file.write(solution_path + "\n")

if __name__ == "__main__":
    main()