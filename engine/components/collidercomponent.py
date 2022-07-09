from ..component import Component
import pygame


class ColliderComponent(Component):
    def __init__(self, name, AABB):
        super().__init__(name)
        self.AABB = AABB

    def update(self, deltaTime):
        self.AABB.x = self.owner.x
        self.AABB.y = self.owner.y

    def load(self):
        from ..engine import Engine

        e = Engine()
        e.collisionSystem.registerCollider(self)

    def onCollision(self, othercollider):
        self.owner.onCollision(othercollider)

    def render(self, surface):
        color = (255, 0, 0)
        pygame.draw.rect(surface, color, self.AABB, 2)

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
        temp = ColliderComponent(name, r)

        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        savedict = {
            **savedict,
            **{
                "boundingRect": {
                    "x": self.AABB.left,
                    "y": self.AABB.top,
                    "width": self.AABB.width,
                    "height": self.AABB.height,
                },
            },
        }
        return savedict
