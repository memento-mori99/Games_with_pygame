import os


# Composition is the containment of one or more objects within another
# With composition, the contained objects' creation and destruction are
# controlled by the container object.

# The container object generally acts as a controller for the contained objects

# For example

class Alien(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass


class AlienSwarm(object):
    def __init__(self, numAliens):
        self.swarm = []

        y = 0
        x = 24

        for num in range(numAliens):
            alien = Alien(x, y)
            self.swarm.append(alien)

            x += 24
            if x > 640:
                x = 0
                y += 24
            # Each alien is separated by 24 pixels across and 24 pixels down.

    def debugPrint(self):
        for a in self.swarm:
            print("x = %d, y = %d " % (a.x, a.y))

    def isHit(self, x, y):
        alienToRemove = None
        for a in self.swarm:
            if x >= a.x and x <= a.x + 24 and y > a.y and a <= a.y + 24:
                alienToRemove = a
                break
        if alienToRemove != None:
            self.swarm.remove(alienToRemove)
            return True
        return False


swarm = AlienSwarm(100)
swarm.debugPrint()
