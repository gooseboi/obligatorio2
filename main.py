import random
import pygame
import render
import config


def crear_tablero_minas():
    """
    Retorna un tablero cuadrado, donde todos los elementos de la matriz son `0`.
    Las dimensiones del tablero son contraladas por la global `config.LARGO_TABLERO`.
    """

    # Generar LARGO_TABLERO listas, cada una con LARGO_TABLERO elementos.
    return [[0 for _ in range(config.LARGO_TABLERO)] for _ in range(config.LARGO_TABLERO)]


def crear_tablero_revelado():
    """
    Retorna un tablero cuadrado, donde todos los elementos de la matriz son `False`.
    Las dimensiones del tablero son contraladas por la global `config.LARGO_TABLERO`.
    """

    # Generar LARGO_TABLERO listas, cada una con LARGO_TABLERO elementos.
    return [[False for _ in range(config.LARGO_TABLERO)] for _ in range(config.LARGO_TABLERO)]


def plantar_bombas(tablero):
    """
    Coloca minas en posiciones aleatorias del tablero proporcionado.

    La cantidad de minas es controlada por la global `config.NUM_MINAS`.
    """

    for _ in range(config.NUM_MINAS):
        # Escoger una posición aleatoria, y si no hay una bomba ya ahí, poner
        # una bomba.
        # Si ya hay una bomba, escoger otra posición aleatoria hasta que no
        # haya una bomba ya colocada.
        pos_x = random.randint(0, config.LARGO_TABLERO-1)
        pos_y = random.randint(0, config.LARGO_TABLERO-1)
        while tablero[pos_y][pos_x] == -1:
            print('colision')
            pos_x = random.randint(0, config.LARGO_TABLERO-1)
            pos_y = random.randint(0, config.LARGO_TABLERO-1)
        tablero[pos_y][pos_x] = -1


def calcular_adyacentes(tablero):
    """
    Calcula la cantidad de minas adyacentes para cada celda no mina del tablero proporcionado, y
    guarda el resultado del cálculo en el tablero proporcionado.
    """

    for y in range(len(tablero)):
        for x in range(len(tablero[y])):
            if tablero[y][x] == -1:
                continue

            count=0
            max_coord=config.LARGO_TABLERO - 1

            # Las celdas adyacentes están a distancia uno, para arriba o abajo,
            # o derecha o izquierda
            for adj_y in [y-1, y, y+1]:
                for adj_x in [x-1, x, x+1]:
                    # Si la celda adyacente está afuera de la matriz, no cuenta
                    #
                    # No importa que se cuente a sí mismo, porque si es una
                    # bomba no llega hasta acá. Es un acceso más a memoria, y
                    # una comparación más, pero el código es más conciso así,
                    # así que queda así.
                    if 0 <= adj_y <= max_coord and 0 <= adj_x <= max_coord:
                        count += (tablero[adj_y][adj_x] == -1)

            tablero[y][x]=count


def revelar_celdas(fila, columna, tablero_minas, tablero_revelado):
    """
    Revela la celda en posición (columna, fila) del tablero en tablero_revelado.

    Si la celda es una mina, retorna -1, indicando la pérdida del juego.
    Si la celda es vacía, revela todas las celdas adyacentes. Además, recursa
    sobre ellas si son también vacías, revelando las adyacentes de estas.
    Si la celda es un número, simplemente la revela.

    La función retorna -1 en caso de revelar una mina, 0 en caso de que queden
    celdas no vacías sin revelar, y 1 si todas las celdas sin revelar son minas.
    """

    tablero_revelado[fila][columna]=True
    if tablero_minas[fila][columna] == -1:
        return -1
    # Si se revela una celda vacía, todas sus adyacentes se revelan
    if tablero_minas[fila][columna] == 0:
        # Las celdas adyacentes están a distancia uno, para arriba o abajo,
        # o derecha o izquierda
        max_coord = config.LARGO_TABLERO - 1
        for fila_adyacente in [fila-1, fila, fila+1]:
            for columna_adyacente in [columna-1, columna, columna+1]:
                if (0 <= fila_adyacente <= max_coord) and (0 <= columna_adyacente <= max_coord):
                    # Si ya está revelada, es un número o vacía.
                    #
                    # Si es un número, no es necesario revelar los adyacentes
                    # por las reglas del juego.
                    #
                    # Si es vacía, significa que el programa ya la reveló,
                    # o estoy volviendo a la que reveló el usuario, y de
                    # cualquier manera no es necesario recursar a esta
                    # ya que ya fueron reveladas sus adyacentes.
                    if not tablero_revelado[fila_adyacente][columna_adyacente]:
                        revelar_celdas(fila_adyacente, columna_adyacente, tablero_minas, tablero_revelado)

    for y in range(len(tablero_revelado)):
        for x in range(len(tablero_revelado[y])):
            # Si existe alguna celda que no esté revelada y no sea
            # una bomba, significa que faltan celdas por revelar, y todavía
            # no ganó el usuario.
            if not tablero_revelado[y][x] and tablero_minas[y][x] != -1:
                return 0
    # Si se llegó hasta acá, significa que todas las celdas no reveladas
    # son minas, y por lo tanto ganamos.
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
