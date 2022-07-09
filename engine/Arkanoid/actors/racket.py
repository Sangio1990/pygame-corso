from ...actor import Actor
from ...component import Component


class Racket(Actor):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def onCollision(self, otherCollider):
        pass

    @staticmethod
    def loadFromDict(actorDescriptor):
        name = actorDescriptor["name"]
        x = actorDescriptor["x"]
        y = actorDescriptor["y"]

        actor = Racket(name, x, y)

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
