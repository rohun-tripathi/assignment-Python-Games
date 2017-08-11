from PIL import Image
import os
import pygame, sys
from pygame.locals import *
import random
from random import shuffle

bif="bg.jpg"
height = 0
width =0
pygame.init()
screen = pygame.display.set_mode((600,400),0,32)
background = pygame.image.load(bif).convert()

#shuff1 = [1,2,3,4,5,6,7,8,9]
x=[1,2,3,4,5,6,7,8,9]
y=[1,2,3,4,5,6,7,8,9]

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

loaded1=pygame.image.load(loadimg1).convert_alpha()
loaded2=pygame.image.load(loadimg2).convert_alpha()
loaded3=pygame.image.load(loadimg3).convert_alpha()
loaded4=pygame.image.load(loadimg4).convert_alpha()
loaded5=pygame.image.load(loadimg5).convert_alpha()
loaded6=pygame.image.load(loadimg6).convert_alpha()
loaded7=pygame.image.load(loadimg7).convert_alpha()
loaded8=pygame.image.load(loadimg8).convert_alpha()
loaded9=pygame.image.load(loadimg9).convert_alpha()

while True:
    mx,my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    if event.type == MOUSEBUTTONDOWN:
        outx[0] = x[0] + loaded1.get_width()
        outy[0] = y[0] + loaded1.get_height()
        outx[1] = x[1] + loaded2.get_width()
        outy[1] = y[1] + loaded2.get_height()
        if mx < outx[0]  and mx > x[0] and my > y[0] and my < outy[0]:
            check[0]=1
        elif mx < outx[1]  and mx > x[1] and my > y[1] and my < outy[1]:
            check[1]=1
            

    elif event.type == MOUSEBUTTONUP:
            check[0] = 0
            check[1] = 0
    
     


    screen.blit(background,(0,0))
    if check[0] == 1:
            x[0],y[0] = pygame.mouse.get_pos()
            x[0] -= loaded1.get_width()/2
            y[0] -= loaded1.get_height()/2
    if check[1] == 1:
            x[1],y[1] = pygame.mouse.get_pos()
            x[1] -= loaded2.get_width()/2
            y[1] -= loaded2.get_height()/2

            
    screen.blit(loaded1,(x[0],y[0]))
    screen.blit(loaded2,(x[1],y[1]))
    screen.blit(loaded3,(x[2],y[2]))
    screen.blit(loaded4,(x[3],y[3]))
    screen.blit(loaded5,(x[4],y[4]))
    screen.blit(loaded6,(x[5],y[5]))
    screen.blit(loaded7,(x[6],y[6]))
    screen.blit(loaded8,(x[7],y[7]))
    screen.blit(loaded9,(x[8],y[8]))


    pygame.display.update()

    
