class Component:

    # Owner could be empty at first
    def __init__(self, name, actor=None):
        self.owner = actor
        self.name = name

    def load(self):
        pass

    def render(self, surface):
        pass

    # There will be timing involved
    def update(self, deltaTime):
        pass

    def setOwner(self, actor):
        self.owner = actor

    @staticmethod
    def loadFromDict(componentDescriptor):
        import importlib

        module = importlib.import_module(componentDescriptor["module"])
        base_class = getattr(module, componentDescriptor["type"])
        component = base_class.loadFromDict(componentDescriptor)
        return component

    def calculateDeltaVelocity(self, deltaTime):
        pass

    def saveToDict(self):
        savedict = {
            "name": self.name,
            "type": self.__class__.__name__,
            "module": self.__module__,
        }
        return savedict
