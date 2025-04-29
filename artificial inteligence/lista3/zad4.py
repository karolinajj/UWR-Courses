# Idea:
# Each cell can be empty (0) or not (1)
# We eliminate incorrect arrangements (presented during a lecture):
#   - threes: (0,1,0) in rows and column
#   - squares: (ex. 10  11
#                   01  10)
# We make sure that the sums of non-empty cells in rows and cols match the descriptions
# We add fixed cells (triples) to the constraints.

def B(i,j):
    return 'B_%d_%d' % (i,j)
    
def domains(Bs): #specifies that each variable can be either 0 or 1
    return [b + ' in 0..1' for b in Bs]

# ------------------------------------------------------
# from lecture (forbidden arrangement)
# prevents 0,1,0 in columns
def inccorect_cols_threes(R, C): 
    res = []
    for i in range(1, R-1):
        for j in range(C):
            res.append(B(i - 1, j) + " + 2 * " + B(i, j) + " + 3 * " + B(i + 1, j) + " #\\= 2")
    return res

# prevents 0,1,0 in rows
def inccorect_rows_threes(R, C):
    res = []
    for i in range(R):
        for j in range(1, C-1):
            res.append(B(i, j-1) + " + 2 * " + B(i, j) + " + 3 * " + B(i, j+1) + " #\\= 2")
    return res

# prevents inccorect squares
def incorrect_squares(R, C):
    res, forbidden = [], [6, 7, 9, 11, 13, 14]
    for i in range(R - 1):
        for j in range(C - 1):
            for f in forbidden:
                res.append(B(i, j) + " + 2 * " + B(i, j + 1) + " + 4 * " + B(i + 1, j) + " + 8 * " + B(i + 1, j + 1) + " #\\= " + str(f))
    return res

# ------------------------------------------------------

def cols_sums(R, C):
    res = []
    for j in range(C):
        s = ""
        for i in range(R):
            s += B(i, j)
            if i != R - 1:
                s += " + "
        s += " #= " + str(cols[j])
        res.append(s)
    return res

def rows_sums(R, C):
    res = []
    for i in range(R):
        s = ""
        for j in range(C):
            s += B(i, j)
            if j != C - 1:
                s += " + "
        s += " #= " + str(rows[i])
        res.append(s)
    return res

# fixed cells
def fixed_cells(triples):
    res = []
    for i, j, k in triples:
        res.append( '%s #= %d' % (B(i,j), k) )
    return res

# ------------------------------------------------------

def storms(rows, cols, triples):
    print(':- use_module(library(clpfd)).')
    
    R = len(rows)
    C = len(cols)
    
    bs = [ B(i,j) for i in range(R) for j in range(C)]
    
    print('solve([' + ', '.join(bs) + ']) :- ')

    constraints = domains(bs) + inccorect_cols_threes(R, C) + inccorect_rows_threes(R, C) + incorrect_squares(R, C) + cols_sums(R, C) + rows_sums(R, C) + fixed_cells(triples)

    for constraint in constraints:
        print(constraint + ',')

    #print('    [%s] = [1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0],' % (', '.join(bs),)) #only for test 1

    print('    labeling([ff], [' +  ', '.join(bs) + ']).' )
    print('')
    print(":- tell('prolog_result.txt'), solve(X), write(X), nl, told.")

def print(s):
    output.write(s + '\n')

if __name__ == "__main__":
    txt = open('zad_input.txt').readlines()
    output = open('zad_output.txt', 'w')

    rows = list(map(int, txt[0].split()))
    cols = list(map(int, txt[1].split()))
    triples = []

    for i in range(2, len(txt)):
        if txt[i].strip():
            triples.append(list(map(int, txt[i].split())))

    storms(rows, cols, triples)            
        
