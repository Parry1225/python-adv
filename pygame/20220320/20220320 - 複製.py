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
background = pygame.image.load('pygame/20220313/snow.jpg')
width = background.get_width()
height = background.get_height()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("minecraft")
mp3_path = 'pygame/20220320/music.mp3'
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(600000)

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 35)
title = font.render('start', True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
speed_ = font.render('fast', False, (0, 0, 0))
tit_w2 = speed_.get_width()
tit_h2 = speed_.get_height()


act = False
speed = False
snow_lint = []
rain_lint = []

for i in range(100):
    x_site = random.randint(0, width)
    y_site = random.randint(-100, -1)
    x_shift = random.randint(-1, 1)
    randius = random.randint(4, 6)
    clock = pygame.time.Clock()
    snow_lint.append([x_site, y_site, x_shift, randius])
for inin in range(40):
    x_site2 = random.randint(0, width)
    y_site2 = (x_site2+1)
    x_site3 = (x_site2+1)
    y_site3 = (y_site2+1)
    x_shift2 = random.randint(-1, 1)
    randius2 = random.randint(4, 6)
    clock2 = pygame.time.Clock()
    rain_lint.append([x_site2, y_site2, x_site3, y_site3, x_shift2, randius2])

while True:
    if speed:
        tit_w2 = speed_.get_width()
        tit_h2 = speed_.get_height()
        speed_ = font.render('fast', True, (0, 0, 0))
        clock.tick(100)
    else:
        tit_w2 = speed_.get_width()
        tit_h2 = speed_.get_height()
        speed_ = font.render('slow', False, (0, 0, 0))
        clock.tick(20)

    randius
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0,    tit_w, tit_h):
                act = not(act)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 255, 255,    (tit_w2+255), (tit_h2+255)):
                speed = not(speed)

    if act:
        title = font.render('stop', True, (0, 0, 0))
        pygame.mixer.music.pause()
        for rain in rain_lint:
            pygame.draw.rect(screen, (0, 20, 255), [
                             rain[0], rain[1], rain[2], rain[3]], rain[5])

            # rain[0] += rain[4]
            rain[1] += 1
            # rain[2] += rain[4]
            rain[3] += 1
            if rain[0] > height or rain[1] > width:
                rain[1] = rain[0]+1
                rain[0] = random.randrange(0, width)
                rain[2] = rain[0]+1
                rain[3] = rain[0]+1

    else:
        pygame.mixer.music.unpause()
        title = font.render('start', True, (0, 0, 0))
        # pygame.draw.circle(screen, (255, 255, 255),
        #                   (x_site, y_site), randius)
        for snow in snow_lint:

            pygame.draw.circle(screen, (255, 255, 255),
                               (snow[0], snow[1]), snow[3])
            snow[0] += snow[2]
            snow[1] += snow[3]
            if snow[1] > height or snow[0] > width:
                snow[1] = random.randrange(-100, -1)
                snow[0] = random.randrange(0, width)

    screen.blit(title, (0, 0))
    screen.blit(speed_, (255, 255))
    pygame.display.update()
