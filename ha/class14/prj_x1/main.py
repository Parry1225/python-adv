from time import sleep
from machine import Pin
from mcu_def import gpio, mcu_fun
from time import sleep

mcu = mcu_fun()
earthquake = Pin(gpio.SDD3, Pin.IN)
mcu.mp3_initial()
while True:
    print(earthquake.value())
    if earthquake.value() == 1:
        print('OH!!')
        mcu.mp3_start()
        sleep(3)
        mcu.mp3_stop()
