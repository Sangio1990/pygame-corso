import image as image

from ..actor import Actor
import pygame


class Background(Actor):
    def __init__(self, name, x, y, imagepath):
        super().__init__(name, x, y)
        self.image = pygame.image.load(imagepath)

    def render(self, surface):
        from ..engine import Engine

        e = Engine()
        screen_w, screen_h = e.window.get_size()
        image_w, image_h = self.image.get_size()
        for x in range(0, screen_w, image_w):
            for y in range(0, screen_h, image_h):
                e.window.blit(self.image, (x, y))

    @staticmethod
    def loadFromDict(actorDescriptor):
        name = actorDescriptor["name"]
        x = actorDescriptor["x"]
        y = actorDescriptor["y"]
        imagepath = actorDescriptor["imagepath"]
        actor = Background(name, x, y, imagepath)

        # Loading each component in the actor
        from ..component import Component

        for componentDescriptor in actorDescriptor["components"]:
            component = Component.loadFromDict(componentDescriptor)
            actor.addComponent(component)

        return actor

    def saveToDict(self):
        savedict = super().saveToDict()
        components_dict = []
        for component in self.components:
            components_dict.append(component.saveToDict())
        savedict["components"] = components_dict
        return savedict
