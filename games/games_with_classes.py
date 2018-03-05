import pygame
import math
import time

pygame.init

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (55, 255, 250)
purple = (196, 55, 255)

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill(black)


class Shapes(object):

    def __init__(self, color):
        self.surface = gameDisplay
        self.color = color

    def line(self, start_tuple, end_tuple, width):
        self.start_tuple = start_tuple
        self.end_tuple = end_tuple
        self.width = width
        pygame.draw.line(gameDisplay, self.color, self.start_tuple, self.end_tuple, width)


Triangle = Shapes(blue)
Triangle.line((200, 400), (300, 500), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
