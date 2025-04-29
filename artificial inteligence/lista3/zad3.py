#Idea:
# Each number (1 – 9) can only appear once per row, column, and 3x3 square.
# The domain for each variable (cell) initially is all numbers from 1 to 9.
# The first variable selected by ff is the one that has the fewest valid numbers left in its domain.
# The labeling process continues, trying to assign values while adhering to these constraints.

import sys

#returns a name of varaible in (i,j)
def V(i,j):
    return 'V%d_%d' % (i,j)

#List of constraints for the variables Vs
# (must be integers from 1 to 9)
def domains(Vs):
    return [ q + ' in 1..9' for q in Vs ]

#enforcing all the elements in list to be different
def all_different(Qs):
    return 'all_distinct([' + ', '.join(Qs) + '])'
    
def get_column(j):
    return [V(i,j) for i in range(9)] 
            
def get_row(i):
    return [V(i,j) for j in range(9)] 
                        
def distinct_rows():   
    return [all_different(get_row(i)) for i in range(9)]

def distinct_cols():
    return [all_different(get_column(j)) for j in range(9)]

def squares(grid_size=9, block_size=3):
    constraints = []
    for block_row in range(0, grid_size, block_size):
        for block_col in range(0, grid_size, block_size):
            block_vars = [
                V(block_row + i, block_col + j)
                for i in range(block_size)
                for j in range(block_size)
            ]
            constraints.append(all_different(block_vars))
    return constraints

def print_constraints(constraints, indent, d):
    position = indent
    print(indent * ' ', end='')
    for constraint in constraints:
        print(constraint + ',', end=' ')
        position += len(constraint)
        if position > d:
            position = indent
            print()
            print(indent * ' ', end='')
      
def sudoku(assigments, grid_size=9):
    variables = [ V(i,j) for i in range(grid_size) for j in range(grid_size)]
    
    print (':- use_module(library(clpfd)).')
    print ('solve([' + ', '.join(variables) + ']) :- ')
    
    
    cs = domains(variables) + distinct_cols() + distinct_rows() + squares()
    for i,j,val in assigments:
        cs.append( '%s #= %d' % (V(i,j), val) )
    
    print_constraints(cs, 4, 80),
    print ()
    print ('    labeling([ff], [' +  ', '.join(variables) + ']).' )
    print ()
    print (':- solve(X), write(X), nl.')       

if __name__ == "__main__":
    input_file = open("zad_input.txt", "r", encoding='utf8').readlines()
    output_file = open("zad_output.txt", "w", encoding='utf8')
    
    orig_stdout = sys.stdout
    sys.stdout = output_file

    row = 0
    triples = []
    
    for x in input_file:
        x = x.strip()
        if len(x) == 9:
            for col in range(9):
                if x[col] != '.':
                    triples.append((row, col, int(x[col]))) 
            row += 1          
    sudoku(triples)

    sys.stdout = orig_stdout
    output_file.close()

#---------------------------------------------------
#input:

"""
89.356.1.
3...1.49.
....2985.
9.7.6432.
.........
.6389.1.4
.3298....
.78.4....
.5.637.48

53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79

3.......1
4..386...
.....1.4.
6.924..3.
..3......
......719
........6
2.7...3..
"""