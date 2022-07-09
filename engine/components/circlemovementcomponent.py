from ..component import Component
import math


class CircleMovementComponent(Component):
    def __init__(self, name, radius, center, speed, starting_angle):
        super().__init__(name)
        self.radius = radius
        self.center = center
        self.angle = math.radians(starting_angle)  # must be a number between 0 and 360
        # Since we don't have a stablished fps the speed is subjected to the
        # Machine calculation power
        self.speed = math.radians(speed)  # Should be a number between -1 and 1

    def render(self, surface):
        pass

    def calculateDeltaVelocity(self, deltaTime):
        deltaSpeed = self.speed * deltaTime
        return deltaSpeed

    def update(self, deltaTime):
        # Calculating the new coordinates
        self.owner.x = self.center[0] + self.radius * math.cos(self.angle)
        self.owner.y = self.center[1] + self.radius * math.sin(self.angle)

        deltaSpeed = self.calculateDeltaVelocity(deltaTime)

        # Adding the speed to the angle
        self.angle += deltaSpeed

    @staticmethod
    def loadFromDict(componentDescriptor):
        radius = componentDescriptor["radius"]
        center = (componentDescriptor["center_x"], componentDescriptor["center_y"])
        speed = componentDescriptor["speed"]
        starting_angle = componentDescriptor["starting_angle"]
        name = componentDescriptor["name"]

        temp = CircleMovementComponent(name, radius, center, speed, starting_angle)
        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        savedict = {
            **savedict,
            **{
                "radius": self.radius,
                "center_x": self.center[0],
                "center_y": self.center[1],
                "speed": math.degrees(self.speed),
                "starting_angle": math.degrees(self.angle),
            },
        }
        return savedict
