import sys
import os
import pygame
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600

# Colour definitions Red Green Blue
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BROWN = (83, 91, 36)

game_Display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("A bit racey")

# A clock is basically going to time things for us
# We use it for frames for second.
clock = pygame.time.Clock()

# we need to tell where to display the car_image
# the car size is 343 * 383
car_image = pygame.image.load("redfighter.png")
car_image = pygame.transform.scale(car_image, (120, 170))


def car(x, y):
    # Intilise where to place the car_image
    game_Display.blit(car_image, (x, y))
    # (x,y) is a tuple
    # blit is basically like drawing to the background


# x = (display_width - (400 - 100))
# y = (display_height - (300 + 100))
x = (display_width * 0.45)
y = (display_height * 0.70)

x_change = 0

crashed = False
while not crashed:

    # This is your event handling loop and you might have a logic loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 5
            elif event.key == pygame.K_RIGHT:
                x_change += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change += 5
            elif event.key == pygame.K_RIGHT:
                x_change += -5
        print(event)

    x += x_change

    game_Display.fill(BROWN)
    car(x, y)

    pygame.display.update()
    clock.tick(60)
    # 60 Frames in second, 30 Frames in second

pygame.quit()
quit()

##############################################################################
# In this tutorial, We will be avoiding objects and swerve left and right.
#
#
