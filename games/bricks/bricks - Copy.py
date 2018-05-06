import pygame
import os
import sys
from pygame.locals import *
import math
import time
import random
import copy

pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption('Bricks')
main_surface = pygame.display.set_mode((800, 600))
BLACK = pygame.Color(0, 0, 0)

# bat init
bat = pygame.image.load('bat.png')
player_y = 540
bat_rect = bat.get_rect()
# print(bat_rect)

# they represent the coordinates of the bat in 2D space on the screen.
mouse_x, mouse_y = (0, player_y)

# ================ ball init ================
ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()
# print(ball_rect)
ball_start_y = 200
ball_speed = 3
ball_served = False

bx, by = (24, ball_start_y)
sx, sy = (ball_speed, ball_speed)
ball_rect.topleft = (bx, by)

# =========== brick init ===========
brick = pygame.image.load('brick.png')
bricks = []

for y in range(5):
    brick_y = (y * 24) + 100
    # print(str(brick_y) + " brick_y")
    for x in range(10):
        brick_x = (x * 31) + 245
        # print(str(brick_x) + " brick_x")
        # print(brick.get_width())
        # print(brick.get_height())
        # print(list(bricks))
        # print(bricks[0][0])
        bricks.append(Rect(brick_x, brick_y, brick.get_width(), brick.get_height()))


while True:
    main_surface.fill(BLACK)

    # ================= brick draw =================
    for b in bricks:
        # print(b)  # Rect(brick_x, brick_y, brick.get_width, brick.get_height)
        main_surface.blit(brick, b)
    # ================= bat and ball draw =================
    main_surface.blit(bat, bat_rect)
    main_surface.blit(ball, ball_rect)

    # ================= events =================
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            # print(event.pos)
            if mouse_x < (800-55):
                bat_rect.topleft = (mouse_x, player_y)
            else:
                bat_rect.topleft = (800-55, player_y)
        elif event.type == MOUSEBUTTONUP:
            if not ball_served:
                ball_served = True
    # ================= main game logic =================
    if ball_served:
        bx += sx  # 24 += 3
        by += sy  # 200 += 3
        ball_rect.topleft = (bx, by)

    if by <= 0:
        by = 0
        sy *= -1

    if by >= 600 - 8:
        # by = 600 - 8  # 592
        # sy *= -1

        # Out of bounds
        ball_served = False
        bx, by = (24, ball_start_y)
        ball_rect.topleft = (bx, by)
    if bx <= 0:
        bx = 0
        sx *= -1

    if bx >= 800-8:
        bx = 800-8  # 792
        sx *= -1

    if ball_rect.colliderect(bat_rect):
        by = player_y - 8  # 540 - 8 = 532
        sy *= -1

    # ================= collision detection =================
    brick_hit_index = ball_rect.collidelist(bricks)
    hide_bricks_list = []

    if brick_hit_index >= 0:
        hide_bricks_list.append(bricks[brick_hit_index])  # hb is a number
        print(brick_hit_index)
    print(hide_bricks_list)
    # for b in hide_bricks_list:
    #     print(b[0])

    midpoint_of_ball_x = bx + 4
    midpoint_of_ball_y = bx + 4
    # bricks[hb][0] + bricks[hb][2]
    # hb.x + hb.width

    for b in hide_bricks_list:
        if midpoint_of_ball_x > b[0] + b[2] or midpoint_of_ball_x < b[0]:
            sx *= -1
        else:
            sy *= -1

    if brick_hit_index == -1:
        pass
    else:
        for b in hide_bricks_list:
            if b in bricks:
                bricks.remove(b)

    pygame.display.update()
    fpsClock.tick(30)
