import pygame
import os
import sys
from pygame.locals import *
import math
import time
import random

pygame.init()

display_width = 800
display_height = 600

fpsClock = pygame.time.Clock()
pygame.display.set_caption('Desert_runner')
surface = pygame.display.set_mode((display_width, display_height))

desert_background = pygame.image.load('desert_cropped.png')
skeleton_image = pygame.image.load('skeleton_severly_cropped.png')
grass_block_image = pygame.image.load('dirt_block.png')

# ================== Default coordinates ==================
# skeleton_x = display_width + (-720)  # 800-720 = 80
# skeleton_y = display_height + (-160)  # 600-160 = 440

# grass_x = display_width + (-400)  # 800-400 = 400
# grass_y = display_height + (-120)  # 600-120 = 480

skeleton_x, skeleton_y = (display_width + (-720), display_height + (-160))
grass_x, grass_y = (display_width + (-400), display_height + (-120))


def skeleton(x, y):
    surface.blit(skeleton_image, (x, y))


def grass_block(x, y):
    surface.blit(grass_block_image, (x, y))


def things_dodged(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


grass_x = random.randrange(0, display_width + 100)
grass_block_speed = 1
grass_x -= grass_block_speed

y_change = 0
crashed = False
while not crashed:
    
    surface.blit(desert_background, (0, 0))
    skeleton(skeleton_x, skeleton_y)
    grass_block(grass_x, grass_y)
    grass_x = random.randrange(0, display_width + 100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_change -= 47
                skeleton_y += y_change
        # TODO : Change the jumping mechanism
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                y_change += 47
                skeleton_y = 440
        print(event)

    pygame.display.update()
    fpsClock.tick(60)


pygame.quit()
quit()
