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

# Kitchen Cat Meme (Press 'k' on keyboard)
def kitchencats():
    kitchencatsImg = pygame.image.load('kitchencats.jpg')
    font = pygame.font.SysFont('Roman', 90)
    text = font.render('When a flatmate', True, (255, 255, 255))
    text2 = font.render("won't wash up.", True, (255, 255, 255))
    window.blit(kitchencatsImg, (0, 0))
    window.blit(text, (20, 10))
    window.blit(text2, (60, 100))

# Kitchen Cat Meme - Red (Press 'r' on keyboard)
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

# Kitchen Cat Meme - Green (Press 'g' on keyboard)
def makegreen():
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

            Red = 255 - Red
            Green = 255
            Blue = 255 - Blue

            PXArray[X, Y] = (Red, Green, Blue)

#Kitchen Cat Meme - Blue (Press 'b' on keyboard)
def makeblue():
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

            Red = 255 - Red
            Green = 255 - Green
            Blue = 255

            PXArray[X, Y] = (Red, Green, Blue)

# Kitchen cat meme - convert to negative (Press 'n' on keyboard)
def negative():
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

            Red = 255 - Red
            Green = 255 - Green
            Blue = 255 - Blue

            PXArray[X,Y] = (Red, Green, Blue)

# Ed's Lecture Meme (Press 'e' on keyboard)
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

# Crusading Meme (Press 'c' on keyboard)
def crusadememe():

    knight = pygame.image.load('knight.png')
    pygame.display.set_icon(knight)
    pygame.display.set_caption("Take back Jerusalem")

    # Meme text font, size, anti-aliasing and colour
    Textfont = pygame.font.SysFont("impact", 45)
    Fontimg = Textfont.render("When you were supposed to go crusading", 1, white)
    Textfont2 = pygame.font.SysFont("impact", 50)
    Fontimg2 = Textfont2.render("but your squad ditches you", 1, white)

    # Loads, draws and updates the meme/display
    Meme = pygame.image.load("loneknight.png")
    window.blit(Meme, (0, 0))
    window.blit(Fontimg, (20, 10))
    window.blit(Fontimg2, (120, 450))
    pygame.display.update()

# Homework Meme (Press 'h' on keyboard)
def homeworkmeme():

    knight = pygame.image.load('shh.png')
    pygame.display.set_icon(knight)
    pygame.display.set_caption("pls stop")

    # Meme text font, size, anti-aliasing and colour
    Textfont = pygame.font.SysFont("impact", 45)
    Fontimg = Textfont.render("When someone is about to remind", 1, white)
    Textfont2 = pygame.font.SysFont("impact", 50)
    Fontimg2 = Textfont2.render("the teacher about homework", 1, white)

    # Loads, draws and updates the meme/display
    Meme = pygame.image.load("shh.png")
    window.blit(Meme, (0, 0))
    window.blit(Fontimg, (11, 10))
    window.blit(Fontimg2, (32, 415))
    pygame.display.update()

# set up program loop
while not image:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            image = True
        if event.type == KEYDOWN and event.key == K_k:
            window_width = 1280
            window_height = 875
            window = pygame.display.set_mode((window_width, window_height))
            kitchencats()
        if event.type == KEYDOWN and event.key == K_r:
            window_width = 1280
            window_height = 875
            window = pygame.display.set_mode((window_width, window_height))
            makered()
        if event.type == KEYDOWN and event.key == K_g:
            window_width = 1280
            window_height = 875
            window = pygame.display.set_mode((window_width, window_height))
            makegreen()
        if event.type == KEYDOWN and event.key == K_b:
            window_width = 1280
            window_height = 875
            window = pygame.display.set_mode((window_width, window_height))
            makeblue()
        if event.type == KEYDOWN and event.key == K_n:
            window_width = 1280
            window_height = 875
            window = pygame.display.set_mode((window_width, window_height))
            negative()
        if event.type == KEYDOWN and event.key == K_e:
            window_width = 640
            window_height = 480
            window = pygame.display.set_mode((window_width, window_height))
            edlecture()
        if event.type == KEYDOWN and event.key == K_c:
            window_width = 800
            window_height = 533
            window = pygame.display.set_mode((window_width, window_height))
            crusadememe()
        if event.type == KEYDOWN and event.key == K_h:
            window_width = 644
            window_height = 483
            window = pygame.display.set_mode((window_width, window_height))
            homeworkmeme()

    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()