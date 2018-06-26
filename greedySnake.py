# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 13:02:48 2018

@author: Administrator
"""
import pygame
import sys
import random
from pygame import *

# 以25为单位
pixel=25

# 蛇类
class Snake(object):
    def __init__(self,screen_x,screen_y):
        #定义常量
        self.direction=2
        self.body=[]
        self.screen_x=screen_x
        self.screen_y=screen_y

        #初始化蛇
        for x in range(4):
            self.addNode()



    # 在前端增加色块
    def addNode(self):
        #找到蛇的最前端
        if self.body:
            node = pygame.Rect(self.body[0].left,self.body[0].top,pixel,pixel)
        else:
            node = pygame.Rect(0,0,pixel,pixel)
        if self.direction==1:
            node.left-=pixel
        elif self.direction==2:
            node.left+=pixel
        elif self.direction==3:
            node.top-=pixel
        elif self.direction==4:
            node.top+=pixel
        self.body.insert(0,node)

    # 删除最后一个块
    def delNode(self):
        self.body.pop()

    # 死亡判断
    def isDead(self):
        # 撞墙
        if self.body[0].x not in range(self.screen_x):
            return True
        if self.body[0].y not in range(self.screen_y):
            return True
        # 咬到自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    # 更新位置
    def move(self):
        self.addNode()
        self.delNode()

    # 改变方向 但是左右、上下不能被逆向改变
    def changeDirection(self, curkey):
        if (curkey == 1 and self.direction == 2) or (curkey == 2 and self.direction == 1) or (
                curkey == 3 and self.direction == 4) or (curkey == 4 and self.direction == 3):
            return
        self.direction = curkey


# 食物类
class Food:
    def __init__(self,screen_x):
        self.body = pygame.Rect(-pixel, 0, pixel, pixel)
        self.screen_x=screen_x

    def reset(self):
        self.body.x = -pixel#隐藏食物
        allpos = [pos for pos in range(pixel, self.screen_x-pixel, pixel)]# 不靠墙太近 pixel ~ SCREEN_X-pixel 之间
        pos_illegal=True
        return random.choice(allpos),random.choice(allpos)


#贪吃蛇
class Game:
    def __init__(self,screen):

        #初始化对象
        self.screen=screen
        self.timer = pygame.time.Clock()

        #初始化常量
        self.screen_x=screen.get_size()[0]
        self.screen_y = screen.get_size()[1]
        self.FPS=60
        self.reset_score=True#该标志用于确保score的重置在下一帧才进行
        self.isdead_state = False
        self.game_over=True
        #实例化
        self.snake = Snake(screen.get_size()[0], screen.get_size()[1])
        self.food = Food(screen.get_size()[0])

        #初始化实例
        self.foodReset()

    def frameStep(self, input_actions):

        pygame.event.pump()
        reward = 0
        terminal = False

        if self.reset_score:
            self.score=0
            self.reset_score=False

        for event in pygame.event.get():
            if event.type == K_ESCAPE or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.game_over=True
                pygame.quit()
                return 0, 0, -1,self.score

        #转换动作状态(与目前相反方向的按键不能生效)
        if input_actions[0] == 1:
            self.snake.changeDirection(1)
        elif input_actions[1] == 1:
            self.snake.changeDirection(2)
        elif input_actions[2] == 1:
            self.snake.changeDirection(3)
        elif input_actions[3] == 1:
            self.snake.changeDirection(4)

        # 蛇移动
        if not self.snake.isDead():
            self.snake.move()
        else:
            self.__init__(self.screen)
            reward = -1
            terminal = True

        #判断是否吃到食物
        if self.food.body == self.snake.body[0]:
            reward = 0.5
            self.foodReset()
            self.snake.addNode()
            self.score+=1

        self.screen.fill((0, 0, 0))
        for rect in self.snake.body:
            pygame.draw.rect(self.screen, (20, 220, 39), rect, 0)
        pygame.draw.rect(self.screen, (136, 0, 21), self.food.body, 0)

        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.update()
        self.timer.tick(self.FPS)

        return image_data, reward, terminal,self.score

    def foodReset(self):
        food_illegal=True
        while food_illegal:
            x,y=self.food.reset()
            if not (x,y) in [(body.x,body.y) for body in self.snake.body]:
                food_illegal=False
                self.food.body.x,self.food.body.y=x,y






