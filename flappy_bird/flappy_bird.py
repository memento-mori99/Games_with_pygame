import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')
main_surface = pygame.display.set_mode((800, 600))
BLACK = pygame.Color(0, 0, 0)

# initialise all things here


while True:
    main_surface.blit()

    # draw something

    # draw something

    # draw something

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # main game logic

    pygame.display.update()  # pygame.display.flip()
    clock.tick(60)  # 60 frames

pygame.quit()
quit()
