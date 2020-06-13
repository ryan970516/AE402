#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:24:13 2020

@author: anne
"""
'''
import pygame

# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Snake(pygame.sprite.Sprite):
    SIZE = 20
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.Surface([self.SIZE,self.SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()         
        self.rect.x = x
        self.rect.y = y
        
class SnakeBody():
    def __init__(self,length,windowSize ):
        self.group = pygame.sprite.Group()
        self.queue = []
        self.x = 0
        self.y = 0
        self.dir = 0 
        self.eatFood = 0
        self.windowSize = windowSize
        
        for i in range(length):
            self.x += Snake.SIZE
      
            body =  Snake(RED,self.x,self.y)
            
            self.group.add(body)
            self.queue.append(body)
    def move(self, pressed=None):
        self.changeDir(pressed)
        
        if self.dir == 0:
            self.x += Snake.SIZE
            head = Snake(RED, self.x, self.y)
        elif self.dir == 1:
            self.y += Snake.SIZE
            head = Snake(RED, self.x, self.y)
        elif self.dir == 2:
            self.x -= Snake.SIZE
            head = Snake(RED, self.x, self.y)
        else:
            self.y -= Snake.SIZE
            head = Snake(RED, self.x, self.y)
            
            
            
        self.group.add(head)
        self.queue.append(head)
        
        if self.eatFood > 0:
           self.eatFood -= 1
        else:   
            tail = self.queue.pop(0)        
            self.group.remove(tail)
            
    def isOutOfRange(self) -> bool:
        if self.x < 0 or  self.x > self.windowSize[0] or \
        self.y < 0 or self.y > self.windowSize[1]:
            return True
        
        
        
        return False 
            
            
            
            
    
    
    
    def changeDir(self, pressed):
        if  not pressed: return
        if pressed[pygame.K_UP]:
            self.dir = 3
        
        elif pressed[pygame.K_LEFT]:
            self.dir = 2
        elif pressed[pygame.K_RIGHT]:
            self.dir = 0
        elif pressed[pygame.K_DOWN]:
            self.dir = 1
    def Eating(self, foodGroup):
                    
        eatFood = pygame.sprite.groupcollide(self.group, foodGroup, False , True) 
        if eatFood:
            self.eatFood += len(list(eatFood.values())[0])
            
            
    def collideSelf(self):
        tmp = pygame.sprite.Group(self.queue[0:-1])
        hits = pygame.sprite.spritecollide(self.queue[-1], tmp, False)
        return bool(hits)
        
            
            
            
    
            
class Food(pygame.sprite.Sprite):
    SIZE = 20
    def __init__(self, color ,x,y):
        super().__init__()
        self.image = pygame.Surface([self.SIZE,self.SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
                  
'''            
import pygame
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class Snake(pygame.sprite.Sprite):
    SIZE = 20
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.Surface([self.SIZE,self.SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()         
        self.rect.x = x 
        self.rect.y = y
        
class SnakeBody():
    def __init__(self,length,windowSize ):
        self.group = pygame.sprite.Group()
        self.queue = []
        self.x = 0
        self.y = 0
        self.dir = 0 
        self.eatFood = 0
        self.windowSize = windowSize
        
        for i in range(length):
            self.x += Snake.SIZE
      
            body =  Snake(RED,self.x,self.y)
            
            self.group.add(body)
            self.queue.append(body)
    def move(self, pressed=None):
        self.changeDir(pressed)
        
        if self.dir == 0:
            self.x += Snake.SIZE
            head = Snake(RED, self.x, self.y)
        elif self.dir == 1:
            self.y += Snake.SIZE
            head = Snake(RED, self.x, self.y)
        elif self.dir == 2:
            self.x -= Snake.SIZE
            head = Snake(RED, self.x, self.y)
        else:
            self.y -= Snake.SIZE
            head = Snake(RED, self.x, self.y)
            
            
            
        self.group.add(head)
        self.queue.append(head)
        
        if self.eatFood > 0:
           self.eatFood -= 1
        else:   
            tail = self.queue.pop(0)        
            self.group.remove(tail)
            
    def isOutOfRange(self) -> bool:
        if self.x < 0 or  self.x > self.windowSize[0] or \
        self.y < 0 or self.y > self.windowSize[1]:
            return True
        
        
        
        return False 
            

    def changeDir(self, pressed):
        if  not pressed: return
        if pressed[pygame.K_UP]:
            self.dir = 3
        
        elif pressed[pygame.K_LEFT]:
            self.dir = 2
        elif pressed[pygame.K_RIGHT]:
            self.dir = 0
        elif pressed[pygame.K_DOWN]:
            self.dir = 1
    def Eating(self, foodGroup):
                    
        eatFood = pygame.sprite.groupcollide(self.group, foodGroup, False , True) 
        if eatFood:
            self.eatFood += len(list(eatFood.values())[0])
            
    def collideSelf(self):
        tmp = pygame.sprite.Group(self.queue[0:-1])
        hits = pygame.sprite.spritecollide(self.queue[-1], tmp, False)
        return bool(hits)
        
class Food(pygame.sprite.Sprite):
    SIZE = 20
    def __init__(self, color ,x,y):
        super().__init__()
        self.image = pygame.Surface([self.SIZE,self.SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
                  
            
            
            
            
            
            