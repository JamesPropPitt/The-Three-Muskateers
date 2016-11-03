import pygame, sys, time
from pygame.locals import *

width = 1000
height = 1000
screen = pygame.display.set_mode((width,height), 0, 32)

pygame.init()
meme = pygame.image.load('classic.jpg')
menu = {"Play", "Options", "Quit"}
while True:
    options=menu.keys()
    options.sort()
    for entry in options:
            print entry,menu[entry]

    uinput=raw_input("Enter a number")
    if uinput =='1':
        screen.blit(meme)

