import numpy as np
from itertools import combinations

def read_input():
    with open('zad_input.txt', 'r') as f:
        line = f.readline().split()
        rows, cols, rows_desc, cols_desc = int(line[0]), int(line[1]), [], []
        for _ in range(rows):
            line = f.readline().split()
            rows_desc.append([int(i) for i in line])
        for _ in range(cols):
            line = f.readline().split()
            cols_desc.append([int(i) for i in line])
        return rows, cols, rows_desc, cols_desc

desc = [[], []]
N = [0] * 2
N[0], N[1], desc[0], desc[1] = read_input()
row_correct = [False] * N[0]
col_correct = [False] * N[1]
picture = np.array([[False] * N[1]] * N[0])

def correct(rows_domains, cols_domains):
    i = 0
    for row in picture:
        if tuple(row) not in rows_domains[i]:
            return False
        i += 1
    for col in range(0, N[1]):
        if tuple(picture[:, col]) not in cols_domains[col]:
            return False
    return True

def generate_domains(idx):
    res = []
    for strip in desc[idx]:
        correct_combs = []
        for c in combinations(range(N[1^idx] - strip[-1] + 1), len(strip)):
            overlap = False
            for i in range(1, len(c)):
                if c[i-1] + strip[i-1] >= c[i]:
                    overlap = True
                    break
            if not overlap:
                new = [0] * N[1^idx]
                k = 0
                for i in c:
                    for j in range(i, i + strip[k]):
                        new[j] = 1
                    k += 1
                correct_combs.append(new)
        res.append({tuple(i) for i in correct_combs})
    return res

def find_intersection(domain):
    intersetion1 = list(list(domain)[0])
    intersetion0 = list(list(domain)[0])
    for solution in domain:
        for i in range(0, len(solution)):
            if intersetion1[i] == solution[i] and solution[i] == 1:
                intersetion1[i] = 1
            else:
                intersetion1[i] = 0
            if intersetion0[i] == solution[i] and solution[i] == 0:
                intersetion0[i] = 0
            else:
                intersetion0[i] = 1
    return (intersetion1, intersetion0)

def clear_row_domain(cells, domain, color):
    for r, c in cells:
        incorrect = []
        for solution in domain[c]:
            if solution[r] != color:
                incorrect.append(solution)
        for rm in incorrect:
            domain[c] -= {rm}
    return domain

def clear_col_domain(cells, domain, color):
    for r, c in cells:
        incorrect = []
        for solution in domain[r]:
            if solution[c] != color:
                incorrect.append(solution)
        for rm in incorrect:
            domain[r] -= {rm}
    return domain

def solve():
    rows_domain = generate_domains(0)
    cols_domain = generate_domains(1)

    while not correct(rows_domain, cols_domain):

        colored_cells, blank_cells = set(), set()
        r = 0
        for row in rows_domain:
            c = 0
            intersection = find_intersection(row)
            for cell in range(0, len(intersection[0])):
                if intersection[0][cell] == 1:
                    picture[r][c] = True
                    colored_cells.add((r, c))
                    
                if intersection[1][cell] == 0:
                    picture[r][c] = False
                    blank_cells.add((r, c))
                c += 1
            r += 1
        cols_domain = clear_row_domain(colored_cells, cols_domain, 1)
        cols_domain = clear_row_domain(blank_cells, cols_domain, 0)

        colored_cells, blank_cells = set(), set()
        c = 0
        for col in cols_domain:
            r = 0
            intersection = find_intersection(col)
            for cell in range(0, len(intersection[0])):
                if intersection[0][cell] == 1:
                    picture[r][c] = True
                    colored_cells.add((r, c))

                if intersection[1][cell] == 0:
                    picture[r][c] = False
                    blank_cells.add((r, c))
                r += 1
            c += 1
        rows_domain = clear_col_domain(colored_cells, rows_domain, 1)
        rows_domain = clear_col_domain(blank_cells, rows_domain, 0)

solve()

def write_picture(picture):
    with open("zad_output.txt", "w") as output:
        for i in range(N[0]):
            for j in range(N[1]):
                if picture[i][j]:
                    output.write('#')
                else:
                    output.write('.')
            output.write("\n")

write_picture(picture)