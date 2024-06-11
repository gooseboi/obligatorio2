import pygame
import render
import config


def crear_tablero_minas():
    # Genera un tablero de tamaño NxN y rellena cada celda con 0.
    # N está declarado en config.py, con el nombre LARGO_TABLERO.
    pass


def crear_tablero_revelado():
    # Genera un tablero de tamaño NxN y rellena cada celda con False.
    # N está declarado en config.py, con el nombre LARGO_TABLERO.
    pass


def plantar_bombas(tablero):
    # Coloca las bombas en el tablero de forma aleatoria.
    # La cantidad de bombas a colocar está definida en config.py
    # Para colocar una bomba, la celda correspondiente debe ser -1
    pass


def calcular_adyacentes(tablero):
    # Para cada celda sin una bomba, calcula cuantas bombas hay en las celdas de alrededor.
    # El resultado se guarda en la misma celda.
    pass


def revelar_celdas(fila, columna, tablero_minas, tablero_revelado):
    # Recibe una fila y una columna (la celda donde el jugador hizo click) y la "revela", o sea,
    # cambia la celda correspondiente en tablero_revelado a "True".
    # Si la celda de tablero_minas es -1, entonces la función devuelve -1.
    # Si la celda estaba vacía (0 u otro número positivo), entonces devuelve 0.
    # Si se revelaron todas las celdas vacías, entonces devuelve 1.
    pass

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
