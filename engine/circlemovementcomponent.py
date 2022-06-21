from typing import Tuple
from .component import Component
import math


class CircleMovementComponent(Component):
    def __init__(self, radius, center: Tuple, speed, starting_angle, actor=None):
        super().__init__(actor)
        self.radius = radius
        self.center = center
        self.angle = math.radians(starting_angle)  # must be a number between 0 and 360
        # Since we don't have a stablished fps the speed is subjected to the
        # Machine calculation power
        self.speed = math.radians(speed)  # Should be a number between -1 and 1

    def render(self, surface):
        pass

    def update(self):
        # Calculating the new coordinates
        self.owner.x = self.center[0] + self.radius * math.cos(self.angle)
        self.owner.y = self.center[1] + self.radius * math.sin(self.angle)

        # Adding the speed to the angle
        self.angle += self.speed

    @staticmethod
    def loadFromDict(componentDescriptor):
        radius = componentDescriptor["radius"]
        center = (componentDescriptor["center_x"], componentDescriptor["center_y"])
        speed = componentDescriptor["speed"]
        starting_angle = componentDescriptor["starting_angle"]
        return CircleMovementComponent(radius, center, speed, starting_angle)

    def saveToDict(self):
        savedict = {
            "name": "circle",
            "type": "CircleMovementComponent",
            "module": "engine.circlemovementcomponent",
            "radius": self.radius,
            "center_x": self.center[0],
            "center_y": self.center[1],
            "speed": math.degrees(self.speed),
            "starting_angle": math.degrees(self.angle),
        }
        return savedict
