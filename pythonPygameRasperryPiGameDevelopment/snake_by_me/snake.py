import pygame
import os
import sys
import random
from pygame.locals import *

# The following 11 functions are defined :
# drawData
# drawGameOver
# drawSnake
# drawWalls
# headHitBody
# headHitWall
# loadimages
# loadMapFile
# loseLife
# positionBerry
# updateGame

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)


class Position(object):
    # This holds the position of a map block.
    # We use the constructor method to pass in the x,y coordinates

    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameData(object):

    # GameData holds just about everything we need to store about the game
    # The majority of the data is for the player's snake.

    # The snake starts out with 2 blocks that are represented by
    # 2 instances of the Position class; that means that it has 1 head segment and 1 tail segment.

    # the number of tail segments grow every time a berry is consumed.

    def __init__(self):
        # the number of lives the player has left
        self.lives = 3

        # set to True when snake touches tail / wall
        self.isDead = False

        # the list of blocks that make up the tail of the snake
        self.blocks = []

        # the running total used to count down to the next animation frame in milliseconds
        self.tick = 250

        # the default tick speed in milliseconds
        self.speed = 250

        # the current level of difficulty
        self.level = 1

        # The number of berries consumed by the snake in this level
        self.berryCount = 0

        # the number of segments added when a berry is consumed.
        # This value changes each level.
        self.segments = 1

        # the current animation frame used to draw the snake's head
        # the snake has 2 forms of animation
        self.frame = 0

        berry_x = random.randint(1, 38)
        berry_y = random.randint(1, 28)

        self.berry = Position(berry_x, berry_y)
        self.blocks.append(Position(20, 15))
        self.blocks.append(Position(19, 15))

        # the snake cannot reverse direction
        self.direction = 0  # 0 = right, 1 = left, 2 = up, 3 = down


def loseLife(GameData):
    pass


def positionBerry(GameData):
    pass


def loadMapFile(fileName):
    return None


def headHitBody(GameData):
    return False


def headHitWall(map, GameData):
    return False


def drawData(surface, GameData):
    pass


def drawGameOver(surface):
    pass


def drawWalls(surface, image, map):
    pass


def drawSnake(surface, image, GameData):
    pass


def updateGame(GameData, gameTime):
    pass


def loadImages():
    return {}
