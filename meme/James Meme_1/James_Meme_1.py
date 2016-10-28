import pygame, sys, time
from pygame.locals import *

pygame.init()
pygame.font.init()
# James' meme test
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
# Defining the display
height = 640
width = 480
display = pygame.display.set_mode((height, width), 0, 32)

# Name that window and set that icon!
bleach = pygame.image.load('bleach.png')
pygame.display.set_caption('Sleepy time')
pygame.display.set_icon(bleach)

#Get dat meme and pute on your clocks
meme = pygame.image.load('classic.jpg')
clock = pygame.time.Clock()

#Define dat meme (potentially all irrelevant, in hindsight)
def Meme(x,y):
    display.blit(meme,(width,height))

#write text on dat meme
font = pygame.font.SysFont("impact", 72)
font2 = pygame.font.SysFont("impact",60)
#show dat meme
display.fill(white)
fontimg = font.render("When Ed's lecture is", 1, white)
fontimg2 = font2.render("9AM monday morning", 1, white)
display.blit(meme,(0,0))
display.blit(fontimg,(10,0))
display.blit(fontimg2,(50,400))
pygame.display.update()
#clock dat meme, just in case animated in future
pygame.time.Clock()
time.sleep(0.01)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
