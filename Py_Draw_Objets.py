#
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Drawing')

# SET COLOR
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)

# SET
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60,60), (120,60), 10)
pygame.draw.line(DISPLAYSURF, BLUE, (120,60), (60,120))
pygame.draw.line(DISPLAYSURF, BLUE, (60,120), (120,120), 10)
pygame.draw.circle(DISPLAYSURF, RED, (300,100), 80, 10)          # (x,y), Radious, Thickness
pygame.draw.ellipse(DISPLAYSURF, BLUE, (50,200, 100, 80), 5)
pygame.draw.rect(DISPLAYSURF, BLUE, (200,150,100,100))           # rect (x,y,dx,dy)

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj [380][280] = BLACK
pixObj [382][282] = BLACK
pixObj [384][284] = BLACK
pixObj [386][286] = BLACK
pixObj [388][299] = BLACK
del pixObj

# main LOOP
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
