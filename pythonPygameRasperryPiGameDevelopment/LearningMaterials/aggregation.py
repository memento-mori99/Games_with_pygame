# Aggregation is conceptually like composition

# A container object has a link to other objects and
# it manipulates them in some form, through a method or methods.

# However, the big difference is that the creation and destruction of the objects
# are handled elsewhere.

# With aggregation, the container class MUST NOT delete objects that it uses.


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


class Player(object):
    def __init__(self):
        self.bullets = []

    def getBullets(self):
        return self.bullets

    def removeBullet(self, bullet):
        self.bullets.remove(bullet)


class Collision(object):
    # The collision class is an aggregation, that is it contains
    # reference to the other 2 classes: Player and AlienSwarm

    # It does not control the creation and deletion of those classes.

    # This ties on with our SOLID principle

    # Program to the interface to keep your classes SMALL and NIMBLE

    def __init__(self, player, swarm):
        self.player = player
        self.swarm = swarm

    def checkCollision(self):
        bulletKill = []

        for b in player.getBullets:
            if swarm.isHit(b.x, b.y):
                bulletKill.append(b)
                continue
        for b in bulletKill:
            self.player.score += 10
            self.player.removeBullet(b)


if __name__ == "__main__":
    swarm = AlienSwarm(5)
    swarm.debugPrint()
    player = Player()
    collision = Collision(player, swarm)
    collision.checkCollision()
