import pygame
from pygame.locals import *
import numpy as np
import sys
#COLOR TABLE
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 150)
WHITE = (255, 255, 255)

h = 0.05
t = v = 0
x = 45*np.pi/180
pen_fm = 0.01
pen_m = 0.1
pen_l = 100*0.01
pen_J = 0.02
pen_g = 9.8
gndCenterX = 150
gndCenterY = 20
penLength = pen_l*100*2

FPSCLOCK = pygame.time.Clock()

def terminate():
    print('\tPROGRAM IS TERMINATED!!....')
    pygame.quit()
    sys.exit()

def calcODEFunc(tVal, xVal, vVal):
	return -pen_fm/(pen_m*pen_l**2+pen_J)*vVal-pen_m*pen_g*pen_l/(pen_m*pen_l**2+pen_J)*xVal

def solveODEusingRK4(t, x, v):
	kx1 = v
	kv1 = calcODEFunc( t, x, v )

	kx2 = v + h*kv1/2
	kv2 = calcODEFunc( t + h/2, x + h*kx1/2, v + h*kv1/2 )

	kx3 = v + h*kv2/2
	kv3 = calcODEFunc( t + h/2, x + h*kx2/2, v + h*kv2/2 )

	kx4 = v + h*kv3
	kv4 = calcODEFunc( t + h, x + h*kx3, v + h*kv3 )

	dx = h*(kx1 + 2*kx2 + 2*kx3 + kx4)/6
	dv = h*(kv1 + 2*kv2 + 2*kv3 + kv4)/6

	return x+dx, v+dv

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300,300))

DISPLAYFONT_BIG = pygame.font.SysFont('Vernada.ttf', 25)
DISPLAYFONT_MID = pygame.font.SysFont('Vernada.ttf', 22)
DISPLAYFONT_SMALL = pygame.font.SysFont('Vernada.ttf', 18)
FONTSURF_01 = DISPLAYFONT_BIG.render('WEHRMACHT PROJEKT', True, RED)
FONTSURF_02 = DISPLAYFONT_BIG.render('Pendel Simulator', True, BLACK)


loopFlag = True

while loopFlag:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            elif event.key == K_SPACE:
                h = 0.05                # time increasement (sec)
                t = v = 0               # time & velocity (sec, m/sec)
                x = 45 * np.pi / 180    # 30 degree * PI() / 180

                pen_fm = 0.01           # fm =
                pen_m = 0.1             # m = mass (kg)
                pen_l = 100 * 0.01      # l = length of string (m)
                pen_J = 0.02            # j =
                pen_g = 9.8             # g = acceleration of Gravity (m/sec**2)

                gndCenterX = 150        # tied positon (center = 300 / 2)
                gndCenterY = 20         # Margin of Ceiling = 20 px.
                penLength = pen_l * 100 * 2 # length of string = multiple 100 times for ANIM.

    FONTSURF_03 = DISPLAYFONT_SMALL.render('Press SPACE to restart                    TIME: %4.2f sec' %t, True, GRAY)

    print('time: %3.2f  X: %3.100f  V: %3.100f' %(t, x, v))

    DISPLAYSURF.fill(WHITE)

    t = t + h
    [x, v] = solveODEusingRK4(t,x,v)

    updatedX = gndCenterX + penLength*np.sin(x)
    updatedY = gndCenterY + penLength*np.cos(x)

    pygame.draw.line(DISPLAYSURF, BLACK, (gndCenterX, gndCenterY), (updatedX, updatedY), 2)
    pygame.draw.circle(DISPLAYSURF, RED, (int(updatedX), int(updatedY)), 20, 0)

    pygame.draw.line(DISPLAYSURF, BLACK, (10,20), (290,20), 10)
    DISPLAYSURF.blit(FONTSURF_01, (10,270))
    DISPLAYSURF.blit(FONTSURF_02, (10,250))
    DISPLAYSURF.blit(FONTSURF_03, (10,3))

	# pygame.time.delay(40)
	# pygame.display.flip()

    pygame.display.update()
    FPSCLOCK.tick(5000)
