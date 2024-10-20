import pygame as pg
import pygame_menu as pgm

# 1 IMAGEN

pg.init() # Iniciamos Modulos de Pygame

# Definimos el tamaño de la ventana
screenW = 600
screenH = 400

surface = pg.display.set_mode((screenW, screenH)) # Creamos la ventana

image = pg.image.load('resources\\kirby.png') # Importamos imagen
image = pg.transform.scale(image, (image.get_width()*4, image.get_height()*4)) # Cambiamos tamaño de la imagen

# Bucle principal
running = True
while (running):
    events = pg.event.get() # Obtenemos una lista de las acciones del usuario

    for event in events:
        if event.type == pg.QUIT: # Verficamos si pulsa el boton de cerrar
            running = False

    surface.fill((0, 0, 0)) # Mandamos a rellenar la ventana de negro

    X = (pg.display.get_window_size()[0] - image.get_width())/2
    Y = (pg.display.get_window_size()[1] - image.get_height())/2
    surface.blit(image, (X, Y), image.get_rect()) # Mandamos a dibujar la imagen en coordenadas X, Y

    pg.display.flip() # Ejecutamos las intrucciones anteriores de dibujado