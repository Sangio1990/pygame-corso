# Here the game is launched
import pygame, pygame.locals, sys
from engine.scene import *
from engine.component import *
from engine.actor import *
from engine.fixwindow import *
from game_logic.faccina import *
from engine.bouncing_object import BouncingObject
from engine.filesave import Save

pygame.init()
pygame.display.set_caption("Prova dell'engine")

Quit = False

scene = FixWindow("Faccina screensaver!")
actor = Faccina()
scene.actors.append(actor)

scene.load()
component = BouncingObject(actor.image, scene.window.get_rect())
scene.actors[0].components.append(component)
Save.level_save("levels", "test_level", [scene])
# exit()


def process_events():
    global Quit
    # process all the events generated by the system
    for event in pygame.event.get():
        # event QUIT is generated when the user closes the application window
        if event.type == pygame.locals.QUIT:
            Quit = True


def update_game_logic():
    global scene

    scene.update()

    return


def render():
    global scene

    # clear the screen
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    scene.window.fill(BLACK)

    scene.render(scene.window)

    # update the display with the new content of the window
    pygame.display.update()


# game loop
while not Quit:
    process_events()

    update_game_logic()

    render()

pygame.quit()
sys.exit()