from ...component import Component
import pygame


class BrickRenderComponent(Component):
    def __init__(self, name):
        super().__init__(name)
        self.lifecolor = {
            -1: "engine/Arkanoid/assets/Immortal_brick.png",
            1: (0, 255, 0),
            2: (255, 255, 0),
            3: (255, 0, 0),
        }
        self.image = None
        self.color = (255, 255, 255)

    def load(self):
        self.update(0)

    def update(self, deltaTime):
        if self.owner.life == -1:
            self.image = pygame.image.load(self.lifecolor[-1])
        else:
            self.color = self.lifecolor[self.owner.life]

    def render(self, surface):
        if self.image is not None:
            rect = self.image.get_rect()
            rect.x = self.owner.x
            rect.y = self.owner.y
            surface.blit(self.image, rect)
        else:
            pygame.draw.rect(
                surface, self.color, pygame.Rect(self.owner.x, self.owner.y, 30, 14)
            )

    @staticmethod
    def loadFromDict(componentDescriptor):
        name = componentDescriptor["name"]
        temp = BrickRenderComponent(name)
        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        return savedict
