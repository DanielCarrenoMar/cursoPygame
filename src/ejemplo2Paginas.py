import pygame as pg
import pygame_menu as pgm

# 2 PAGINAS

pg.init()

screenW = 600
screenH = 400

surface = pg.display.set_mode((screenW, screenH))
image = pg.image.load('resources\\kirby.png')
image = pg.transform.scale(image, (image.get_width()*4, image.get_height()*4))

actualPage = 0 # Definimos la variable pagina actual

# Funciones con el codigo de dibujado de cada pagina
def intro():
    global actualPage
    X = (pg.display.get_window_size()[0] - image.get_width())/2
    Y = (pg.display.get_window_size()[1] - image.get_height())/2
    surface.blit(image, (X, Y), image.get_rect())

def menu():
    global actualPage

def formas():
    global actualPage

running = True
while (running):
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            running = False

    surface.fill((0, 0, 0))

    # Dibujamos la pagina actual
    if actualPage == 0: intro()
    elif actualPage == 1: menu()
    elif actualPage == 2: formas()

    pg.display.flip()