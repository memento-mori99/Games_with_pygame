import pygame
import math
import time
import random

pygame.init()

display_width = 800
display_height = 600

# colour variable = (red, green, blue)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (150, 65, 0)
block_color = (0, 128, 0)
block_color2 = (0, 253, 221)

car_width = 73
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car-py')
clock = pygame.time.Clock()
carimg = pygame.image.load('racecar.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):  # x coordinate, y coordinate, width, height
    # things are the obstacles (the green boxes that must be dodged to avoid crashing)
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carimg, (x, y))  # x and y has to be a tuple()


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2.0), (display_height/2.0))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()  # it resets the game_loop function which in turn also resets the dodged variable


def crash():
    message_display("You crashed!")


def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
        gameDisplay.fill(block_color2)
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("Welcome !", largeText)
        TextRect.center = ((display_width/2.0), (display_height/2.0))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.80)
    x_change = 0

    thing_startx = random.randrange(0, display_width - 100)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    thing_count = 1
    dodged = 0

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # if key is presses
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(brown)
        # things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0 - car_width:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            # if dodged % 10 == 0:
            #     thing_speed += 1
            # thing_speed +=1              # These are to make the game a bit harder
            # thing_width += (dodged * 1.2)  # These are to make the game a bit harder
            thing_count += 1

            for thing in range(thing_count):
                print(thing)

        if y < thing_starty + thing_height:
            print('y cross over')
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x cross over")
                crash()

        pygame.display.update()  # pygame.display.flip()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
