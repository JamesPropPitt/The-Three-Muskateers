import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
pygame.font.init()

# set up window size variables
window_width = 1280
window_height = 875

# set up window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Kitchen Cat Fight')

# set colour variables
black = (0, 0, 0)
white = (255, 255, 255)

# load kitchencat image
clock = pygame.time.Clock()
image = False
kitchencatsImg = pygame.image.load('kitchencats.jpg')

# set up font and text
font = pygame.font.SysFont('Roman', 90)
text = font.render('When a flatmate', True, (255, 255, 255))
text2 = font.render("won't wash up.", True, (255, 255, 255))

# blit image to window
def kitchencats(x, y):
    window.blit(kitchencatsImg, (x, y))
    window.blit(text, (20, 10))
    window.blit(text2, (60, 100))

# set image position variables
x = (0)
y = (0)

# set up program loop
while not image:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            image = True

    # fill window white, set kitchencats position on window
    window.fill(white)
    kitchencats(x, y)

    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()