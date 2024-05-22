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

def draw_pieces(screen, board, cell_size, yoshi_green_image, yoshi_red_image, yoshi_green_pos, yoshi_red_pos):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (row, col) == yoshi_green_pos:
                screen.blit(yoshi_green_image, (col * cell_size, row * cell_size))  # Ajuste de posición
            elif (row, col) == yoshi_red_pos:
                screen.blit(yoshi_red_image, (col * cell_size, row * cell_size))  # Ajuste de posición
            elif board[row][col] == 'G':
                pygame.draw.rect(screen, (0, 255, 0), (col * cell_size, row * cell_size, cell_size, cell_size))
            elif board[row][col] == 'R':
                pygame.draw.rect(screen, (255, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size))