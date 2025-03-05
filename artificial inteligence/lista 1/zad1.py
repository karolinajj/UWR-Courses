from queue import Queue

DIMENSION = 8

def correct_moves(pawn_type, position, w_king, w_rook, b_king):
    """
    Returns a set of valid moves for a king (pawn_type = 0) or a rook (pawn_type = 1).
    The moves are validated to ensure the king does not move into check.
    """
    moves = set()
    letter = position[0]
    number = int(position[1])
    
    if pawn_type == 0:  # King moves
        for i in range(max(1, number - 1), min(DIMENSION, number + 1) + 1):
            for j in range(max(ord('a'), ord(letter) - 1), min(ord('a') + DIMENSION, ord(letter) + 1) + 1):
                move = f"{chr(j)}{i}"
                if move != position or (position == b_king and not is_check(w_king, w_rook, move)):  # Exclude current position and moves where king is in check
                    moves.add(move)
    
    else:  # Rook moves
        for i in range(1, DIMENSION + 1):  # Vertical moves
            move = f"{letter}{i}"
            if move != position:
                moves.add(move)
        
        for i in range(0, DIMENSION):  # Horizontal moves
            move = f"{chr(ord('a') + i)}{number}"
            if move != position:
                moves.add(move)

    return moves

def opponent(player):
    """
    Returns the opponent's color.
    """
    return 'black' if player == 'white' else 'white'

def is_check(w_king, w_rook, b_king):
    """
    Returns True if the white rook is attacking the black king.
    """
    if w_rook[0] == b_king[0] or w_rook[1] == b_king[1]:  # Same row or column
        rook_file, rook_rank = w_rook[0], int(w_rook[1])
        king_file, king_rank = b_king[0], int(b_king[1])

        # Check if the white king is blocking the check
        if rook_file == king_file:  # Same column
            for i in range(min(rook_rank, king_rank) + 1, max(rook_rank, king_rank)):
                if f"{rook_file}{i}" == w_king:
                    return False
        else:  # Same row
            for j in range(min(ord(rook_file), ord(king_file)) + 1, max(ord(rook_file), ord(king_file))):
                if f"{chr(j)}{rook_rank}" == w_king:
                    return False
        return True
    return False

def is_mate(w_king, w_rook, b_king):
    """
    Returns True if black king is in checkmate.
    """
    if not is_check(w_king, w_rook, b_king):  # First, check if black king is in check
        return False

    # Check if black king has any legal escape moves
    for move in correct_moves(0, b_king, w_king, w_rook, b_king):
        if not is_check(w_king, w_rook, move):  # If there's a safe move, it's not checkmate
            return False

    return True  # No escape moves → Checkmate

def bfs(player, w_king, w_rook, b_king):
    """
    Breadth-first search (BFS) to find the minimum number of moves to checkmate.
    """
    queue = Queue()
    visited = set()
    queue.put([(player, w_king, w_rook, b_king)])

    while not queue.empty():
        state = queue.get()
        player, w_king, w_rook, b_king = state[-1]  # Get the last state
        current = (player, w_king, w_rook, b_king)

        if current in visited:
            continue
        visited.add(current)

        if is_mate(w_king, w_rook, b_king):

            print(correct_moves(0, b_king, w_king, w_rook, b_king))
            return state  # Return the number of moves taken

        if player == 'black':  # Black moves
            moves = correct_moves(0, b_king, w_king, w_rook, b_king)
            for move in moves:
                if move not in visited:
                    queue.put(state + [(opponent(player), w_king, w_rook, move)])

        else:  # White moves
            king_moves = correct_moves(0, w_king, w_king, w_rook, b_king)
            rook_moves = correct_moves(1, w_rook, w_king, w_rook, b_king)

            for move in king_moves:
                if move not in visited:
                    queue.put(state + [(opponent(player), move, w_rook, b_king)])

            for move in rook_moves:
                if move not in visited:
                    queue.put(state + [(opponent(player), w_king, move, b_king)])

    return "INF"  # If no solution is found

# Example Test
player, w_king, w_rook, b_king = 'black', 'b4', 'f3', 'e8'
print(bfs(player, w_king, w_rook, b_king))

# Read input from file and process multiple cases
# with open('zad1_input.txt', 'r', encoding='utf-8') as lines, open('zad1_output.txt', 'w', encoding='utf-8') as results:
#     for line in lines:
#         line = line.strip()
#         if line:
#             player, w_king, w_rook, b_king = line.split()
#             result = bfs(player, w_king, w_rook, b_king)
#             results.write(str(result) + '\n')
