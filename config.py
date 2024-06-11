# Configuración del juego.
# IMPORTANTE: Las constantes no se copian en main.
# Para poder usar estas constantes en main, deben escribirlas como config.<nombre de la variable>
# Por ejemplo, si quieren usar num_minas en main escriben config.num_minas

# Son libres de cambiar los valores como quieran, pero no pueden agregar nuevas constantes en este archivo.
LARGO_TABLERO = 10  # Largo y ancho de la matriz que vamos a usar de tablero
NUM_MINAS = 10  # Cantidad de minas que tiene el tablero
IMAGEN_FONDO = ""  # Si quieren cambiar el fondo, pueden descargar una imagen y poner la ruta acá.

WINDOW_SIZE = 800  # Tamaño de la ventana, en pixeles
CELL_SIZE = WINDOW_SIZE // LARGO_TABLERO  # Tamaño de cada celda individual del tablero.
