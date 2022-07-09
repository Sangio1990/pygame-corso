from ..component import Component
import time
import random


class ZigZagMovementComponent(Component):
    def __init__(self, name, boundingRect):
        super().__init__(name)
        self.vx = 0.05
        self.vy = 0.05
        self.boundingRect = boundingRect
        self.last_change = time.time()

    def render(self, surface):
        pass

    def random_direction(self):
        # If 1 second is passed since last change the velocity value will randomly change
        if time.time() > self.last_change + 1:
            self.vx = random.randrange(-300, 300)
            self.vy = random.randrange(-300, 300)
            self.last_change = time.time()

    def calculateDeltaVelocity(self, deltaTime):
        deltavx = self.vx * deltaTime
        deltavy = self.vy * deltaTime
        return deltavx, deltavy

    def update(self, deltaTime):
        self.random_direction()

        # bounce on the x axis
        if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
            self.vx = -self.vx

        # bounce on the y axis
        if self.owner.y < 0 or self.owner.y > self.boundingRect.height:
            self.vy = -self.vy

        deltavx, deltavy = self.calculateDeltaVelocity(deltaTime)

        self.owner.x += deltavx
        self.owner.y += deltavy

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
        temp = ZigZagMovementComponent(name, r)
        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        savedict["boundingRect"] = {
            "x": self.owner.x,
            "y": self.owner.y,
            "width": self.boundingRect.width,
            "height": self.boundingRect.height,
        }
        return savedict
