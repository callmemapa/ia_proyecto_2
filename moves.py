BOARD_SIZE = 8

# Movimientos posibles del caballo en ajedrez
KNIGHT_MOVES = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

def get_possible_moves(board, position):
    possible_moves = []
    for move in KNIGHT_MOVES:
        new_row = position[0] + move[0]
        new_col = position[1] + move[1]
        if is_valid_move(board, new_row, new_col):
            possible_moves.append((new_row, new_col))
    return possible_moves

def is_valid_move(board, row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == ' '
