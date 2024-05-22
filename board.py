import pygame

BOARD_SIZE = 8

def create_board():
    return [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def apply_move(board, position, player):
    board[position[0]][position[1]] = player

def count_tiles(board, player):
    return sum(row.count(player) for row in board)

def draw_board(screen, board, cell_size):
    screen.fill((255, 255, 255))  # Llenar el fondo de blanco
    for row in range(len(board)):
        for col in range(len(board[row])):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

def draw_pieces(screen, board, cell_size):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'G':
                pygame.draw.circle(screen, (0, 255, 0), (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 3)
            elif board[row][col] == 'R':
                pygame.draw.circle(screen, (255, 0, 0), (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 3)
