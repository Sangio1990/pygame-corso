import pygame
import time
from pygame.locals import *
from .scenefactory import SceneFactory
from .inputsystem import InputSystem
from .scene import Scene


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Engine(metaclass=Singleton):
    def __init__(self):
        pygame.init()
        self.inputSystem = InputSystem()
        self.scene = None
        self.window = None
        self.quit = False
        self.newTime = time.time()
        self.oldTime = self.newTime

    def loadScene(self, fileName):
        # Level setup code
        self.scene = SceneFactory.newLoadSceneFromFile(fileName)

        # setup the window
        self.window = pygame.display.set_mode(
            (self.scene.windowRect.width, self.scene.windowRect.height), 0, 32
        )
        pygame.display.set_caption(self.scene.title)

        self.scene.load()

    def gameLoop(self):
        while not self.quit:
            self.processEvents()
            self.update()
            self.render()

        pygame.quit()

    def processEvents(self):
        # process all the events generated by the system, this also pumps the event queue
        for event in pygame.event.get():
            # event QUIT is generated when the user closes the application window
            if event.type == pygame.locals.QUIT:
                SceneFactory.newSaveSceneToFile(self.scene, "savefiles\prova2.json")
                self.quit = True

        self.inputSystem.process()

    def update(self):
        self.newTime = time.time()
        deltaTime = self.newTime - self.oldTime
        self.scene.update(deltaTime)

        self.oldTime = self.newTime  # prepare for the next frame

    def render(self):
        # clear the screen
        BLACK = (0, 0, 0)
        self.window.fill(BLACK)
        self.scene.render(self.window)

        # update the display with the new content of the window
        pygame.display.update()
