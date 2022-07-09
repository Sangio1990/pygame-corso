from ...actor import Actor
from ...component import Component


class Ball(Actor):
    def __init__(self, name, x, y, vx, vy):
        super().__init__(name, x, y)
        self.vx = vx
        self.vy = vy

    def onCollision(self, direction):
        for component in self.components:
            try:
                component.onCollision(direction)
            except:
                pass

    @staticmethod
    def loadFromDict(actorDescriptor):
        name = actorDescriptor["name"]
        x = actorDescriptor["x"]
        y = actorDescriptor["y"]
        vx = actorDescriptor["vx"]
        vy = actorDescriptor["vy"]
        actor = Ball(name, x, y, vx, vy)

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
