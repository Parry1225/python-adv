from time import sleep
from machine import Pin
from mcu_def import gpio, mcu_fun
from time import sleep

IR = Pin(gpio.D3, Pin.IN)
while True:
    print(IR.value())