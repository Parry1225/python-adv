from machine import I2C, Pin
from common.esp8266_i2c_lcd import I2cLcd

f = 1000
d = 0
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.putstr("u suck ")
lcd.move_to(0, 1)
lcd.putstr("LOL")
