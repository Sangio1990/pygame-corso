from ..component import Component
import pygame


class MarioMovementComponent(Component):
    def __init__(self, name, boundingRect):
        super().__init__(name)
        from ..engine import Engine

        engine = Engine()
        self.vx = 0
        self.vy = 0
        self.boundingRect = boundingRect
        self.gravity = 0.5
        self.floor = False

        engine.inputSystem.bindToKeyboard(pygame.locals.K_SPACE, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.keyPressed)

    def update(self, deltaTime):
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime

        # inertia
        if self.vx > 0:
            self.vx = self.vx - 200 * deltaTime
        if self.vx < 0:
            self.vx = self.vx + 200 * deltaTime
        if self.vy > 0:
            self.vy = self.vy - 200 * deltaTime
        if self.vy < 0:
            self.vy = self.vy + 200 * deltaTime

        # gravity
        self.vy += self.gravity

        if self.owner.x <= self.boundingRect.x:
            self.vx = 0
            self.owner.x = self.boundingRect.x
        if self.owner.x >= self.boundingRect.width:
            self.vx = 0
            self.owner.x = self.boundingRect.width
        if self.owner.y >= self.boundingRect.height:
            self.vy = 0
            self.owner.y = self.boundingRect.height
            self.floor = True

    def keyPressed(self, key):
        if key == pygame.locals.K_SPACE:
            if self.floor:
                self.vy = -900
                self.floor = False
        # Adding an easy acceleration system
        if key == pygame.locals.K_LEFT:
            self.vx -= 1
            if self.vx < -300:
                self.vx = -300
        if key == pygame.locals.K_RIGHT:
            self.vx += 1
            if self.vx > 300:
                self.vx = 300

    @staticmethod
    def loadFromDict(componentDescriptor):
        from pygame import rect

        rectDescriptor = componentDescriptor["boundingRect"]
        r = rect.Rect(
            rectDescriptor["x"],
            rectDescriptor["y"],
            rectDescriptor["width"],
            rectDescriptor["height"],
        )
        name = componentDescriptor["name"]
        temp = MarioMovementComponent(name, r)

        # If the actor was moving we keep the inertia while loading
        try:
            temp.vx = componentDescriptor["vx"]
            temp.vy = componentDescriptor["vy"]
        except KeyError:
            # If not we set it as standing on the given point
            temp.vx = 0
            temp.vy = 0
        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        savedict = {
            **savedict,
            **{
                "boundingRect": {
                    "x": self.boundingRect.left,
                    "y": self.boundingRect.top,
                    "width": self.boundingRect.width,
                    "height": self.boundingRect.height,
                },
                "vx": self.vx,
                "vy": self.vy,
            },
        }
        return savedict
