import time
from pygame.locals import *
from hashlib import new
from json import load
from re import M
from tkinter import font
from turtle import back, st, width
from numpy import angle
import pygame
import sys
import math
import random
import os

os.chdir(sys.path[0])


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
# background = pygame.image.load('pygame/20220313/snow.jpg')
# width = background.get_width()
# height = background.get_height()
background = pygame.image.load('Gophers_BG_800x600.png')
width = background.get_width()
height = background.get_height()
Blue = (0, 0, 255)
BLack = (0, 0, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('打地鼠')
sur = pygame.Surface([width, height])

gophers = pygame.image.load('Gophers150.png')
gophers2 = pygame.image.load('Gophers2_150.png')
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]
tick = 0
max_tick = 20
pos = pos6[0]
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
clock = pygame.time.Clock()
times = 0
time_max = 20
end_font = pygame.font.Font(typeface, 36)
end_sur = end_font.render(str(times), True, [255, 0, 0])
mpos = (0, 0)
pygame.mouse.set_visible(False)
ham1 = pygame.image.load('Hammer1.png')
ham2 = pygame.image.load('Hammer2.png')
hitsur = gophers
pygame.mixer.music.load('hit.mp3')

while True:
    hitsur = gophers
    clock.tick(30)
    hammer = ham2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):

                if times < time_max:
                    tick = max_tick + 100000
                    score += 1
                    hitsur = gophers2

        elif event.type == MOUSEMOTION:
            mpos = pygame.mouse.get_pos()
    if times > time_max:
        sur.fill((0, 0, 0))
        pygame.mouse.set_visible(True)
        end_sur = score_font.render(
            "Your Score is : {}/{}".format(score, time_max), False, RED)
        screen.blit(sur, (0, 0))
        screen.blit(end_sur, (100, 100))
        pygame.display.flip()
    else:
        if tick > max_tick:
            times = times + 1
            screen.blit(background, (0, 0))
            score_sur = score_font.render(str(score), True, [255, 0, 0])
            end_sur = score_font.render(str(score), True, [255, 0, 0])
            new_pos = random.randint(0, 5)
            pos = pos6[new_pos]
            tick = 0
        else:
            tick += 1
        sur.blit(background, (0, 0))

        sur.blit(hitsur, (pos[0] - hitsur.get_width() / 2,
                          pos[1] - hitsur.get_height() / 2))
        sur.blit(hammer, (mpos[0] - hammer.get_width() / 2,
                          mpos[1] - hammer.get_height() / 2))

        # pygame.draw.circle(sur, [0, 255, 0], mpos, 10)
        screen.blit(sur, (0, 0))
        sorce_sur = score_font.render(str(score), False, RED)
        screen.blit(sorce_sur, (10, 10))
        pygame.display.update()
        if hammer == ham1 or hitsur == gophers2:
            time.sleep(0.1)
