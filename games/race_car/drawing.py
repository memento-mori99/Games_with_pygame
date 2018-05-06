import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (55, 255, 250)
purple = (196, 55, 255)

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

# Parameters -> (Surface, color, start_point, end_point, width of line)
pygame.draw.line(gameDisplay, blue, (100, 200), (300, 450), 5)  # Draw a line

# Parameters -> (Surface, color, (Top_left_coordinates_x,Top_left_coordinates_y, width of rectangle, height of rectangle ))
pygame.draw.rect(gameDisplay, green, (400, 400, 50, 25))
pygame.draw.rect(gameDisplay, cyan, (600, 600, 50, 25))
# Specify center of the circle, radius of the circle, width of the circle
pygame.draw.circle(gameDisplay, cyan, (150, 150), 75)

#
pygame.draw.polygon(gameDisplay, purple, ((25, 75), (76, 125), (250, 375), (400, 25)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
