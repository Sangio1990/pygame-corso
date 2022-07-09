class CollisionSystem:
    def __init__(self):
        self.colliders = []

    def process(self):
        # detect collision

        index = 0
        for a in self.colliders:
            index += 1
            for x in range(index, len(self.colliders)):
                try:  # Just to be safe, but shouldn't be needed
                    b = self.colliders[x]
                    if a is not b:  # Just to be safe, but shouldn't be needed.
                        if a.AABB.colliderect(b.AABB):
                            direction = self.calculateCollisionDirections(a, b)
                            a.onCollision(direction)
                            b.onCollision(direction)
                            print(
                                str(a.owner.name)
                                + " collided with "
                                + str(b.owner.name)
                                + " on the "
                                + direction
                            )
                except IndexError:
                    pass

    def calculateCollisionDirections(self, a, b):
        a.right = a.AABB.x + a.AABB.width
        b.right = b.AABB.x + b.AABB.width
        a.bottom = a.AABB.y + a.AABB.height
        b.bottom = b.AABB.y + b.AABB.height

        depth = {}

        # Calculating the depth of each collision
        if a.AABB.x < b.AABB.x < a.right < b.right:
            depth["left"] = a.right - b.AABB.x

        if b.AABB.x < a.AABB.x < b.right < a.right:
            depth["right"] = b.right - a.AABB.x

        if a.AABB.y < b.AABB.y < a.bottom < b.bottom:
            depth["top"] = a.bottom - b.AABB.y

        if b.AABB.y < a.AABB.y < b.bottom < a.bottom:
            depth["bottom"] = b.bottom - a.AABB.y

        # Returning the lowest value to the system
        if len(depth) > 0:
            return min(depth, key=depth.get)

    def registerCollider(self, collider):
        self.colliders.append(collider)

    def deregisterCollider(self, collider):
        self.colliders.remove(collider)
