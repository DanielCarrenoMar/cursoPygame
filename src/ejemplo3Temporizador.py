import pygame as pg
import pygame_menu as pgm

# 3 TEMPORIZADOR

pg.init()

screenW = 600
screenH = 400

surface = pg.display.set_mode((screenW, screenH))
pg.display.set_caption("Titulo")
image = pg.image.load('resources\\kirby.png')
image = pg.transform.scale(image, (image.get_width()*4, image.get_height()*4))

actualPage = 0

# Iniciamos el temporizador
start_ticks = pg.time.get_ticks() # Obtenemos la cantidad de tick actual
timer_duration = 3000 # Duración del temporizador en milisegundos (3 segundos)

def intro():
    global actualPage
    X = (pg.display.get_window_size()[0] - image.get_width())/2
    Y = (pg.display.get_window_size()[1] - image.get_height())/2
    surface.blit(image, (X, Y), image.get_rect())

    # Calcular el tiempo restante
    time = pg.time.get_ticks() - start_ticks  # Ticks que han pasado desde que se inicio el temporizador
    timeLeft = max(0, timer_duration - time)  # ticks restantes

    if (timeLeft == 0): # Si el temporizador ha terminado
        actualPage = 1

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

    if (actualPage == 0): intro()
    elif (actualPage == 1): menu()
    elif (actualPage == 2): formas()

    pg.display.flip()