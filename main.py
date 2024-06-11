import pygame
import render
import config
import random

def crear_tablero_minas():
    return [[0 for _ in range(config.LARGO_TABLERO)] for _ in range(config.LARGO_TABLERO)]


def crear_tablero_revelado():
    return [[False for _ in range(config.LARGO_TABLERO)] for _ in range(config.LARGO_TABLERO)]


def plantar_bombas(tablero):
    for _ in range(config.NUM_MINAS):
        pos_x = random.randint(0, config.LARGO_TABLERO-1)
        pos_y = random.randint(0, config.LARGO_TABLERO-1)
        while tablero[pos_x][pos_y] == -1:
            pos_x = random.randint(0, config.LARGO_TABLERO-1)
            pos_y = random.randint(0, config.LARGO_TABLERO-1)
        tablero[pos_x][pos_y] = -1

def calcular_adyacentes(tablero):
    for y in range(len(tablero)):
        for x in range(len(tablero[y])):
            if tablero[y][x] == -1:
                continue
            count = 0
            max_coord = config.LARGO_TABLERO - 1

            if y != 0:
                if x != 0:
                    count += (tablero[y-1][x-1] == -1)
                count += (tablero[y-1][x] == -1)
                if x != max_coord:
                    count += (tablero[y-1][x+1] == -1)

            if x != 0:
                count += (tablero[y][x-1] == -1)
            if x != max_coord:
                count += (tablero[y][x+1] == -1)

            if y != max_coord:
                if x != 0:
                    count += (tablero[y+1][x-1] == -1)
                count += (tablero[y+1][x] == -1)
                if x != max_coord:
                    count += (tablero[y+1][x+1] == -1)

            tablero[y][x] = count


def revelar_celdas(fila, columna, tablero_minas, tablero_revelado):
    tablero_revelado[fila][columna] = True
    if tablero_minas[fila][columna] == -1:
        return -1
    else:
        for x in range(len(tablero_revelado)):
            for y in range(len(tablero_revelado[x])):
                if tablero_revelado[x][y]:
                    return 0
        return 1

#======================================
# A partir de acá no se puede modificar
#======================================
if __name__ == "__main__": # Esto es solo para indicarle a Pycharm que arranque la ejecución por acá.
    # Configuración inicial
    tablero_minas = crear_tablero_minas()  # Matriz de enteros, que representa el tablero de juego
    tablero_revelado = crear_tablero_revelado()  # Matriz de booleanos, que representa si cada celda está revelada o no.
    plantar_bombas(tablero_minas)  # Agregamos las minas de forma aleatoria
    calcular_adyacentes(tablero_minas)  # Agregamos los números en las celdas

    # Bucle principal del juego
    juego_terminado = 0
    while juego_terminado == 0:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                render.salir("")  # Salimos antes de tiempo.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                fila = pygame.mouse.get_pos()[1] // config.CELL_SIZE
                columna = pygame.mouse.get_pos()[0] // config.CELL_SIZE
                juego_terminado = revelar_celdas(fila, columna, tablero_minas, tablero_revelado)

        # Dibuja el tablero
        # Si quieren agregar una imagen de fondo, descárgenla y pongan la ruta en config.imagen_fondo
        render.dibujar_tablero(tablero_minas, tablero_revelado)

    # Salimos
    if juego_terminado == -1:
        render.salir("¡PERDISTE!")
    else:
        render.salir("¡GANASTE!")
