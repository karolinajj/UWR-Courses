from queue import Queue

DIMENSION = 8

# Define board directions for king moves
KING_MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_valid(position):
    """Check if a position is within board bounds."""
    return 'a' <= position[0] <= 'h' and 1 <= int(position[1]) <= 8

def correct_moves(pawn_type, position, w_king, w_rook, b_king):
    """
    Returns a set of valid moves for a king (pawn_type = 0) or a rook (pawn_type = 1).
    Ensures the king does not move into check.
    """
    moves = set()
    letter, number = position[0], int(position[1])
    
    if pawn_type == 0:  # King moves
        for dx, dy in KING_MOVES:
            new_letter = chr(ord(letter) + dx)
            new_number = number + dy
            move = f"{new_letter}{new_number}"
            if is_valid(move) and move != w_rook and move != w_king:
                moves.add(move)
    
    else:  # Rook moves
        for i in range(1, DIMENSION + 1):
            move = f"{letter}{i}"
            if move != position and move != b_king:
                moves.add(move)
        for j in range(ord('a'), ord('h') + 1):
            move = f"{chr(j)}{number}"
            if move != position and move != b_king:
                moves.add(move)
    
    return moves

def is_check(w_king, w_rook, b_king):
    """Returns True if the white rook is attacking the black king."""
    if w_rook[0] == b_king[0] or w_rook[1] == b_king[1]:  # Same row or column
        for i in range(min(ord(w_rook[0]), ord(b_king[0])) + 1, max(ord(w_rook[0]), ord(b_king[0]))):
            if f"{chr(i)}{w_rook[1]}" == w_king:
                return False
        for j in range(min(int(w_rook[1]), int(b_king[1])) + 1, max(int(w_rook[1]), int(b_king[1]))):
            if f"{w_rook[0]}{j}" == w_king:
                return False
        return True
    return False

def is_mate(w_king, w_rook, b_king):
    """Returns True if black king is in checkmate."""
    if not is_check(w_king, w_rook, b_king):
        return False
    for move in correct_moves(0, b_king, w_king, w_rook, b_king):
        if not is_check(w_king, w_rook, move):
            return False
    return True

def bfs(player, w_king, w_rook, b_king):
    """Find the minimum number of moves to checkmate using BFS and print the game state at each step."""
    queue = Queue()
    visited = set()
    queue.put((player, w_king, w_rook, b_king, 0, []))
    
    while not queue.empty():
        player, w_king, w_rook, b_king, moves, path = queue.get()
        state = (player, w_king, w_rook, b_king)
        
        if state in visited:
            continue
        visited.add(state)
        
        if is_mate(w_king, w_rook, b_king):
            print("Moves taken:", path)
            return moves
        
        if player == 'black':  # Black moves
            for move in correct_moves(0, b_king, w_king, w_rook, b_king):
                queue.put((opponent(player), w_king, w_rook, move, moves + 1, path + [(player, w_king, w_rook, move)]))
        else:  # White moves (king or rook)
            for move in correct_moves(0, w_king, w_king, w_rook, b_king):
                queue.put((opponent(player), move, w_rook, b_king, moves + 1, path + [(player, move, w_rook, b_king)]))
            for move in correct_moves(1, w_rook, w_king, w_rook, b_king):
                queue.put((opponent(player), w_king, move, b_king, moves + 1, path + [(player, w_king, move, b_king)]))
    
    return "INF"

def opponent(player):
    """Returns the opponent's color."""
    return 'black' if player == 'white' else 'white'

player, w_king, w_rook, b_king = 'black', 'g8', 'h1', 'c4'
print(bfs(player, w_king, w_rook, b_king))
# Read input from file and process multiple cases
# with open('zad1_input.txt', 'r', encoding='utf-8') as infile, open('zad1_output.txt', 'w', encoding='utf-8') as outfile:
#     for line in infile:
#         player, w_king, w_rook, b_king = line.strip().split()
#         result = bfs(player, w_king, w_rook, b_king)
#         outfile.write(str(result) + '\n')
