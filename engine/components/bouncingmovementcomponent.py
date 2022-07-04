from ..component import *


class BouncingMovementComponent(Component):
    # Owner could be empty at first
    def __init__(self, boundingRect, actor=None):
        super().__init__(actor)
        self.vx = 0.05
        self.vy = 0.05
        self.boundingRect = boundingRect

    # I could implement some debugging rendering here
    def render(self, surface):
        pass

    def calculateDeltaVelocity(self, deltaTime):
        deltavx = self.vx * deltaTime
        deltavy = self.vy * deltaTime
        return (deltavx, deltavy)

    # There will be timing involved
    def update(self, deltaTime):
        deltavx, deltavy = self.calculateDeltaVelocity(deltaTime)

        self.owner.x += deltavx
        self.owner.y += deltavy

        # bounce on the x axis
        if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
            self.vx = -self.vx

        # bounce on the y axis
        if self.owner.y < 0 or self.owner.y > self.boundingRect.height:
            self.vy = -self.vy

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
        temp = BouncingMovementComponent(r)
        temp.name = componentDescriptor["name"]
        temp.vx = componentDescriptor["vx"]
        temp.vy = componentDescriptor["vy"]
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
