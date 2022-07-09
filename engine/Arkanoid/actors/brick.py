from ...actor import Actor
from ...component import Component


class Brick(Actor):
    def __init__(self, name, x, y, life):
        super().__init__(name, x, y)
        self.life = life

    def onCollision(self, direction):
        if self.life > 0:
            self.destrucion()

    def destrucion(self):
        self.life -= 1
        if self.life == 0:
            self.owner.removeActor(self)

    @staticmethod
    def loadFromDict(actorDescriptor):
        name = actorDescriptor["name"]
        x = actorDescriptor["x"]
        y = actorDescriptor["y"]
        life = actorDescriptor["life"]

        actor = Brick(name, x, y, life)

        # Loading each component in the actor
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
