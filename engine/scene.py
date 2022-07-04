from pygame import rect


class Scene:
    def __init__(self):
        # there will be actors acting things
        self.actors = []
        self.title = "No Title"
        self.windowRect = rect.Rect(0, 0, 0, 0)

    def load(self):
        for a in self.actors:
            a.load()

    def render(self, surface):
        for a in self.actors:
            a.render(surface)

    # There will be timing involved
    def update(self, deltaTime):
        for a in self.actors:
            a.update(deltaTime)

    def loadFromDict(self, sceneDescriptor):
        windowDescriptor = sceneDescriptor["window"]
        self.windowRect.height = windowDescriptor["height"]
        self.windowRect.width = windowDescriptor["width"]
        self.title = windowDescriptor["title"]

        # Loading each actor in the scene
        from .actor import Actor

        for actorDescriptor in sceneDescriptor["actors"]:
            actor = Actor.loadFromDict(actorDescriptor)
            self.actors.append(actor)

    def saveToDict(self):
        savedict = {
            "window": {
                "width": self.windowRect.width,
                "height": self.windowRect.height,
                "title": self.title,
            },
        }
        actor_list = []
        for actor in self.actors:
            actor_list.append(actor.saveToDict())
        savedict["actors"] = actor_list
        return savedict
