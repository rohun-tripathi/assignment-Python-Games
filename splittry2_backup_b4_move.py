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
t1=[60,120,180]
t2=[60,120,180]
shuffle(t1)
shuffle(t2)

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
     
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(loaded1,(t1[0],t2[0]))
    screen.blit(loaded2,(t1[1],t2[0]))
    screen.blit(loaded3,(t1[2],t2[0]))
    screen.blit(loaded4,(t1[0],t2[1]))
    screen.blit(loaded5,(t1[1],t2[1]))
    screen.blit(loaded6,(t1[2],t2[1]))

    screen.blit(loaded7,(t1[0],t2[2]))
    screen.blit(loaded8,(t1[1],t2[2]))
    screen.blit(loaded9,(t1[2],t2[2]))
    pygame.display.update()


    
