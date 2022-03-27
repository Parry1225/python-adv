from hashlib import new
from json import load
from re import M
from tkinter import font
from turtle import back, width
from numpy import angle
import pygame
import sys
import math
import random


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
background = pygame.image.load('pygame/20220327/Gophers_BG_800x600.png')
width = background.get_width()
height = background.get_height()
Blue = (0, 0, 255)
BLack = (0, 0, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('打地鼠')
sur = pygame.Surface([width, height])
gophers = pygame.image.load('pygame/20220327/Gophers150.png')
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]
tick = 0
max_tick = 20
pos = pos6[0]
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0]+50, pos[1]+50):
                tick = max_tick+100000
                score += 1

    if tick > max_tick:
        screen.blit(background, (0, 0))
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
    else:
        tick += 1
    sur.blit(background, (0, 0))
    sur.blit(gophers, (pos[0] - gophers.get_width() /
             2, pos[1] - gophers.get_height()/2))

    screen.blit(sur, (0, 0))
    sorce_sur = score_font.render(str(score), False, RED)
    screen.blit(sorce_sur, (10, 10))
    pygame.display.update()
