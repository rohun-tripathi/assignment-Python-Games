bif="bg.jpg"
mif="ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render("Some text!", 1, (255,255,0))
x,y=0,0
movex,movey = 0,0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -1
            elif event.key == K_RIGHT:
                movex = +1
            elif event.key == K_UP:
                movey = -1
            elif event.key == K_DOWN:
                movey = +1

        if event.type == KEYUP:
             if event.key == K_LEFT:
                 movex = 0
             elif event.key == K_RIGHT:
                movex = 0
             elif event.key == K_UP:
                movey = 0
             elif event.key == K_DOWN:
                movey = 0
    x += movex
    y += movey

    screen.blit(background,(0,0))
    screen.blit(mouse_c,(x,y))
    screen.blit(label, (200, 100))
    pygame.display.update()
    
