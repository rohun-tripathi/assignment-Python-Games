from PIL import Image
import os
import pygame, sys
from pygame.locals import *
import random
from random import shuffle

import cv2
import cv2.cv as cv
import numpy as np


bif="bg.jpg"
mif="ball.png"
img2="basket.png"

height = 0
width =0

pygame.init()

screen = pygame.display.set_mode((700,500),0,32)
background = pygame.image.load(bif).convert()

x=[1,2,3,4,5,6,7,8,9]
y=[1,2,3,4,5,6,7,8,9]
stored=  [1,0,1,0,1,0,1,0,1]

check = [0,0,0,0,0,0,0,0,0]

t1=[70,140,210]
t2=[70,140,210]
shuffle(t1)
shuffle(t2)

x[0] = t1[0]
y[0] = t2[0]
x[1] = t1[0]
y[1] = t2[2]
x[2] = t1[1]
y[2] = t2[1]
x[3] = t1[1]
y[3] = t2[2]
x[4] = t1[2]
y[4] = t2[0]
x[5] = t1[2]
y[5] = t2[2]
x[6] = t1[1]
y[6] = t2[0]
x[7] = t1[0]
y[7] = t2[1]
x[8] = t1[2]
y[8] = t2[1]


outx = [1099,1099]
outy = [1099,1099]

def crop(infile,height,width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(3):
        for j in range(3):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

if __name__=='__main__':
    infile="jennifer.png"
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    height = imgheight//3
    width = imgwidth//3
    print(height)
    start_num=1
    for k,piece in enumerate(crop(infile,height,width),start_num):
        img=Image.new('RGB', (height,width), 255)
        img.paste(piece)
        path=os.path.join('C:\Users\Rohun\Desktop\game1',"IMG-%s.png" % k)
        img.save(path)

loadimg1 = "IMG-1.png"
loadimg2 = "IMG-2.png"
loadimg3 = "IMG-3.png"
loadimg4 = "IMG-4.png"
loadimg5 = "IMG-5.png"
loadimg6 = "IMG-6.png"
loadimg7 = "IMG-7.png"
loadimg8 = "IMG-8.png"
loadimg9 = "IMG-9.png"


loaded = []

loaded.append(pygame.image.load(loadimg1).convert_alpha())
loaded.append(pygame.image.load(loadimg2).convert_alpha())
loaded.append(pygame.image.load(loadimg3).convert_alpha())
loaded.append(pygame.image.load(loadimg4).convert_alpha())
loaded.append(pygame.image.load(loadimg5).convert_alpha())
loaded.append(pygame.image.load(loadimg6).convert_alpha())
loaded.append(pygame.image.load(loadimg7).convert_alpha())
loaded.append(pygame.image.load(loadimg8).convert_alpha())
loaded.append(pygame.image.load(loadimg9).convert_alpha())


while True:
    mx,my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    if event.type == MOUSEBUTTONDOWN:
        outx[0] = x[0] + loaded[0].get_width()
        outy[0] = y[0] + loaded[0].get_height()
        outx[1] = x[1] + loaded[1].get_width()
        outy[1] = y[1] + loaded[1].get_height()
        if mx < outx[0]  and mx > x[0] and my > y[0] and my < outy[0]:
            check[0]=1
        elif mx < outx[1]  and mx > x[1] and my > y[1] and my < outy[1]:
            check[1]=1
            

    elif event.type == MOUSEBUTTONUP:

        for index in range(2):
            if check[index] == 1:
                break

        for i in range(2):
            check[i]=0

        if x[index] > 368  and 432 > x[index] and 102 > y[index] and 38 < y[index]:
            x[index]=  400
            y[index] = 70
        elif x[index] > 368  and 432 > x[index] and 172 > y[index] and 108 < y[index]:
            x[index]=  400
            y[index] = 140
        elif x[index] > 368  and 432 > x[index] and 242 > y[index] and 178 < y[index]:
            x[index]=  400
            y[index] = 210
        elif x[index] > 438 and 502 > x[index] and 102 > y[index] and 38 < y[index]:
            x[index]=  470
            y[index] = 70
        elif x[index] > 438  and 502 > x[index] and 172 > y[index] and 108 < y[index]:
            x[index]=  470
            y[index] = 140
        elif x[index] > 438  and 502 > x[index] and 242 > y[index] and 178 < y[index]:
            x[index]=  470
            y[index] = 210
        elif x[index] > 508  and 572 > x[index] and 102 > y[index] and 38 < y[index]:
            x[index]=  540
            y[index] = 70
        elif x[index] > 508  and 572 > x[index] and 172 > y[index] and 108 < y[index]:
            x[index]=  540
            y[index] = 140
        elif x[index] > 508  and 572 > x[index] and 242 > y[index] and 178 < y[index]:
            x[index]=  540
            y[index] = 210
            

    
     


    screen.blit(background,(0,0))
    
    screen.lock()
    pygame.draw.rect(screen,(140,240,130),Rect((400,70),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((400,140),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((400,210),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((470,70),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((470,140),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((470,210),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((540,70),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((540,140),(60,60)))
    pygame.draw.rect(screen,(140,240,130),Rect((540,210),(60,60)))
    screen.unlock()

    for ncount in range(9):
        if check[ncount] == 1:
            x[ncount],y[ncount] = pygame.mouse.get_pos()
            x[ncount] -= loaded[ncount].get_width()/2
            y[ncount] -= loaded[ncount].get_height()/2
            break
        
            
    screen.blit(loaded[0],(x[0],y[0]))
    screen.blit(loaded[1],(x[1],y[1]))
    screen.blit(loaded[2],(x[2],y[2]))
    screen.blit(loaded[3],(x[3],y[3]))
    screen.blit(loaded[4],(x[4],y[4]))
    screen.blit(loaded[5],(x[5],y[5]))
    screen.blit(loaded[6],(x[6],y[6]))
    screen.blit(loaded[7],(x[7],y[7]))
    screen.blit(loaded[8],(x[8],y[8]))

    for top in range(9):
        for k in range(3):
            for f in range(3):
                 if x[top] == 400 + 70*f and y[top] == 70 + 70*k:
                     stored[k*3 + f]=top
                     break

    tex = 0

    path = []
    for mcount in range(9):
        mcounter = mcount+1
        path.append(os.path.join('C:\Users\Rohun\Desktop\game1',"IMG-%s.png" % mcounter))

    mat = []
    checkmat = []
    
    for ncount in range(9):
        mat.append(cv.LoadImageM(path[ncount], cv.CV_LOAD_IMAGE_UNCHANGED))
        checkmat.append(cv.LoadImageM(path[stored[ncount]], cv.CV_LOAD_IMAGE_UNCHANGED))
    
    #hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
    for k in range(9):
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

    
