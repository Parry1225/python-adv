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


typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 35)
title = font.render('start', True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()

act = False
x_site = random.randint(0, width)
y_site = random.randint(-10, -1)
x_shift = random.randint(-1, -1)
randius = random.randint(4, 6)
clock = pygame.time.Clock()

while True:
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
    if act:
        title = font.render('stop', True, (0, 0, 0))

    else:
        title = font.render('start', True, (0, 0, 0))
        pygame.draw.circle(screen, (255, 255, 255),
                           (x_site, y_site), randius)
        x_site += x_shift
        y_site += randius
        if y_site > height or x_site > width:
            y_site = random.randrange(-10, -1)
            x_site = random.randrange(0, width)

    screen.blit(title, (0, 0))
    pygame.display.update()
