#Idea:
# ac-3 algorithm
# First we generate all valid domains for a given row / column (domain is a set of all possible configurations for a row / column).
# We update the puzzle until it is correct.
# In a loop we:
# - identify guaranteed cells (colored or blank) for both rows and columns.
# - update the grid based on these guarantees.
# - filter out invalid configurations from the row and column domains

import numpy as np
from itertools import combinations

DIMENSIONS = [0, 0]
desc = [[], []]
puzzle = []

def read_input():
    global DIMENSIONS, desc, puzzle

    with open('zad_input.txt', 'r') as f:
        line = f.readline().split()
        DIMENSIONS[0], DIMENSIONS[1] = int(line[0]), int(line[1])
        rows_desc, cols_desc = [], []
        
        for _ in range(DIMENSIONS[0]):
            line = f.readline().split()
            rows_desc.append([int(i) for i in line])

        for _ in range(DIMENSIONS[1]):
            line = f.readline().split()
            cols_desc.append([int(i) for i in line])

        desc[0], desc[1] = rows_desc, cols_desc
        puzzle = np.zeros((DIMENSIONS[0], DIMENSIONS[1]), dtype=bool)

def is_correct(rows_domains, cols_domains):
    i = 0
    for row in puzzle:
        if tuple(row) not in rows_domains[i]:
            return False
        i += 1
    for col in range(0, DIMENSIONS[1]):
        if tuple(puzzle[:, col]) not in cols_domains[col]:
            return False
    return True

def generate_domains(option): #option = 1 for rows, 0 for columns
    res = [] #list contains sets of valid configurations for 1st row / col , 2nd row / col ...
    num_cells = DIMENSIONS[1] if option == 0 else DIMENSIONS[0]

    for constraint in desc[option]:
        valid_combinations = []

        for positions in combinations(range(num_cells - constraint[-1] + 1), len(constraint)): #all posssible starting positions for the blocks
            
             #checking if blocks overlap
            overlap = False
            for i in range(1, len(positions)):
                if positions[i - 1] + constraint[i - 1] >= positions[i]:
                    overlap = True
                    break

            # If no overlap, generate the valid configuration for this combination
            if not overlap:
                config = [0] * num_cells
                k = 0
                for start_pos in positions:
                    for j in range(start_pos, start_pos + constraint[k]):
                        config[j] = 1
                    k += 1
                valid_combinations.append(config)

        res.append(set(tuple(config) for config in valid_combinations))
    return res 

def find_guaranteed(domain):
    guaranteed_black = list(list(domain)[0]) #true for positions in which a cell is for sure black
    guaranteed_white = list(list(domain)[0]) #true for positions in which a cell is for sure white

    for solution in domain:
        for i in range(len(solution)):
            if all(s[i] == 1 for s in domain):
                guaranteed_black[i] = 1
                # print(s)
            else:
                guaranteed_black[i] = 0
            
            if all(s[i] == 0 for s in domain):
                guaranteed_white[i] = 0
            else:
                guaranteed_white[i] = 1
    # print((guaranteed_black, guaranteed_white))
    return (guaranteed_black, guaranteed_white)

def delete_invalid_rows(cells, domain, color):
    for row, col in cells:
        incorrect_solutions = []

        for solution in domain[col]:
            if solution[row] != color:
                incorrect_solutions.append(solution)

        for solution in incorrect_solutions:
            domain[col].discard(solution)
    return domain

def delete_invalid_cols(cells, domain, color):
    for row, col in cells:
        incorrect_solutions = []

        for solution in domain[row]:
            if solution[col] != color:
                incorrect_solutions.append(solution)

        for solution in incorrect_solutions:
            domain[row].discard(solution)
    return domain

def solve():
    rows_domains, cols_domains = generate_domains(0), generate_domains(1)

    while not is_correct(rows_domains, cols_domains):
        colored_cells, blank_cells = process_rows(rows_domains)
        cols_domains = update_column_domains(colored_cells, blank_cells, cols_domains) #updating column domains based on row results
        colored_cells, blank_cells = process_columns(cols_domains)
        rows_domains = update_row_domains(colored_cells, blank_cells, rows_domains) #updating row domains based on column results

def process_rows(rows_domains): #finds guaranteed black and white cells for rows
    colored_cells, blank_cells = set(), set()
    row_index = 0

    for row_domain in rows_domains:
        col_index = 0
        intersection = find_guaranteed(row_domain)

        for cell in range(len(intersection[0])): # checking each cell in the row to determine if it is guaranteed to be black or white
            if intersection[0][cell] == 1:
                puzzle[row_index][col_index] = True
                colored_cells.add((row_index, col_index))
            if intersection[1][cell] == 0:
                puzzle[row_index][col_index] = False
                blank_cells.add((row_index, col_index))
            col_index += 1

        row_index += 1

    return colored_cells, blank_cells

def process_columns(cols_domains): #finds guaranteed black and white cells for columns
    colored_cells, blank_cells = set(), set()
    col_index = 0

    for col_domain in cols_domains:
        row_index = 0
        intersection = find_guaranteed(col_domain)

        for cell in range(len(intersection[0])):
            if intersection[0][cell] == 1:
                puzzle[row_index][col_index] = True
                colored_cells.add((row_index, col_index))
            if intersection[1][cell] == 0:
                puzzle[row_index][col_index] = False
                blank_cells.add((row_index, col_index))
            row_index += 1

        col_index += 1

    return colored_cells, blank_cells

def update_column_domains(colored_cells, blank_cells, cols_domains): # delete invalid configurations based on cells that are known to be black (1) or white (0)
    tmp = delete_invalid_rows(colored_cells, cols_domains, 1)
    cols_domains = delete_invalid_rows(blank_cells, tmp, 0)
    return cols_domains

def update_row_domains(colored_cells, blank_cells, rows_domains):# delete invalid configurations based on cells that are known to be black (1) or white (0)
    tmp = delete_invalid_cols(colored_cells, rows_domains, 1)
    rows_domains = delete_invalid_cols(blank_cells, tmp, 0)
    return rows_domains

if __name__ == "__main__":
    read_input()
    solve()
    with open("zad_output.txt", "w") as output:
        for i in range(DIMENSIONS[0]):
            for j in range(DIMENSIONS[1]):
                if puzzle[i][j]:
                    output.write('#')
                else:
                    output.write('.')
            output.write("\n")

