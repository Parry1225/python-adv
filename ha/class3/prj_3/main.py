from machine import Pin, PWM
from time import sleep
from mcu_def import gpio
import random

RED = Pin(gpio.D5)
GREEN = Pin(gpio.D6)
BLUE = Pin(gpio.D7)
f = 1000
d = 0
RED2 = PWM(RED, freq=f, duty=d)
GREEN2 = PWM(GREEN, freq=f, duty=d)
BLUE2 = PWM(BLUE, freq=f, duty=d)
while True:
    for i in range(512, 1024):
        RED2.duty(i)
        sleep(0.003)
    for i in range(1024, 512, -1):
        RED2.duty(i)
        sleep(0.003)
    for i in range(512, 1024):
        GREEN2.duty(i)
        sleep(0.003)
    for i in range(512, 1024, -1):
        GREEN2.duty(i)
        sleep(0.003)
    for i in range(1024, 512):
        BLUE2.duty(i)
        GREEN2.duty(i)
        sleep(0.003)
    for i in range(1024, 512, -1):
        BLUE2.duty(i)
        GREEN2.duty(i)
        sleep(0.003)