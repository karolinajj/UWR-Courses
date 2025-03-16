# Idea: for each incorrect column / row
# I correct the field which is the most optimal in this columne / row (based on opt_dist func)
import numpy as np
import random
from opt_dist import opt_dist

MAX_ITER = 90000

def initialize(rows_num, cols_num):
    return [[0] * cols_num for _ in range(rows_num)]


def select_wrong_row(tab, rows):
    wrong = []
    for i in range(len(tab)):
        if opt_dist(tab[i], rows[i]) != 0:
            # print(tab[i], rows[i])
            wrong.append(i)

    if len(wrong) > 0:
        return np.random.choice(wrong)
    return -1

def select_wrong_col(tab, cols):
    wrong = []

    for i in range(len(tab[0])):
        col = [tab[j][i] for j in range(len(tab))]
        if opt_dist(col, cols[i]) != 0:
            wrong.append(i)

    if len(wrong) > 0:
        return np.random.choice(wrong)
    return -1

def fix_row(row_index, tab, rows, cols_num):
    row_to_fix = tab[row_index]
    best_index = 0
    best_score = cols_num

    for i in range(cols_num):
        new_row = row_to_fix[:i] + [row_to_fix[i] ^ 1] + row_to_fix[i+1:]
        new_score = opt_dist(new_row,rows[row_index])
        if new_score < best_score:
            best_score = new_score
            best_index = i
    
    tab[row_index][best_index] ^= 1
    if random.randint(1, 100) == 1:
        random_index = random.randint(0,cols_num - 1)
        tab[row_index][random_index] ^= 1
    else:
        tab[row_index][best_index] ^= 1
    return tab


def fix_col(col_index, tab, cols, rows_num):
    col_to_fix = [tab[i][col_index] for i in range(rows_num)]
    best_index = 0
    best_score = rows_num

    for i in range(rows_num):
        new_col = col_to_fix[:i] + [col_to_fix[i] ^ 1] + col_to_fix[i+1:]
        new_score = opt_dist(new_col,cols[col_index])
        if new_score < best_score:
            best_score = new_score
            best_index = i

    if random.randint(1, 100) == 1:
        random_index = random.randint(0,rows_num - 1)
        tab[random_index][col_index] ^= 1
    else:
        tab[best_index][col_index] ^= 1
    return tab
    


def solve(tab, rows, cols, rows_num, cols_num):
    for _ in range(MAX_ITER):
        row_index = select_wrong_row(tab, rows)
        if row_index > -1:
            tab = fix_row(row_index, tab, rows, cols_num)
        
        col_index = select_wrong_col(tab, cols)
        if col_index > -1:
            tab = fix_col(col_index, tab, cols, rows_num)
        
        if select_wrong_row(tab, rows) == -1 and select_wrong_col(tab, cols) == -1:
            # print(tab)
            return True, tab
        
    return False, tab

def draw_tab(tab):
    with open("zad5_output.txt", "w") as file:
        for row in tab:
            row_str = "".join(['.' if cell == 0 else '#' for cell in row])
            file.write(row_str + "\n")
    file.close()


def main():
    random.seed()
    with open('zad5_input.txt', 'r') as file:
        line = file.readline().split()
        rows_num, cols_num = int(line[0]), int(line[1])
        rows, cols = [], []

        for _ in range(rows_num):
            line = file.readline().split()
            rows.append(int(line[0]))

        for _ in range(cols_num):
            line = file.readline().split()
            cols.append(int(line[0]))

    # tab = initialize(rows_num, cols_num)
    # is_solved, solved_tab = solve(tab, rows, cols, rows_num, cols_num)

    is_solved = False
    while not is_solved:
        tab = initialize(rows_num, cols_num)
        is_solved, solved_tab = solve(tab, rows, cols, rows_num, cols_num)
          
    draw_tab(solved_tab)
    # print(solved_tab)

main()
