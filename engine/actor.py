class Actor:
    def __init__(self, name, x, y):
        self.components = []
        self.x = x
        self.y = y
        self.name = name

    def load(self):
        for a in self.components:
            a.load()

    def render(self, surface):
        for a in self.components:
            a.render(surface)

    # There will be timing involved
    def update(self, deltaTime):
        for a in self.components:
            a.update(deltaTime)

    def addComponent(self, component):
        self.components.append(component)
        component.setOwner(self)

    def onCollision(self, otherCollider):
        pass

    def setOwner(self, scene):
        self.owner = scene

    @staticmethod
    def loadFromDict(actorDescriptor):
        import importlib

        module = importlib.import_module(actorDescriptor["module"])
        base_class = getattr(module, actorDescriptor["type"])
        actor = base_class.loadFromDict(actorDescriptor)
        return actor

    def saveToDict(self):
        savedict = {
            "name": str(self.name),
            "type": self.__class__.__name__,
            "module": self.__module__,
            "x": self.x,
            "y": self.y,
        }
        return savedict
