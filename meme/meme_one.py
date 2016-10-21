import pygame, sys
from pygame.locals import *

#Hannah meme
#test for importing image

pygame.init()

#defines window size
width = 1000
height = 900

#sets window display and captions as Spyro
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Spyro')

#defines black and white variables
black = (0, 0, 0)
white = (255, 255, 255)

#sets image variable to false and loads Spyro.jpg
image = False
spyroImg = pygame.image.load('Spyro.jpg')

#defines spyro variable and blits image
def spyro(x, y):
    window.blit(spyroImg, (x, y))

#defines x, y for image placement
x = (0)
y = (0)

#fills screen with white and draws Spyro image on window
window.fill(white)
spyro(x, y)

pygame.display.update()

#for quitting game
while not image:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
