from moves import get_possible_moves
from board import apply_move, count_tiles

def minimax(board, depth, is_maximizing, position, player, max_depth):
    opponent = 'R' if player == 'G' else 'G'
    possible_moves = get_possible_moves(board, position)
    
    if depth == max_depth or not possible_moves:
        return count_tiles(board, player) - count_tiles(board, opponent)

    if is_maximizing:
        best_score = float('-inf')
        for move in possible_moves:
            new_board = []
            for row in board:
                new_board.append(row[:])
            apply_move(new_board, move, player)
            score = minimax(new_board, depth + 1, False, move, player, max_depth)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in possible_moves:
            new_board = []
            for row in board:
                new_board.append(row[:])
            apply_move(new_board, move, opponent)
            score = minimax(new_board, depth + 1, True, move, opponent, max_depth)
            best_score = min(score, best_score)
        return best_score

def best_move(board, position, player, max_depth):
    best_score = float('-inf')
    best_move = None
    possible_moves = get_possible_moves(board, position)
    for move in possible_moves:
        new_board = []
        for row in board:
            new_board.append(row[:])
        apply_move(new_board, move, player)
        score = minimax(new_board, 1, False, move, player, max_depth)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
