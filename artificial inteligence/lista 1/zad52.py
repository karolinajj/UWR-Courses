import numpy as np
import random
from opt_dist import opt_dist

MAX_ITER = 1000000

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

def fix_row(row_index, tab, rows, R):


def fix_col(col_index, tab, cols, C):


def solve(tab, rows, cols):
    for _ in range(MAX_ITER):
        row_index = select_wrong_row(tab, rows)
        if row_index > -1:
            fix_row(row_index, tab, rows, R)
        
        col_index = select_wrong_col(tab, cols)
        if col_index > -1:
            fix_col(col_index, tab, cols, C)
        
        if select_wrong_row(tab, rows) == -1 and select_wrong_col(tab, cols) == -1:
            # print(tab)
            return True, tab
        
    return False, tab

def main():
    global R, C
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

    R = rows_num
    C = cols_num
    tab = initialize(rows_num, cols_num)
    solved_tab = solve(tab, rows, cols)
    print(solved_tab)

main()
