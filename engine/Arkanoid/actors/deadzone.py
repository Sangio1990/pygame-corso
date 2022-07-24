from ...actor import Actor
from ...component import Component


class DeadZone(Actor):
    def onCollision(self, direction):
        print("GAME OVER!")

    @staticmethod
    def loadFromDict(actorDescriptor):
        name = actorDescriptor["name"]
        x = actorDescriptor["x"]
        y = actorDescriptor["y"]

        actor = DeadZone(name, x, y)

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
