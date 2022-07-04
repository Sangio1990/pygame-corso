from ..component import Component
import math


# This component get a list of coordinates and move the actor along the coordinates
class PathMovementComponent(Component):
    def __init__(self, path, actor=None):
        super().__init__(actor)
        self.vx = 0
        self.vy = 0
        self.index = 0
        self.path = path

    def calculateVelocity(self, destinationDict):
        destiantionx = destinationDict["x"]
        destiantiony = destinationDict["y"]
        time = destinationDict["time"]
        try:
            self.vx = (destiantionx - self.owner.x) / time
            self.vy = (destiantiony - self.owner.y) / time
        except ZeroDivisionError:
            # If the time is zero the target get teleported to the destination
            self.vx = 0
            self.vy = 0
            self.owner.x = destiantionx
            self.owner.y = destiantiony

    def calculateDeltaVelocity(self, deltaTime):
        deltavx = self.vx * deltaTime
        deltavy = self.vy * deltaTime
        return deltavx, deltavy

    def update(self, deltaTime):
        destination = self.path[self.index]
        # Reading the next position to navigate
        deltax = self.owner.x - destination["x"]
        deltay = self.owner.y - destination["y"]

        if math.sqrt(deltax**2 + deltay**2) < 1:
            self.index += 1
            if self.index == len(self.path):
                self.index = 0
            self.calculateVelocity(self.path[self.index])

        deltavx, deltavy = self.calculateDeltaVelocity(deltaTime)

        self.owner.x += deltavx
        self.owner.y += deltavy

    @staticmethod
    def loadFromDict(componentDescriptor):
        path = componentDescriptor["path"]
        temp = PathMovementComponent(path)
        temp.name = componentDescriptor["name"]
        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        savedict["path"] = self.path
        return savedict
