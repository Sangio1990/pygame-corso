from ...components.collidercomponent import ColliderComponent


class DeadZoneColliderComponent(ColliderComponent):
    def __init__(self, name, AABB):
        super().__init__(name)
        self.AABB = AABB

    def update(self, deltaTime):
        self.AABB.x = self.owner.x
        self.AABB.y = self.owner.y + 20  # 20px are the transparent space above the beam

    def load(self):
        from ...engine import Engine

        e = Engine()
        e.collisionSystem.registerCollider(self)

    @staticmethod
    def loadFromDict(componentDescriptor):
        from pygame import rect

        rectDescriptor = componentDescriptor["boundingRect"]
        r = rect.Rect(
            rectDescriptor["x"],
            rectDescriptor["y"],
            rectDescriptor["width"],
            rectDescriptor["height"],
        )
        name = componentDescriptor["name"]
        temp = DeadZoneColliderComponent(name, r)

        return temp

    def saveToDict(self):
        savedict = super().saveToDict()
        savedict = {
            **savedict,
            **{
                "boundingRect": {
                    "x": self.AABB.left,
                    "y": self.AABB.top,
                    "width": self.AABB.width,
                    "height": self.AABB.height,
                },
            },
        }
        return savedict
