# this code will work for one image
# the drag and drop causes the position to jump to position such thet the mouse pointer is in the center of the image. this can be changed later on.


bif="bg.jpg"
mif="ball.png"
img2="basket.png"


import pygame, sys
from pygame.locals import *
import cv2
import cv2.cv as cv
import numpy as np

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(bif).convert()
mouse_c = []

mouse_c.append(pygame.image.load(img2).convert_alpha())
mouse_c.append(pygame.image.load(mif).convert_alpha())


check=[0,0,0,0,0,0,0,0,0]
x=[50,150]
y=[50,150]
outx = [799,799]
outy = [799,799]
stored=  [1,0]

while True:
    mx,my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if event.type == MOUSEBUTTONDOWN:
        outx[0] = x[0] + mouse_c[0].get_width()
        outy[0] = y[0] + mouse_c[0].get_height()
        outx[1] = x[1] + mouse_c[1].get_width()
        outy[1] = y[1] + mouse_c[1].get_height()
        if mx < outx[0]  and mx > x[0] and my > y[0] and my < outy[0]:
            check[0]=1
        elif mx < outx[1]  and mx > x[1] and my > y[1] and my < outy[1]:
            check[1]=1
        elif mx >400 and mx < 500  and my > 500 and my <600:
            break

    elif event.type == MOUSEBUTTONUP:
        for index in range(2):
            if check[index] == 1:
                break
        for i in range(2):
            check[i]=0
        if x[index] > 368  and 432 > x[index] and 132 > y[index] and 68 < y[index]:
            x[index]=  400
            y[index] = 100
        elif x[index] > 368  and 432 > x[index] and 232 > y[index] and 168 < y[index]:
            x[index]=  400
            y[index] = 200

            #screen.blit(mouse_c,(x,y))
            #pygame.event.get()

    
    screen.blit(background,(0,0))
    screen.lock()
    pygame.draw.rect(screen,(140,240,130),Rect((400,100),(64,64)))
    pygame.draw.rect(screen,(140,240,130),Rect((400,200),(64,64)))

    screen.unlock()
    if check[0] == 1:
            x[0],y[0] = pygame.mouse.get_pos()
            x[0] -= mouse_c[0].get_width()/2
            y[0] -= mouse_c[0].get_height()/2
    if check[1] == 1:
            x[1],y[1] = pygame.mouse.get_pos()
            x[1] -= mouse_c[1].get_width()/2
            y[1] -= mouse_c[1].get_height()/2

            
    temp1=x[0]
    temp2=y[0]
    
    screen.blit(mouse_c[0],(temp1,temp2))
    temp1=x[1]
    temp2=y[1]
    
    screen.blit(mouse_c[1],(temp1,temp2))
    
    for k in range(2):
        for f in range(2):
             if x[k] == 400 and y[k] == 100 + 100*f:
                 stored[f]=k


    tex = 0
    path = ['basket.png','ball.png']
    mat = []
    checkmat = []
    
    mat.append(cv.LoadImageM(path[0], cv.CV_LOAD_IMAGE_UNCHANGED))
    mat.append(cv.LoadImageM(path[1], cv.CV_LOAD_IMAGE_UNCHANGED))

    checkmat.append(cv.LoadImageM(path[stored[0]], cv.CV_LOAD_IMAGE_UNCHANGED))
    checkmat.append(cv.LoadImageM(path[stored[1]], cv.CV_LOAD_IMAGE_UNCHANGED))
    
    #hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
    for k in range(2):
        for i in xrange(mat[0].cols):
            for j in xrange(mat[0].rows):
                # multiply all 3 components by 0.5
                if(mat[k][j, i] != checkmat[k][j,i]):# tuple(c*0.5 for c in mat[y, x])
                    tex=1
                  #  print "we r here"

    if(tex == 0):
        pygame.display.quit()
        break

    
    pygame.display.update()

