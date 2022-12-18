from machine import Pin
from mcu_def import gpio
from time import sleep

earthquake = Pin(gpio.SDD3, Pin.IN)
while True:
    print(earthquake.value())
    if earthquake.value() == 1:
        print('OH!!')
    sleep(1)
