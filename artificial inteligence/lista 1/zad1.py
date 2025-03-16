# Idea:
# We solve the problem using BFS.
# New states are generated based on positions that can be reached from the current state (player whoes turn it is, pawns' positions).

from collections import deque
import sys

def rook_attacks_king(wk,wr,bk):
    if(wr[0] == bk[0]): #same row
        if wk[0] == wr[0]:
            if wr[1] < wk[1] < bk[1] or bk[1] < wk[1] < wr[1]: # if wk covers bk
                return False
        return True
    if(wr[1] == bk[1]): #same column
        if wk[1] == wr[1]:
            if wr[0] < wk[0] < bk[0] or bk[0] < wk[0] < wr[0]: # if wk covers bk
                return False
        return True
    return False

def pos_covered_by_king(px,py,wk):
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            nx = px + dx
            ny = py + dy
            if nx == wk[0] and ny == wk[1]:
                return True
    return False

def can_bk_hide(wk,wr,bk):
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue
            nx,ny = bk[0],bk[1]
            nx += dx
            ny += dy
            if 1 <= ny <= 8 and 1 <= nx <= 8 and (not pos_covered_by_king(nx,ny,wk)) and (not rook_attacks_king(wk,wr,(nx,ny))):
                return True
            if (nx,ny) == wr and (not pos_covered_by_king(nx,ny,wk)): #when bk can beat wr
                return True
    return False

def is_checkmate(turn, wk, wr, bk):
    if turn == "white":
        return False
    
    if rook_attacks_king(wk,wr,bk):
        return not can_bk_hide(wk,wr,bk)

def get_following_moves(turn, wk, wr, bk, prev_moves):
    new_prev_moves = prev_moves+[(wk,wr,bk)]
    res = []

    if turn == "white":
        #wk moves
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx == 0 and dy == 0:
                    continue
                nx,ny = wk
                nx += dx
                ny += dy
                if 1 <= nx <= 8 and 1 <= ny <= 8 and (not pos_covered_by_king(nx,ny,bk)):
                    res.append(("black",(nx,ny), wr, bk, new_prev_moves))
        #wr moves
        for dx,dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for i in range(1, 8):
                nx, ny = wr[0] + dx * i, wr[1] + dy * i
                if 1 <= nx <= 8 and 1 <= ny <= 8 and (nx,ny) != wk and (nx,ny) != bk:
                    res.append(("black",wk,(nx,ny),bk,new_prev_moves))
                else:
                    break
    else:
        #bk moves
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx == 0 and dy == 0:
                    continue
                nx,ny = bk
                nx += dx
                ny += dy
                if 1 <= nx <= 8 and 1 <= ny <= 8 and (not pos_covered_by_king(nx,ny,wk)) and (not rook_attacks_king(wk,wr,(nx,ny))):
                    res.append(("white",wk,wr,(nx,ny),new_prev_moves))
                if (nx,ny) == wr:
                    res.append(("white",wk,wr,(nx,ny),new_prev_moves))
    return res

def parse_pos(x): #b4 -> (2,4)
    return (ord(x[0]) - ord('a') + 1, int(x[1]))

def parse_back(x): #(3,7) -> c7
    return chr(x[0] - 1 +ord('a')) + f"{x[1]}"

def min_no_moves_till_checkmate(turn, wk, wr, bk):
    moves = deque([(turn,wk,wr,bk,[])])
    tried = set()
    
    while moves:
        t, k, r, cbk, prev_moves = moves.popleft()
        if r != cbk: # if black king beated the rook its pat
            if is_checkmate(t, k, r, cbk):
                return prev_moves + [(parse_back(k), parse_back(r), parse_back(cbk))]

            for move in get_following_moves(t, k, r, cbk, prev_moves):
                t2,cwk,cwr,ccbk,tmp = move
                if tried.isdisjoint([(cwk,cwr,ccbk)]):
                    moves.append((t2, cwk, cwr, ccbk, prev_moves + [(parse_back(k), parse_back(r), parse_back(cbk))]))
                    tried.add((cwk,cwr,ccbk))
    return "INF"

def draw_board(wk,wr,bk):

    wk = parse_pos(wk)
    wr = parse_pos(wr)
    bk = parse_pos(bk)

    board = [["__" for _ in range(8)] for _ in range(8)]

    board[8 - wk[1]][wk[0] - 1] = "WK"
    board[8 - wr[1]][wr[0] - 1] = "WR"
    board[8 - bk[1]][bk[0] - 1] = "BK"

    print("   a   b   c   d   e   f   g   h")
    for i, row in enumerate(board):
        print(f"{8 - i} {'  '.join(row)}")
    print("   a   b   c   d   e   f   g   h\n")


def solve(input, output, mode=False):
    with open(input,'r') as f:
        lines = f.readlines()
    
    results = []
    for line in lines:
        turn, normal_wk, normal_wr, normal_bk = line.strip().split()
        result = min_no_moves_till_checkmate(turn, parse_pos(normal_wk),
                                            parse_pos(normal_wr), parse_pos(normal_bk))

        if mode:
            with open(output,'w') as f:
                for state in result:
                    f.write(f"{state}\n")
                    draw_board(state[0], state[1], state[2])
            f.close()
        else:
            with open(output,'w') as f:
                f.write(f"{len(result)-1}")
            f.close()

if __name__ == "__main__":
    debug_mode = '--debug' in sys.argv
    solve("zad1_input.txt", "zad1_output.txt", debug_mode)