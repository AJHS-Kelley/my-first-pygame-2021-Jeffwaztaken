# My First PyGame, Jeffrey Zeiger, 11/29/21 2:11pm, v0.6

import pygame, sys
from pygame. locals import *

# Start PyGame
pygame.init()

#setup our window. 1
windowSurface=pygame.display.set_mode((500,400),0, 32)
pygame.display.set_caption('Hello,world!')

# Setup Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CIRCLEPURPLE =(110,97,253)
# Setup text
basicFont=pygame.font.SysFont(None,40)

#setup Text
text=basicFont.render('Hello World', True, WHITE,BLUE)
textRect=text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill background color
windowSurface.fill(BLUE)
windowSurface.fill(CIRCLEPURPLE)
# Draw a polygon onto the screen

pygame.draw.polygon(windowSurface, CIRCLEPURPLE,(146,0), (291,106,) (236,277), (236,277), (56,277), (0,106))

# Draw lines on the screen
pygame.draw.line(windowSurface,RED,(60,60),(120,60),4)
pygame.draw.line(windowSurface,WHITE,(75,60), (60,75),2)
pygame.draw.line(windowSurface,BLUE,(0,150,0),1)

# DRAW a circle.
pygame.draw.circle(windowSurface, BLACK, (300,50), 20, 0)

# DRAW an ellipse.
pygame.draw.ellipse(windowSurface, RED,(300,250,40,80),1)

# DRAW the text rectangle
pygame.draw.rect(windowSurface,RED, (textRect.left -20,textRect.top-20,textRect.windowSurface))

#Create Pixel Array
pixArray= pygame.Pixelarray(windowSurface)
pixArray[480][380]= BLUE
del pixArray

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

# Update Pygame Display
pygame.display.update()

#Run game Loop
while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
