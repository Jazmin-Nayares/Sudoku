import sys
import copy
import pygame  #Para que se muestre en pantalla
from pygame.locals import *  #Para que se muestre en pantalla
from collections import deque #Para poder crear una cola

pygame.init()

# Dimensiones y colores
WIDTH, HEIGHT = 680, 680 #Tanaño de pantalla
GRID_SIZE = WIDTH // 9 #Tamaño de cada uno de los recuadros 
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)

#Dibujar tablero
def draw_board(board):
    for i in range(1, 9):
        pygame.draw.line(screen, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), 2 if i % 3 == 0 else 1)
        pygame.draw.line(screen, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT), 2 if i % 3 == 0 else 1)

    font = pygame.font.Font(None, 36) #Definir letra

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                if sudoku_board[i][j] == board[i][j]:
                    number_color = (128, 0, 128)  # Se asigna color morado a numeros inciales
                else:
                    number_color = BLACK  # Negro para números durante la búsqueda

                number = font.render(str(board[i][j]), True, number_color)
                screen.blit(number, (j * GRID_SIZE + GRID_SIZE // 3, i * GRID_SIZE + GRID_SIZE // 4))


#Verificar si el numero es valido
def is_valid(board, row, col, num):
    # Válido en la fila y columna
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Válido en el cuadro 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

#Busqueda de celdas
def find_empty_location(board):
    # Primera celda vacía en el tablero
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

#Resolver con bfs
def solve_sudoku(board):
    queue = deque([board])

    while queue:
        current_board = queue.popleft()

        # Tabla actual
        screen.fill(WHITE)
        draw_board(current_board)
        pygame.time.delay(800)  #Tiempo de retraso de pantalla inicial 
        pygame.display.flip()
        pygame.time.delay(400)  

        empty_location = find_empty_location(current_board)

        # Si no hay celdas vacías, el Sudoku está resuelto
        if not empty_location:
            return current_board

        row, col = empty_location

        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                # Utiliza deepcopy para hacer una copia profunda de la tabla
                new_board = copy.deepcopy(current_board)
                new_board[row][col] = num
                queue.append(new_board)

# Configuración de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku Solver')

# Asignacion de valores a el sudoku inicial
sudoku_board = [
    [5, 3, 4, 0, 7, 0, 0, 1, 0],
    [6, 0, 2, 1, 9, 5, 0, 0, 8],
    [0, 9, 8, 0, 4, 2, 0, 6, 0],
    [8, 0, 9, 7, 6, 0, 4, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

running = True
while running: #Se establece que se mantenga la ventana del juego abierta
    for event in pygame.event.get():
        #Si se llega a cerrar la ventana entonces el valor de running sera false por lo que se cerrara.
        if event.type == QUIT:
            running = False

    screen.fill(WHITE)
    draw_board(sudoku_board) #Dibujar el juego
    pygame.display.flip() #Actualiza el estado del board

    solution = solve_sudoku(sudoku_board) #Se continua resolviendo el juego

    if solution:
        sudoku_board = solution #En caso de que se logre terminar el juego aparece con los valores obtenidos a traves de bfs
    else:#Si no se encuentra solucion 
        print("No hay solución.") 
        running = False

    pygame.time.delay(100)  # Retraso para visualizar cada paso

pygame.quit()
sys.exit()


#Jazmin Carolina Moreno Nayares
#N.Control: 19691071
#Inteligencia Artificial 
