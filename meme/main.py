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
pygame.display.set_caption('Memes')

# set colour variables
black = (0, 0, 0)
white = (255, 255, 255)
Red = (255, 0, 0)

clock = pygame.time.Clock()
image = False

x = (0)
y = (0)

# Kitchen Cat Meme (Press k on keyboard)
def kitchencats():
    kitchencatsImg = pygame.image.load('kitchencats.jpg')
    font = pygame.font.SysFont('Roman', 90)
    text = font.render('When a flatmate', True, (255, 255, 255))
    text2 = font.render("won't wash up.", True, (255, 255, 255))
    window.blit(kitchencatsImg, (0, 0))
    window.blit(text, (20, 10))
    window.blit(text2, (60, 100))

# Kitchen Cat Meme - Red (Press r on keyboard)
def makered():
    kitchencatsImg = pygame.image.load('kitchencats.jpg')
    font = pygame.font.SysFont('Roman', 90)
    text = font.render('When a flatmate', True, (255, 255, 255))
    text2 = font.render("won't wash up.", True, (255, 255, 255))
    window.blit(kitchencatsImg, (0, 0))
    window.blit(text, (20, 10))
    window.blit(text2, (60, 100))

    for Y in range(0, window_height):
        for X in range(0, window_width):

            PXArray = pygame.PixelArray(window)
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b

            Red = 255
            Green = 255 - Green
            Blue = 255 - Blue

            PXArray[X, Y] = (Red, Green, Blue)

# set up program loop
while not image:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            image = True
        if event.type == KEYDOWN and event.key == K_k:
            kitchencats()
        if event.type == KEYDOWN and event.key == K_r:
            makered()


    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()