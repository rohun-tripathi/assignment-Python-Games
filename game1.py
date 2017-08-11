# this code will work for one image
# the drag and drop causes the position to jump to position such thet the mouse pointer is in the center of the image. this can be changed later on.


bif="bg.jpg"
mif="ball.png"
img2="ball.png"


import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()
mouse_c2=pygame.image.load(img2).convert_alpha()


check=[0,0]
x=[50,150]
y=[50,150]
outx = [799,799]
outy = [799,799]

while True:
    mx,my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if event.type == MOUSEBUTTONDOWN:
        outx[0] = x[0] + mouse_c.get_width()
        outy[0] = y[0] + mouse_c.get_height()
        outx[1] = x[1] + mouse_c2.get_width()
        outy[1] = y[1] + mouse_c2.get_height()
        if mx < outx[0]  and mx > x[0] and my > y[0] and my < outy[0]:
            check[0]=1
        if mx < outx[1]  and mx > x[1] and my > y[1] and my < outy[1]:
            check[1]=1
            

    elif event.type == MOUSEBUTTONUP:
            check[0] = 0
            check[1]=0

            #screen.blit(mouse_c,(x,y))
            #pygame.event.get()

    
    screen.blit(background,(0,0))
    if check[0] == 1:
            x[0],y[0] = pygame.mouse.get_pos()
            x[0] -= mouse_c.get_width()/2
            y[0] -= mouse_c.get_height()/2
    if check[1] == 1:
            x[1],y[1] = pygame.mouse.get_pos()
            x[1] -= mouse_c2.get_width()/2
            y[1] -= mouse_c2.get_height()/2 
    temp1= x[0]
    temp2= y[0]
    screen.blit(mouse_c,(temp1,temp2))
    temp1=x[1]
    temp2=y[1]
    
    screen.blit(mouse_c2,(temp1,temp2))


    pygame.display.update()
    
