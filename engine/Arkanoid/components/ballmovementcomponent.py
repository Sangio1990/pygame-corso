from ...component import Component


class BallMovementComponent(Component):
    def __init__(self, name, boundingRect):
        super().__init__(name)
        self.boundingRect = boundingRect

    def calculateDeltaVelocity(self, deltaTime):
        deltavx = self.owner.vx * deltaTime
        deltavy = self.owner.vy * deltaTime
        return (deltavx, deltavy)

    def update(self, deltaTime):
        deltavx, deltavy = self.calculateDeltaVelocity(deltaTime)

        self.owner.x += deltavx
        self.owner.y += deltavy

        # bounce on the x axis
        if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
            self.owner.vx = -self.owner.vx

        # bounce on the y axis
        if self.owner.y < 0 or self.owner.y > self.boundingRect.height:
            self.owner.vy = -self.owner.vy

    def onCollision(self, direction):
        if direction == "left" or direction == "right":
            self.owner.vx = -self.owner.vx
        if direction == "top" or direction == "bottom":
            self.owner.vy = -self.owner.vy

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
        temp = BallMovementComponent(name, r)
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
                "vx": self.owner.vx,
                "vy": self.owner.vy,
            },
        }
        return savedict
