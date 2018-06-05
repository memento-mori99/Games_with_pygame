import pygame
import os
import sys
from pygame.locals import *

# OOP is a programming paradigm where items are abstracted down to their basic
# elements.

# What you can do with them : aka Functions / Methods.
# Attributes that describe them : Variables.

# Copies of these classes in memory are called instances.
# In some languages classes are called User-defined types.
# A "class" is an abstract thing.
# These 'class' defines method (actions) that can be taken on the
# data (attributes) of the 'instance'.
# An 'instance' of a class is called an object.
# An 'instance' of a user defined class is much like '5' is an 'instance'
# of an "integer" or "Hello World" is an instance of a "string".
# Both "integer" and 'string' are abstractions and "5" and "Hello World"
# are instances of each respectively.

# Let's take an example of a ball. A ball can be described by it's
# shape,size and colour. These are its attributes.
# Some methods we can do are update its position, check for collision
# and draw it onscreen. These actions are called Methods.

# SUMMARY : ATTRIBUTES DESCRIBE THE OBJECT METHODS AND ARE WHAT
# WE CAN MAKE THE OBJECT DO.


class Ball():
    # A class is defined using the class keyword.
    def __init__(self):
        self.x = 0
        self.y = 24
        self.speed = (4, 4)
        self.image = pygame.image.load(
            "C:\\programming\\python\\programs\\Pygame_projects\\pythonPygameRasperryPiGameDevelopment\\LearningMaterials\\balls.png")
    # These variables are called 'member-fields' and they are stored on a
    # per-object basis. This means that each object gets a separate
    # bit of memory for each field. In our ball class, we have 4 such memory
    # fields.

    def update(self, gameTime):
        sx = self.speed[0]
        sy = self.speed[1]
        self.x += sx
        self.y += sy

        if self.y <= 0:
            self.y = 0
            sy *= -1  # The ball shoots itself in the reverse direction.

        if self.y >= 600 - 8:
            self.y = 600 - 8
            sy *= -1

        if self.x <= 0:
            self.x = 0
            sx *= -1

        if self.x >= 800 - 8:
            self.x = 800 - 8
            sx *= -1

        self.speed = (sx, sy)

        # Earlier i mentioned that the member fields are per object.
        # The "self" keyword is used because Python passes in a reference
        # to the object being used for that operation.
        # Whereas the data is different for each object, the code is not.
        # It is shared between all instances of the class.
        # This means that the same piece of code
        # that updates a ball is used by all instances of the ball class.

    def HasHitBrick(self, bricks):
        return False
    # This method will return a True if the ball has hit a brick. in our stub
    # code, we will always return False.

    def HasHitBat(self, gameTime, SWSURFACE):
        return False

    def draw(self, gameTime, surface):
        surface.blit(self.image, (self.x, self.y))
        # Attributes and methods belonging to the current object are accessed
        # through self dot(.) followed by the attribute and method.
        # When calling the method,
        # you don't have to pass in self, python will handle that for you.
        # Self is only placed in the parameter list at the method declaration.


if __name__ == '__main__':
    pygame.init()
    fps_clock = pygame.time.Clock()
    surface = pygame.display.set_mode((800, 600))

    ball = Ball()  # An object has been created
    # The parantheses allows parameters to be passed to a special method
    # called a constructor.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.quit()
        surface.fill((0, 0, 0))
        ball.draw(fps_clock, surface)  # Calling the draw() method
        ball.update(fps_clock)
        pygame.display.update()
        fps_clock.tick(60)
