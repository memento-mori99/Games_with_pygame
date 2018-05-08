import pygame
import os
import sys
from pygame.locals import *
import math
import time
import random

pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')
main_surface = pygame.display.set_mode((800, 600))
BLACK = pygame.Color(0, 0, 0)

# initialise all things here


while True:
    main_surface.blit()

    # draw xx

    # draw

    # draw

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # main game logic
