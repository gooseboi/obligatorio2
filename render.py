import pygame
import config

# No se puede modificar este archivo

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((config.WINDOW_SIZE, config.WINDOW_SIZE))
# Dibujar la imagen de fondo
if config.IMAGEN_FONDO != "":
    pantalla.blit(pygame.image.load(config.IMAGEN_FONDO), (0, 0))
# Título de la ventana
pygame.display.set_caption("Buscaminas")

# Colores
BLANCO = (255, 255, 255)
GRIS_OSCURO = (100, 100, 100)
GRIS_CLARO = (180, 180, 180)
ROJO = (255, 0, 0)


# Funciones
# Forma el tablero y lo dibuja en la ventana
# Recibe como argumento "tablero", que es la matriz de números enteros, y "revelado", que es la matriz de booleanos.
def dibujar_tablero(tablero, revelado):
    for fila in range(config.LARGO_TABLERO):
        for columna in range(config.LARGO_TABLERO):
            celda = pygame.Rect((columna * config.CELL_SIZE) + 3, (fila * config.CELL_SIZE) + 3, config.CELL_SIZE - 6, config.CELL_SIZE - 6)
            if revelado[fila][columna]:
                pygame.draw.rect(pantalla, GRIS_CLARO, celda, border_radius=4)
                if tablero[fila][columna] == -1:
                    pygame.draw.circle(pantalla, ROJO, celda.center, config.CELL_SIZE // 6)
                elif tablero[fila][columna] > 0:
                    fuente = pygame.font.Font(None, config.CELL_SIZE)
                    texto = fuente.render(str(tablero[fila][columna]), True, GRIS_OSCURO)
                    pantalla.blit(texto, texto.get_rect(center=celda.center))
            else:
                pygame.draw.rect(pantalla, GRIS_OSCURO, celda, border_radius=4)
    pygame.display.flip()


# Muestra un mensaje en la pantalla y termina la partida
def salir(mensaje):
    if mensaje == "":  # Salió porque el usuario cerró antes de terminar la partida
        pygame.time.wait(3000)  # Esperar 3 segundos antes de cerrar
        pygame.quit()
        exit()

    # Cambiamos el header
    pygame.display.set_caption(f"Buscaminas - {mensaje}")

    # Mensaje principal
    fuente = pygame.font.Font(None, 68)
    texto = fuente.render(mensaje, True, BLANCO)
    rectangulo = texto.get_rect(center=(config.WINDOW_SIZE // 2, config.WINDOW_SIZE // 2))
    pantalla.blit(texto, rectangulo)
    pygame.display.flip()
    pygame.time.wait(3000)  # Esperar 3 segundos antes de cerrar
