#===載入套件開始===
#***載入套件結束***
from re import T
from socket import gaierror
from turtle import Screen
from matplotlib.pyplot import sca
from numpy import block
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import *
import random
#===初始化設定開始===
'''顏色'''
BLOCK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
rainbow1 = random.randint(100, 250)
rainbow2 = random.randint(100, 250)
rainbow3 = random.randint(100, 250)
'''初始化'''

game_mode = 1


def resetGame():
    global brick_num, bricks_list, dx, dy, act, rrainbow1, rrainbow2, rrainbow3, bricks, ball_color
    act = False
    for bricks in bricks_list:
        rrainbow1 = (random.randint(100, 250))
        rrainbow2 = (random.randint(100, 250))
        rrainbow3 = (random.randint(100, 245))
        rrainbow = (rainbow1, rainbow2, rainbow3)
        ball_color = rrainbow
        bricks[4] = True
    brick_num = TOTAL_BLOCK
    dx = 8
    dy = -8


'''FPS'''
pygame.init()
clock = pygame.time.Clock()
'''
遊戲狀態
# False:等待開球
# True:遊戲進行中
'''
act = False
livn = 2
#***初始化設定結束***
bg_x = 800
bg_y = 600
bg_size = (bg_x, bg_y)
pygame.display.set_caption(u"LOL")
Screen = pygame.display.set_mode(bg_size)

#===遊戲視窗設定開始===
#***遊戲視窗設定結束***

#===磚塊設定開始===
TOTAL_BLOCK = 60
bricks_list = []
brick_num = 0
brick_x = 70
brick_y = 60
brick_w = 0
brick_h = 0
brick_v = True
rainbow = (rainbow1, rainbow2, rainbow3)

for i in range(0, TOTAL_BLOCK):
    if ((i % 10) == 0):
        brick_w = 0
        brick_h += 18

    rainbow = (rainbow1, rainbow2, rainbow3)
    rainbow1 = random.randint(1, 250)
    rainbow2 = random.randint(1, 250)
    rainbow3 = random.randint(1, 245)
    bricks_list.append(
        [brick_w + brick_x, brick_h + brick_y, 50, 10, brick_v, rainbow])

    brick_w += 70


def bricks_update(win):
    global brick_num, dy
    for bricks in bricks_list:
        if (is_hit(ball_x, ball_y,
                   [bricks[0], bricks[1], bricks[2], bricks[3]])):
            if (bricks[4]):
                brick_num -= 1
                if (brick_num <= 0):
                    resetGame()
                    break
                dy = -dy
            bricks[4] = False

    for bricks in bricks_list:
        if (bricks[4] == True):
            block_rect = [bricks[0], bricks[1], bricks[2], bricks[3]]
            pygame.draw.rect(win, bricks[5], block_rect)


#===磚塊設定結束===

#===顯示磚塊數量設定開始===
typeface = pygame.font.get_default_font()
number_font = pygame.font.Font(typeface, 36)


def get_blick_num(win):
    global brick_num
    sur = number_font.render(str(brick_num), True, RED)
    win.blit(sur, [10, 10])


def get_livn(win):
    global livn
    sur = number_font.render(str(livn), True, RED)
    win.blit(sur, [10, 200])


#===顯示磚塊數量設定結束===


#===碰撞設定開始===
def is_hit(x, y, boxRect):
    xmatch = x >= boxRect[0] and x <= boxRect[0] + boxRect[2]
    ymatch = y >= boxRect[1] and y <= boxRect[1] + boxRect[3]
    if (xmatch and ymatch):
        return True
    return False


#===碰撞設結束===

#===初始遊戲設定開始===
#===初始遊戲設定結束===

#===底板設定開始===
paddle_x = 0
paddle_y = (bg_y - 24)


def paddle_update(win):
    global dx, dy
    paddly_rect = [paddle_x, paddle_y, 100, 10]
    pygame.draw.rect(win, RED, paddly_rect)
    if (is_hit(ball_x, ball_y, paddly_rect)):
        dy = -dy


#===底板設定結束===

#===球設定開始===
ball_x = 400
ball_y = 300
ball_radius = 8
ball_diameter = ball_radius * 2

rrainbow1 = (random.randint(100, 250))
rrainbow2 = (random.randint(100, 250))
rrainbow3 = (random.randint(100, 245))
rrainbow = (rainbow1, rainbow2, rainbow3)
ball_color = rrainbow
dx = 8
dy = -8


def ball_update(win):
    global ball_x, ball_y, rrainbow, rrainbow1, rrainbow2, rrainbow3, livn, game_mode
    global dx, dy, act
    if (act == False):
        ball_x = paddle_x + 55
        ball_y = paddle_y - ball_radius
    else:
        ball_x += dx
        ball_y += dy
        if (ball_y > bg_y - ball_diameter):
            livn -= 1
            act = False
            if (livn < 0):
                game_mode = 0
        if (ball_x > bg_x - ball_diameter or ball_x < ball_diameter):
            dx = -dx
        if (ball_y > bg_y - ball_diameter or ball_y < ball_diameter):
            dy = -dy
        pygame.draw.circle(win, ball_color, [ball_x, ball_y], ball_radius)


#===球設定結束===

#===初始遊戲設定開始===
img_gg = pygame.image.load('gameover.png')
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()


def game_over(win):
    global livn
    win.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


#===初始遊戲設定結束===
resetGame()
#-------------------------------------------------------------------------
# 主迴圈.

#-------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            paddle_x = pygame.mouse.get_pos()[0] - 55
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (act == False):
                act = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                resetGame()
                game_mode = 1
                livn = 3
    if (game_mode):
        Screen.fill(BLOCK)
        bricks_update(Screen)
        get_blick_num(Screen)
        ball_update(Screen)
        paddle_update(Screen)
        get_livn(Screen)

    else:
        game_over(Screen)

    pygame.display.update()
    clock.tick(60)