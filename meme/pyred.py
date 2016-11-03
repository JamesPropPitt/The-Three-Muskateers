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

#def get_screen():
 #   for X in range ((0, window_width)):
  #      for Y in range ((0, window_height)):
   #         Red = window.get_at((X, Y)).r
    #        Green = window.get_at((X, Y)).g
     #       Blue = window.get_at((X, Y)).b
# This block of code is experimental.



# set colour variables
black = (0, 0, 0)
white = (255, 255, 255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

# load kitchencat image
image = False
kitchencatsImg = pygame.image.load('kitchencats.jpg')

# set up font and text
font = pygame.font.SysFont('Impact', 90)
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
kitchencats(x, y)

pygame.display.update()

PXArray = pygame.PixelArray(window)

# Makes image red, when r is pressed
def makered():
    for Y in range(0, window_height):
        for X in range(0, window_width):

            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b

            Red = 255
            Green = 255 - Green
            Blue = 255 - Blue

            PXArray[X, Y] = (Red, Green, Blue)

def makegreen():
    for Y in range(0, window_height):
        for X in range(0, window_width):
             Red = window.get_at((X, Y)).r
             Green = window.get_at((X, Y)).g
             Blue = window.get_at((X, Y)).b

             Red = 255 - Red
             Green = 255
             Blue = 255 - Blue

             PXArray[X, Y] = (Red, Green, Blue)

def makeblue():
    for Y in range(0, window_height):
        for X in range(0, window_width):
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b

            Red = 255 - Red
            Green = 255 - Green
            Blue = 255

            PXArray[X, Y] = (Red, Green, Blue)

def negative():
    for Y in range(0, window_height):
        for X in range(0, window_width):
            Red = window.get_at((X, Y)).r
            Green = window.get_at((X, Y)).g
            Blue = window.get_at((X, Y)).b

            Red = 255 - Red
            Green = 255 - Green
            Blue = 255 - Blue

            PXArray[X,Y] = (Red, Green, Blue)

#def hippie():
 #   for
  #      get_screen()
   # Red = 150
    #Green = 150
    #Blue = 150
#
#
 #           PXArray[X,Y] = (Red, Green, Blue)
# This block of code is experimental.


# set up program loop
while not image:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            image = True
        if event.type == KEYDOWN and event.key == K_r:
            makered()
        if event.type == KEYDOWN and event.key == K_g:
            makegreen()
        if event.type == KEYDOWN and event.key == K_b:
            makeblue()
        if event.type == KEYDOWN and event.key == K_n:
            negative()
        #if event.type ==KEYDOWN and event.key == K_h:
            #hippie()
        pygame.display.update()

pygame.quit()
quit()