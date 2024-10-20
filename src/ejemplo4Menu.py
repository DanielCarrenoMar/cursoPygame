import pygame as pg
import pygame_menu as pgm

# 4 MENU CON PYGAME_MENU

pg.init()

screenW = 600
screenH = 400

surface = pg.display.set_mode((screenW, screenH))
image = pg.image.load('resources\\kirby.png')
image = pg.transform.scale(image, (image.get_width()*4, image.get_height()*4))

actualPage = 0

start_ticks = pg.time.get_ticks()
timer_duration = 10

def play():
    global actualPage
    actualPage = 2

def setName(value):
    global nameInput
    print("Nombre " + value)

def setDifficulty(value, difficulty):
    print(value, difficulty)
    pass

#Creamos la variable menu y le asignamos un nombre, el tamaño de la pantalla y el tema
menu = pgm.Menu('Principal', screenW, screenH,theme=pgm.themes.THEME_BLUE)

#Añadimos los botones que tendra el menu
menu.add.text_input('Name :', default='John Doe', onchange=setName) # La funcion setName se ejecutara cada vez que se escriba
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=setDifficulty) # La funcion setName se ejecutara cada vez que se cambie el campo
menu.add.button('Play', play) # La funcion play se ejecutara al pulsar el boton
menu.add.button('Quit', pgm.events.EXIT) # Salir del juego

def intro():
    global actualPage
    X = (pg.display.get_window_size()[0] - image.get_width())/2
    Y = (pg.display.get_window_size()[1] - image.get_height())/2
    surface.blit(image, (X, Y), image.get_rect())

    time = pg.time.get_ticks() - start_ticks
    timeLeft = max(0, timer_duration - time)

    if (timeLeft == 0):
        actualPage = 1

def mainMenu():
    #Actualizamos el menu y lo dibujamos
    menu.update(events)
    menu.draw(surface)

def formas():
    global actualPage

running = True
while (running):
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            running = False

    surface.fill((0, 0, 0))

    if actualPage == 0: intro()
    elif actualPage == 1: mainMenu()
    elif actualPage == 2: formas()

    pg.display.flip()