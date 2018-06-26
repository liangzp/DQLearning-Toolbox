# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:21:27 2018

@author: Administrator
"""
import numpy as np
from MyLibrary import *

FPS=120
screenwidth=288
screenheight=512
fontsize=30
player_filename="players.png"
player_frame_width=48
player_frame_height=48
player_frame_num=4
base_filename="base.png"
base_frame_width=80
base_frame_height=15
base_frame_num=1
base_velocity_y=np.arange(-3,-8,-0.5)
stage=0
level=0
maxlevel=len(base_velocity_y)-1
timer_tick=30
interval=90
player_velocity_y=6
final_color=0,0,0
game_over=False
player_moving=False
FPSclock=pygame.time.Clock()

#创建玩家、平板的精灵组
player_group=pygame.sprite.Group()
base_group=pygame.sprite.Group()


#在屏幕下方随机位置生成板
def getRandomBase(filename,framewidth,frameheight,frameamount,velocity_y=-3,distance=100):
    base=MySprite()
    base.load(filename,framewidth,frameheight,frameamount)
    base.position=random.randint(0,screenwidth-base.frame_width),distance+screenheight
    base.velocity.y=velocity_y
    base_group.add(base)

#当有板超出屏幕上方时，改变其Y坐标至屏幕下方
def chBase():
    global stage
    for base in base_group:
        if base.Y<-base.frame_height:
            stage+=1
            base.Y=screenheight+interval 
            base.X=random.randint(0,screenwidth-base.frame_width)

#计算游戏难度、板的速度
def calcLevel():
    global level
    old_level=level
    present_level=stage//20
    if present_level>=old_level and level<maxlevel:
        level+=1
        return base_velocity_y[level]

    
#计算玩家的速度
def calcVelocity(direction,vel=1.0):
    velocity=Point(0,0)
    if direction==0:#not move
        velocity.x=0
    elif direction==1:#to the left
        velocity.x=-vel
    elif direction==2:#to the right
        velocity.x=vel
    return velocity

#当玩家按左右键时更改帧的图像        
def frameChange():
    if player.direction==0:#不动
        player.first_frame=3
        player.last_frame=3
    elif player.direction==1:#向左
        player.first_frame=0
        player.last_frame=0
    elif player.direction==2:#向右
        player.first_frame=2
        player.last_frame=2
    if player.frame<player.first_frame:
        player.frame=player.first_frame

#获取每个像素的透明度矩阵
def getHitmasks(image):
    mask = []
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask

#如果碰撞，则返回True
def checkCrash(player,base,hitmasks):
    #碰到底部
    if player.Y + player.frame_height >= screenheight - 1:
        return True
    else:
        player_rect = pygame.Rect(player.X, player.Y, player.frame_width, player.frame_height)
        for base in base_group:
            base_rect = pygame.Rect(base.X, base.Y, base.frame_width, base.frame_height)
            player_hit_mask = hitmasks['player']
            base_hit_mask = hitmasks['base']
            #检测是否有像素碰撞
            collide = pixelCollision(player_rect, base_rect, player_hit_mask, base_hit_mask)
            if collide:
                return True          
    return False

#检测像素是否碰撞        
def pixelCollision(rect1, rect2, hitmask1, hitmask2):
    
    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y
                    
    for x in range(rect.width):
        for y in range(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
            
    return False

class Game():
    def __init__(self,screen0):
        global screen, timer, player, font,player_group,base_group
        pygame.init()
        player_group = pygame.sprite.Group()
        base_group = pygame.sprite.Group()
        screen = screen0
        timer = pygame.time.Clock()
        player = MySprite()
        player.load(player_filename, player_frame_width, player_frame_height, player_frame_num)
        player.position = screenwidth // 3, screenheight // 3
        player_group.add(player)
        self.reset_score = True  # 该标志用于确保score的重置在下一帧才进行

        for i in np.arange(0, 501, 100):
            getRandomBase(base_filename, base_frame_width, base_frame_height, base_frame_num, base_velocity_y[0], i)

    def frameStep(self,input_actions):

        if self.reset_score:
            self.score=0
            self.reset_score=False
        pygame.event.pump()
        reward=0.2
        self.score+=1
        terminal=False

        timer.tick(timer_tick)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if(input_actions[0]==1):
            player_moving = True
            player.direction = 1
        elif input_actions[2]==1:
            player_moving = True
            player.direction = 2
        else:
            player.direction = 0

        global  game_over,level
        if game_over:
            reward=-5
            level = 0
            terminal=True
            global screen
            self.__init__(screen)
            game_over=False

        else:
            if player.direction:
                player.velocity = calcVelocity(player.direction, 5)

            #改变帧图像
            frameChange()

            #更新图像
            player_group.update(ticks, 50)

            #检测碰撞，以确定速度
            player_moving = True

            for base in base_group:
                # player={}
                Hitmasks = {}
                Hitmasks['base'] = (getHitmasks(base.image))
                Hitmasks['player'] = (getHitmasks(player.image))
                iscrash = checkCrash(player, base,Hitmasks)
                if iscrash:
                    if player.Y + player.frame_height >= base.Y and player.Y < base.Y:
                        if player.Y + player.frame_height < base.Y + 15:
                            player.Y = base.Y - player.frame_height + 2
                            player.velocity.y = base.velocity.y
                        elif player.X + player.frame_width >= base.X and player.X < base.X:
                            player.X = base.X - player.frame_width
                            player.velocity.y = player_velocity_y
                        elif player.X <= base.X + base.frame_width and base.X < player.X:
                            player.X = base.X + base.frame_width
                            player.velocity.y = player_velocity_y
                        break
                else:
                    player.velocity.y = player_velocity_y

            if player_moving:
                player.X += player.velocity.x
                player.Y += player.velocity.y
                if player.X < 0:
                    player.X = 0
                elif player.X > screenwidth - player.frame_width:
                    player.X = screenwidth - player.frame_width
                if player.Y < 0 or player.Y > screenheight - player.frame_height:
                    game_over = True

            #移动板
            calcLevel()
            for base in base_group:
                base.velocity.y = base_velocity_y[level]
                base.Y += base.velocity.y

            #改变板的位置（如果碰到边界）
            chBase()

            screen.fill(final_color)

            base_group.draw(screen)
            player_group.draw(screen)

        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.update()
        FPSclock.tick(FPS)

        return image_data,reward,terminal,self.score