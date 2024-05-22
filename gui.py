import random
import pygame
import sys
from board import create_board, apply_move, count_tiles, draw_board, draw_pieces
from moves import get_possible_moves
from minimax import best_move

# Configuración del tamaño del tablero y colores
BOARD_SIZE = 8
CELL_SIZE = 80
WINDOW_SIZE = BOARD_SIZE * CELL_SIZE
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

yoshi_green_image = pygame.image.load("./images/green_yoshi.png")
yoshi_red_image = pygame.image.load("./images/red_yoshi.png")

def draw_text(screen, text, position, font_size=30, color=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def select_difficulty(screen):
    screen.fill(WHITE)
    draw_text(screen, "Selecciona el nivel de dificultad:", (10, 10))
    draw_text(screen, "1. Principiante (profundidad 2)", (10, 40))
    draw_text(screen, "2. Amateur (profundidad 4)", (10, 70))
    draw_text(screen, "3. Experto (profundidad 6)", (10, 100))
    pygame.display.flip()
    
    level = None
    while level is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level = 1
                elif event.key == pygame.K_2:
                    level = 2
                elif event.key == pygame.K_3:
                    level = 3
    return level

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Yoshi\'s World')
    
    level = select_difficulty(screen)
    depth_levels = {1: 2, 2: 4, 3: 6}
    max_depth = depth_levels.get(level, 2)

    board = create_board()
    
    # Generar posiciones iniciales aleatorias para los Yoshis
    while True:
        yoshi_green_pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        yoshi_red_pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        if yoshi_green_pos != yoshi_red_pos:
            break

    apply_move(board, yoshi_green_pos, 'G')
    apply_move(board, yoshi_red_pos, 'R')

    current_player = 'G'
    yoshi_positions = {'G': yoshi_green_pos, 'R': yoshi_red_pos}

    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_board(screen, board, CELL_SIZE)
        draw_pieces(screen, board, CELL_SIZE)

        if not game_over:
            if current_player == 'G':
                pygame.display.flip()
                pygame.time.wait(500)
                current_position = best_move(board, yoshi_positions['G'], 'G', max_depth)
                if current_position:
                    apply_move(board, current_position, 'G')
                    yoshi_positions['G'] = current_position
                    current_player = 'R'
                else:
                    current_player = 'R'
            else:
                valid_moves = get_possible_moves(board, yoshi_positions['R'])
                if not valid_moves:
                    current_player = 'G'
                    continue
                
                # Esperar el movimiento del jugador
                move_made = False
                while not move_made:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            row = mouse_pos[1] // CELL_SIZE
                            col = mouse_pos[0] // CELL_SIZE
                            if (row, col) in valid_moves:
                                current_position = (row, col)
                                apply_move(board, current_position, 'R')
                                yoshi_positions['R'] = current_position
                                current_player = 'G'
                                move_made = True
                                break

            if not get_possible_moves(board, yoshi_positions['G']) and not get_possible_moves(board, yoshi_positions['R']):
                game_over = True

        screen.fill(WHITE)
        draw_board(screen, board, CELL_SIZE)
        draw_pieces(screen, board, CELL_SIZE)
        pygame.display.flip()

        if game_over:
            green_tiles = count_tiles(board, 'G')
            red_tiles = count_tiles(board, 'R')

            # Mostrar pantalla de resultados
            screen.fill(WHITE)
            draw_text(screen, f"Yoshi verde pintó {green_tiles} casillas.", (10, WINDOW_SIZE // 2 - 60))
            draw_text(screen, f"Yoshi rojo pintó {red_tiles} casillas.", (10, WINDOW_SIZE // 2 - 30))

            if green_tiles > red_tiles:
                draw_text(screen, "¡Yoshi verde, ha ganado la máquina!", (10, WINDOW_SIZE // 2), color=GREEN)
            elif red_tiles > green_tiles:
                draw_text(screen, "¡Yoshi rojo, has ganado tú!", (10, WINDOW_SIZE // 2), color=RED)
            else:
                draw_text(screen, "¡Es un empate!", (10, WINDOW_SIZE // 2), color=BLACK)
            
            pygame.display.flip()
            pygame.time.wait(10000)
            running = False

    pygame.quit()