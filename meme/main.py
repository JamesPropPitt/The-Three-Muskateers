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

# Ed's Lecture Meme (Press e on keyboard)
def edlecture():

    # Meme text font, size, anti-aliasing and colour
    Textfont = pygame.font.SysFont("impact", 72)
    Fontimg = Textfont.render("When Ed's lecture is", 1, white)
    Textfont2 = pygame.font.SysFont("impact", 60)
    Fontimg2 = Textfont2.render("9AM monday morning", 1, white)

    # Loads, draws and updates the meme/display
    Meme = pygame.image.load("classic.jpg")
    window.blit(Meme, (0, 0))
    window.blit(Fontimg, (25, 0))
    window.blit(Fontimg2, (53, 400))
    pygame.display.update()

# set up program loop
while not image:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            image = True
        if event.type == KEYDOWN and event.key == K_k:
            kitchencats()
        if event.type == KEYDOWN and event.key == K_r:
            makered()
        if event.type == KEYDOWN and event.key == K_e:
            edlecture()

    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()