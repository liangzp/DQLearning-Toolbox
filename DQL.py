# -*- coding: utf-8 -*-

import cv2
from DQLBrain import Brain
import numpy as np
from collections import deque
import sqlite3
import pygame
import time
import game_setting
import importlib

SCREEN_X = 288
SCREEN_Y = 512
FPS = 60

class AI:
    def __init__(self, title,model_path,replay_memory,current_timestep,explore,initial_epsilon,final_epsilon,gamma,replay_size,batch_size):
        #初始化常量
        self.scores = deque()
        self.games_info = game_setting.getSetting()

        #连接临时数据库（并确保已经存在对应的表）
        self.data_base = sqlite3.connect('temp.db', check_same_thread=False)
        self.c = self.data_base.cursor()
        try:
            self.c.execute('create table scores (time integer, score integer) ')
        except:
            pass

        #创建Deep-Reinforcement Learning对象
        self.brain = Brain(self.games_info[title]["action"],model_path,replay_memory,current_timestep,explore,initial_epsilon,final_epsilon,gamma,replay_size,batch_size)

        #创建游戏窗口
        self.startGame(title,SCREEN_X,SCREEN_Y)

        #加载对应的游戏
        game=importlib.import_module(self.games_info[title]['class'])
        self.game=game.Game(self.screen)

    def startGame(self,title,SCREEN_X, SCREEN_Y):
        #窗口的初始化
        pygame.init()
        screen_size = (SCREEN_X, SCREEN_Y)
        pygame.display.set_caption(title)

        #屏幕的创建
        self.screen = pygame.display.set_mode(screen_size)

        #游戏计时器的创建
        self.clock = pygame.time.Clock()

    #为降低画面复杂度，将画面进行预处理
    def preProcess(self, observation):

        #将512*288的画面裁剪为80*80并将RGB(三通道)画面转换成灰度图(一通道)
        observation = cv2.cvtColor(cv2.resize(observation, (80, 80)), cv2.COLOR_BGR2GRAY)

        #将非黑色的像素都变成白色
        threshold,observation = cv2.threshold(observation, 1, 255, cv2.THRESH_BINARY)

        #返回(80,80,1)，最后一维是保证图像是一个tensor(张量),用于输入tensorflow
        return np.reshape(observation, (80, 80, 1))

    def playGame(self):
        #先随便给一个决策输入，启动游戏
        observation0, reward0, terminal,score =self.game.frameStep(np.array([1, 0, 0]))
        observation0 = self.preProcess(observation0)
        self.brain.setInitState(observation0[:,:,0])

        #开始正式游戏
        i = 1
        while True:
            i = i + 1
            action = self.brain.getAction()
            next_bservation, reward, terminal,score = self.game.frameStep(action)

            #处理游戏界面销毁消息
            if (terminal == -1):
                self.closeGame()
                return
            else:

            #继续游戏
                next_bservation = self.preProcess(next_bservation)
                self.brain.setPerception(next_bservation, action, reward, terminal)

            #提取每一局的成绩
            if terminal:
                t = int(time.time())
                self.c.execute("insert into scores values (%s,%s)" % (t, score))

    def closeGame(self):
        pygame.quit()
        self.brain.close()
        self.data_base.close()

    def getState(self):
        return self.brain.getState()


    def getReplay(self):
        return self.brain.replayMemory

