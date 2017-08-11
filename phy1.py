bif="bg.jpg"
mif="ball.png"

import pygame, sys,os,math,pygame.mixer
from pygame.locals import *

pygame.init()
black = 0,0,0
white = 255,255,255
screen = pygame.display.set_mode((640,360),0,32)
background = pygame.image.load(bif).convert()
#ball = pygame.image.load(mif).convert_alpha()
class MyCircle:
    def __init__(self,(x,y),size,color,width):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.width = width
    def display(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size,self.width)
x =0
clock = pygame.time.Clock()
speed = 250
my_circle = MyCircle((100,200),100,black,4)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    my_circle.display()
    screen.fill(white)
    #screen.blit(background,(0,0))
    #screen.blit(ball,(x,160))
    #milli = clock.tick()
    #seconds = milli/1000.0
    #dm = seconds*speed
    #x = x + dm

   # if x>640:
   #     x = 0
    
    
     
    pygame.display.update()
    
