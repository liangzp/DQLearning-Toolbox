# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:37:39 2018

@author: Sunday
"""
import sys,pygame,time,random,math
from pygame.locals import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.master_image=None
        self.frame=0
        self.old_frame=-1
        self.frame_width=1
        self.frame_height=1
        self.first_frame=0
        self.last_frame=0
        self.columns=1
        self.last_time=0
        self.velocity=Point(0,0)
        self.direction=0

        
    #X property    
    def _getx(self):
        return self.rect.x
    def _setx(self,value):
        self.rect.x=value
    X=property(_getx,_setx)
    
    #Y property
    def _gety(self):
        return self.rect.y
    def _sety(self,value):
        self.rect.y=value
    Y=property(_gety,_sety)
    
    #position property
    def _getpos(self):
        return self.rect.topleft
    def _setpos(self,pos):
        self.rect.topleft=pos
    position=property(_getpos,_setpos)
    
    def load(self,filename,width,height,columns):
        self.master_image=pygame.image.load(filename).convert_alpha()
        self.frame_width=width
        self.frame_height=height
        self.columns=columns
        self.rect=Rect(0,0,width,height)
        self.image=self.master_image.subsurface(self.rect)
        rect=self.master_image.get_rect()
        self.last_frame=(rect.width//width)*(rect.height//height)-1
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self,current_time,rate=30):
        if current_time>self.last_time+rate:
            self.frame+=1
            if self.frame>self.last_frame:
                self.frame=self.first_frame
            self.last_time=current_time
        if self.frame!=self.old_frame:
            frame_x=(self.frame%self.columns)*self.frame_width
            frame_y=(self.frame//self.columns)*self.frame_height
            rect=Rect(frame_x,frame_y,self.frame_width,self.frame_height)
            self.image=self.master_image.subsurface(rect)
            self.old_frame=self.frame
                    
    def __str__(self):
        return str(self.frame)+","+str(self.first_frame)+","+str(self.last_frame)+","+str(self.frame_width)+","+str(self.frame_height)+","+str(self.columns)+","+str(self.rect)

def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen=pygame.display.get_surface()
    screen.blit(imgText,(x,y))

class Point(object):
    def __init__(self,x,y):
        self._x=x
        self._y=y
    
    def getx(self):
        return self._x
    def setx(self,value):
        self._x=value
    x=property(getx,setx)
    
    def gety(self):
        return self._y
    def sety(self,value):
        self._y=value
    y=property(gety,sety)
    
    def __str__(self):
        return "{X:"+"{:.0f}".format(self._x)+",Y:"+"{:.0f}".format(self._y)+"}"
    




























                  