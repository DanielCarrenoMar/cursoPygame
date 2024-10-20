import pygame as pg
import pygame_menu as pgm

# 4 DIBUJAR Y MODIFICAR FORMAS EN PANTALLA

pg.init()

screenW = 600
screenH = 400

surface = pg.display.set_mode((screenW, screenH))
pg.display.set_caption("Titulo")
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

menu = pgm.Menu('Principal', screenW, screenH,theme=pgm.themes.THEME_BLUE)
menu.add.text_input('Name :', default='John Doe', onchange=setName)
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=setDifficulty)
menu.add.button('Play', play)
menu.add.button('Quit', pgm.events.EXIT)

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
    menu.update(events)
    menu.draw(surface)

color  = (255, 0, 0) # Creamos una variable para el color fuera del bucle
def formas():
    global actualPage, color # Ponemos color como variable global para poder usarla en la funcion

    texto = pg.font.Font(None, 36).render("Pulsa A,S,D para cambiar de color", True, (255, 255, 255)) #Asignamos el texto a la varaible como si fuera una imagen
    surface.blit(texto, (100, 300)) # Dibujamos en pantalla la imagen del texto

    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a: #Si se presiona la tecla A, cambia el color
                color = (0, 200, 20)
            elif event.key == pg.K_s:
                color = (200, 20, 0)
            elif event.key == pg.K_d:
                color = (20, 0, 200)

    pg.draw.rect(surface, color, (200, 50, 200, 200))
    #pg.draw.circle(surface, color, (300, 150), 100)
    #pg.draw.line(surface, color, (200, 50), (300, 200), 4)

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