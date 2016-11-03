import pygame, sys
from pygame.locals import *
pygame.init()

Black = (0, 0, 0)
White = (255, 255, 255)

Height = 644
Width = 483

Display = pygame.display.set_mode((Height, Width), 0, 32)

knight = pygame.image.load('shh.png')
pygame.display.set_icon(knight)
pygame.display.set_caption("pls stop")

# Meme text font, size, anti-aliasing and colour
Textfont = pygame.font.SysFont("impact", 45)
Fontimg = Textfont.render("When someone is about to remind", 1, White)
Textfont2 = pygame.font.SysFont("impact", 50)
Fontimg2 = Textfont2.render("the teacher about homework", 1, White)

# Loads, draws and updates the meme/display
Meme = pygame.image.load("shh.png")
Display.blit(Meme, (0, 0))
Display.blit(Fontimg, (11, 10))
Display.blit(Fontimg2, (32, 415))
pygame.display.update()


while True:

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            elif event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                 sys.exit()