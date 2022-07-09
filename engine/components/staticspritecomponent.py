from ..component import Component
import pygame


class StaticSpriteComponent(Component):
    def __init__(self, name, assetFileName):
        super().__init__(name)
        self.assetFileName = assetFileName
        self.image = None

    def load(self):
        self.image = pygame.image.load(self.assetFileName)

    def render(self, surface):
        rect = self.image.get_rect()
        rect.x = self.owner.x
        rect.y = self.owner.y
        surface.blit(self.image, rect)

    @staticmethod
    def loadFromDict(componentDescriptor):
        filename = componentDescriptor["fileName"]
        name = componentDescriptor["name"]
        temp = StaticSpriteComponent(name, filename)
        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        savedict["fileName"] = str(self.assetFileName)
        return savedict
