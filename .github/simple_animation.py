# Simple Animation with PyGame, Zeigler Jeffrey, 1/5/22, 2:48PM, v0.1

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!') 