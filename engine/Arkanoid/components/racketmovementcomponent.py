from ...component import Component
import pygame


class RacketMovementComponent(Component):
    def __init__(self, name):
        super().__init__(name)
        from ...engine import Engine

        engine = Engine()
        self.vx = 0
        self.vy = 0

        engine.inputSystem.bindToKeyboard(pygame.locals.K_SPACE, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.keyPressed)

    def update(self, deltaTime):
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime

        if self.vx != 0:
            self.vx = 0
        if self.vy != 0:
            self.vy = 0

    def keyPressed(self, key):
        if key == pygame.locals.K_LEFT:
            self.vx = -400
        if key == pygame.locals.K_RIGHT:
            self.vx = 400

    @staticmethod
    def loadFromDict(componentDescriptor):
        name = componentDescriptor["name"]
        temp = RacketMovementComponent(name)
        return temp

    def saveToDict(self):

        return super().saveToDict()
