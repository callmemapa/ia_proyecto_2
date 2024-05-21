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

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Yoshi\'s World')
    
    board = create_board()
    
    # Generar posiciones iniciales aleatorias para los Yoshis
    while True:
        yoshi_green_pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        yoshi_red_pos = (random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
        if yoshi_green_pos != yoshi_red_pos:
            break

    apply_move(board, yoshi_green_pos, 'G')
    apply_move(board, yoshi_red_pos, 'R')

    print("Selecciona el nivel de dificultad:")
    print("1. Principiante (profundidad 2)")
    print("2. Amateur (profundidad 4)")
    print("3. Experto (profundidad 6)")
    level = int(input("Ingresa el nivel de dificultad: "))

    depth_levels = {1: 2, 2: 4, 3: 6}
    max_depth = depth_levels.get(level, 2)

    current_player = 'G'
    yoshi_positions = {'G': yoshi_green_pos, 'R': yoshi_red_pos}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_board(screen, board, CELL_SIZE)
        draw_pieces(screen, board, CELL_SIZE)

        pygame.display.flip()
        
        if current_player == 'G':
            print("Turno de Yoshi verde (computadora):")
            current_position = best_move(board, yoshi_positions['G'], 'G', max_depth)
            if current_position:
                apply_move(board, current_position, 'G')
                yoshi_positions['G'] = current_position
                current_player = 'R'
            else:
                print("Yoshi verde no puede moverse.")
                current_player = 'R'
        else:
            print("Turno de Yoshi rojo (tú):")
            valid_moves = get_possible_moves(board, yoshi_positions['R'])
            if not valid_moves:
                print("Yoshi rojo no puede moverse.")
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
            break

    green_tiles = count_tiles(board, 'G')
    red_tiles = count_tiles(board, 'R')

    print(f"Yoshi verde pintó {green_tiles} casillas.")
    print(f"Yoshi rojo pintó {red_tiles} casillas.")

    if green_tiles > red_tiles:
        print("¡Yoshi verde (computadora) gana!")
    elif red_tiles > green_tiles:
        print("¡Yoshi rojo (tú) gana!")
    else:
        print("¡Es un empate!")

    pygame.quit()

if __name__ == "__main__":
    main()
