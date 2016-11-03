import pygame, sys
from pygame.locals import *
pygame.init()

Black = (0, 0, 0)
White = (255, 255, 255)

Height = 800
Width = 533

Display = pygame.display.set_mode((Height, Width), 0, 32)

knight = pygame.image.load('knight.png')
pygame.display.set_icon(knight)
pygame.display.set_caption("Take back Jerusalem")

# Meme text font, size, anti-aliasing and colour
Textfont = pygame.font.SysFont("impact", 45)
Fontimg = Textfont.render("When you were supposed to go crusading", 1, White)
Textfont2 = pygame.font.SysFont("impact", 50)
Fontimg2 = Textfont2.render("but your squad ditches you", 1, White)

# Loads, draws and updates the meme/display
Meme = pygame.image.load("loneknight.png")
Display.blit(Meme, (0, 0))
Display.blit(Fontimg, (20, 10))
Display.blit(Fontimg2, (120, 450))
pygame.display.update()


while True:

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            elif event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                 sys.exit()