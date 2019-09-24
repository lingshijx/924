# -*- coding:utf-8 -*-
import pygame
import sys
import time
import random
from pygame.locals import *

class my_craft(object):
    def __init__(self,screen,enemycraft):
        self.x = 190
        self.y = 600
        self.screen = screen
        self.who = 'hero'
        self.blood = 100
        self.enemy = enemycraft
        self.range = (self.x,self.x+100,self.y)
        self.imageName = 'venv/bin/feiji/hero.gif'
        self.my_craft = pygame.image.load(self.imageName).convert()
        self.bulletlist = []

    def display(self):
        self.screen.blit(self.my_craft, (self.x, self.y))

        for bullet in self.bulletlist:
            bullet.display()



            if bullet.x >= bullet.enemyrange[0] and bullet.x <= bullet.enemyrange[1] and bullet.y == bullet.enemyrange[2]:
                bullet.hit()
                print('打中了')
                self.bulletlist.remove(bullet)
            bullet.y -= 10
            if bullet.y < 0:#出界删除
                self.bulletlist.remove(bullet)
                continue

        #print('{}颗子弹'.format(len(self.bulletlist  )))
    def left(self):
        if self.x > 0:
            self.x -= 15
    def right(self):
        if self.x < 375:
            self.x += 15
    def up(self):
        if self.y > 0:
            self.y -= 15
    def down(self):
        if self.y < 650:
            self.y += 15

    def shotAbullet(self):
        newbullet = bullet(self,self.enemy)
        self.bulletlist.append(newbullet)

    def done(self):
        print('英雄死了')


class enemy_craft(object):
    def __init__(self,screen):
        self.x = 190
        self.y = 0
        self.screen = screen
        self.destination = 1
        self.who = 'enemy-3'
        self.blood = 1000
        self.range = (self.x, self.x + 165,self.y+246)
        self.imageName = 'venv/bin/feiji/enemy-3.gif'
        self.my_craft = pygame.image.load(self.imageName).convert()
        self.bulletlist = []

    def display(self):
        self.screen.blit(self.my_craft, (self.x, self.y))

        if self.x < 0:
            self.destination = 1
        if self.x > 320:
            self.destination = 0
        if self.destination == 1:
            self.right()
        else:
            self.left()

        #发射子弹
        # a = random.randint(1,100)
        # if a > 80:
        #     self.shotAbullet()
        # for bullet in self.bulletlist:
        #     bullet.display()
        #     bullet.y +=20
        #     if bullet.y > 800:#出界删除
        #         self.bulletlist.remove(bullet)



    def left(self):
        self.x -= 15
    def right(self):
        self.x += 15

    def shotAbullet(self):
        newbullet = bullet(self,object)
        self.bulletlist.append(newbullet)


    def done(self):
        print('敌机死了')

class bullet(object):
    def __init__(self,mycraft,enemycraft):
        self.x = mycraft.x
        self.y = mycraft.y
        self.screen = mycraft.screen
        self.who = mycraft.who
        self.enemy = enemycraft
        self.enemyrange = self.enemy.range
        self.enemyblood = self.enemy.blood

        if self.who == 'hero':
            self.attack = 100
        elif self.who == 'enemy-3':
            self.attack = 10


        self.image1 = pygame.image.load('venv/bin/feiji/bullet-1.gif').convert()
        self.image2 = pygame.image.load('venv/bin/feiji/bullet-2.gif').convert()

    def display(self):
        if self.who == 'hero':
            self.screen.blit(self.image1, (self.x + 40, self.y - 20))
        elif self.who == 'enemy-3':
            self.screen.blit(self.image2, (self.x + 82, self.y + 246))
        print(self.enemyrange,self.enemyblood)
    def hit(self):
        self.enemyblood -= self.attack
        if self.enemyblood <= 0:
            self.enemy.done()






bg_image = 'venv/bin/feiji/background.png'#背景图片

pygame.init()

screen = pygame.display.set_mode((480,852),0,32)

background = pygame.image.load(bg_image).convert()
#
enemy_craft1 = enemy_craft(screen)
my_craft1 = my_craft(screen,enemy_craft1)#创建飞机对象


while True:  # 死循环确保窗口一直显示
    screen.blit(background, (0, 0))
    my_craft1.display()
    enemy_craft1.display()


    for event in pygame.event.get():  # 遍历所有事件

        if event.type == QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                my_craft1.left()

            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                my_craft1.right()

            elif event.key == K_w or event.key == K_UP:
                print('up')
                my_craft1.up()

            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                my_craft1.down()

            elif event.key == K_SPACE:
                print('space')
                my_craft1.shotAbullet()
    time.sleep(0.01)






    pygame.display.update()















pygame.quit()  # 退出pygame