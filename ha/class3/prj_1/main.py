from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
from time import sleep

f = 1000
d = 0
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
p2 = Pin(2, Pin.OUT)
while True:
    p2.value(0)
    lcd.putstr("oh")
    sleep(2)
    lcd.clear()
    p2.value(1)
    lcd.putstr("oof")
    sleep(2)
    lcd.clear()
