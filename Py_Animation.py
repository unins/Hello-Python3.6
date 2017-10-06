# page = 46
import sys, pygame
from pygame.locals import *

pygame.init()

FPS = 30            # Frame Per Second
fpsCLOCK = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('./img/cat.jpg')
catx = 10
caty = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        catx += 5
        if catx == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'right':
        catx -= 5
        if catx == 18:
            direction = 'right'
DISPLAYSURF.blit(catImg, (catx, caty))

for event in pygame.event.get():
    if event.type == QUTI:
        pygame.QUIT()
        sys.exit()
pygame.display.update()
fpsCLOCK.tick(FPS)
