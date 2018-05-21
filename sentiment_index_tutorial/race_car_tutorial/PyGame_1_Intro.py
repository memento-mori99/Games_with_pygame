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
    # pygame.display.update() will accept parameters and it will just update
    # that 1 thing. So the background processing would be a little easier.
    # If you do not put any parameter in there, it will just update the
    # whole surface (window).
    # pygame.display.flip() will update everything.

    clock.tick(60)
    # 60 Frames in second, 30 Frames in second

pygame.quit()
quit()
