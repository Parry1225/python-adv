from turtle import back, width
from numpy import angle
import pygame
import sys
import math
act = False
pygame.init()
width = 640
height = 320

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("minecraft")

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            act = not(act)
    if act:
        pygame.draw.circle(background, (0, 255, 255), (320, 160), 150, 0)
        pygame.draw.circle(background, (230, 0, 255), (230, 130), 40, 0)
        pygame.draw.circle(background, (230, 0, 255), (389, 130), 40, 0)
        pygame.draw.rect(background, (0, 20, 255), [130, 240, 240, 130], 0)
        pygame.draw.ellipse(background, (0, 20, 255), [260, 130, 60, 400], 5)
        pygame.draw.polygon(background, (50, 20, 255), [
            [200, 100], [130, 60], [0, 200], [100, 76], [78, 51]], 5)
        pygame.draw.arc(background, (20, 40, 255), [
            240, 60, 60, 240], math.radians(40), math.radians(140), 5)
        pygame.draw.arc(background, (20, 40, 255), [
            240, 60, 60, 240], math.radians(90), math.radians(203), 5)
    else:
        background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    pygame.display.update()
