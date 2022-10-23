from machine import I2C, Pin, ADC, PWM
from esp8266_i2c_lcd import I2cLcd
from time import sleep
from mcu_def import gpio

f = 1000
d = 0
adc = ADC(0)
RED = Pin(gpio.D5)
GREEN = Pin(gpio.D6)
BLUE = Pin(gpio.D7)

RED2 = PWM(RED, freq=f, duty=d)
GREEN2 = PWM(GREEN, freq=f, duty=d)
BLUE2 = PWM(BLUE, freq=f, duty=d)

while True:
    value = adc.read()
    print(f'value={value},{round(value*100/1024)}%')
    sleep(1)
    if int(value) > 400:
        RED2.duty(value - 200)
        BLUE2.duty(value - 200)
        GREEN2.duty(value - 200)
        sleep(0.003)
    else:
        RED2.duty(0)
        BLUE2.duty(0)
        GREEN2.duty(0)
