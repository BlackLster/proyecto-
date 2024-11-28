import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la ventana
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Juego de la Serpiente')

# Configuración de la serpiente
tamaño_cuadro = 10
velocidad = 15

# Fuente para el puntaje
fuente = pygame.font.SysFont('Arial', 25)

def mostrar_puntaje(puntaje):
    texto = fuente.render("Puntaje: " + str(puntaje), True, negro)
    ventana.blit(texto, [0, 0])

def dibujar_serpiente(tamaño_cuadro, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(ventana, verde, [x[0], x[1], tamaño_cuadro, tamaño_cuadro])

def juego():
    game_over = False
    game_close = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamaño_cuadro) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_cuadro) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            ventana.fill(blanco)
            mensaje = fuente.render("Perdiste! Presiona C para jugar de nuevo o Q para salir", True, rojo)
            ventana.blit(mensaje, [ancho / 6, alto / 3])
            mostrar_puntaje(longitud_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_cuadro
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_cuadro
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_cuadro
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_cuadro
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        ventana.fill(blanco)
        pygame.draw.rect(ventana, azul, [comida_x, comida_y, tamaño_cuadro, tamaño_cuadro])
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)
        if len(lista_serpiente) > longitud_serpiente:
            del lista_serpiente[0]

        for x in lista_serpiente[:-1]:
            if x == cabeza_serpiente:
                game_close = True

        dibujar_serpiente(tamaño_cuadro, lista_serpiente)
        mostrar_puntaje(longitud_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_cuadro) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_cuadro) / 10.0) * 10.0
            longitud_serpiente += 1

        pygame.time.Clock().tick(velocidad)

    pygame.quit()
    quit()

juego()
