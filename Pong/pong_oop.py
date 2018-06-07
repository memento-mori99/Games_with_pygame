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
        # Ball related attributes
        self.x = 0  # x coordinate of the ball
        self.y = 24  # y coordinate of the ball
        self.speed = (4, 4)
        self.ball_image = pygame.image.load(
            "C:\\programming\\python\\programs\\Pygame_projects\\Pong\\ball.png")
        self.bat_image = pygame.image.load(
            "C:\\programming\\python\\programs\\Pygame_projects\\Pong\\bat.png")

        self.bat_rect = self.bat_image.get_rect()
        self.bat_x = 400
        self.bat_y = 50
        self.bat_rect.topleft = (self.bat_x, self.bat_y)

        self.points = 0
        # self.bat_speed = 3

    # These variables are called 'member-fields' and they are stored on a
    # per-object basis. This means that each object gets a separate
    # bit of memory for each field. In our ball class, we have 4 such memory
    # fields.

    def draw_ball(self, gameTime, surface):
        surface.blit(self.ball_image, (self.x, self.y))
        # Attributes and methods belonging to the current object are accessed
        # through self dot(.) followed by the attribute and method.
        # When calling the method,
        # you don't have to pass in self, python will handle that for you.
        # Self is only placed in the parameter list at the method declaration.

    def update_ball(self, gameTime):
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
        # that updates a ball is used by all instances of the ball class.s

    def HasHitBrick(self, bricks):
        return False
    # This method will return a True if the ball has hit a brick. in our stub
    # code, we will always return False.

    def HasHitBat(self, gameTime, SWSURFACE):  # Stud method
        return False

    def draw_bat(self, gameTime, surface):  # Turns out that this function is useless LOL
        surface.blit(self.bat_image, self.bat_rect)

    def update_bat(self, new_bat_x):
        surface.blit(self.bat_image, (new_bat_x, 50))

    def what_to_do_for_collision(self, mouse_x, mouse_y):
        # if (self.bat_x - 8 >= self.x) and (self.x <= self.bat_x + 8) and (self.y <= self.bat_y + 11):
            # self.y =
            # self.speed[1] *= -1
        # if (self.x <= 455) or (self.x >= 400):
        #     print("x cross over")
        #     if (self.y <= 61) or (self.y >= 50):
        #         print("pass")
        if (self.x <= mouse_x + 55) and (self.x >= mouse_x):
            # print("x cross over")
            if (self.y <= 61) and (self.y >= 50):
                # print("Yay")
                sx = self.speed[0]
                sy = self.speed[1]

                # Don't include the below code !!!
                # self.x += sx
                # self.y += sy

                sy *= -1
                self.points += 1
                print(self.points)
                self.speed = (sx, sy)

    def display_points(self, text):
        font_properties = pygame.font.Font("freesansbold.ttf", size=150)
        text_surface, text_rectangle = text_objects(text, font_properties)


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
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                # print(mouse_x)  # [ Useful for ]
                # print(mouse_y)  # [ Debugging ]
                # print(ball.bat_x)

        surface.fill((0, 0, 0))

        ball.update_ball(fps_clock)
        ball.draw_ball(fps_clock, surface)  # Calling the draw() method

        # ball.draw_bat(fps_clock, surface)
        ball.update_bat(mouse_x)

        ball.what_to_do_for_collision(mouse_x, mouse_y)
        # print(ball.bat_rect.topleft)

        pygame.display.update()
        fps_clock.tick(60)
