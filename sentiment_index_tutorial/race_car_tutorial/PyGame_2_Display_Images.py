import sys
import os
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("A bit racey")

# A clock is basically going to time things for us
# We use it for frames for second.
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()

    clock.tick(60)
    # 60 Frames in second, 30 Frames in second

pygame.quit()
quit()
