# Pygame Practice
import pygame, sys
from pygame.locals import *

pygame.init()           # if import pygame, init() should always execute in advance
DISPLAYSURF = pygame.display.set_mode((640,480))    # set_mode
pygame.display.set_caption('Hello World~!')         # set_caption

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:                      # event = Quit, press [x]
            pygame.quit()
            sys.exit()
        pygame.display.update()                     # update() Loop
