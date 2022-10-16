from machine import I2C, Pin, ADC, PWM
from esp8266_i2c_lcd import I2cLcd
from time import sleep
from mcu_def import gpio
import network

WlSSID = 'SingularClass0'
wlPWD = 'Singular#1234'
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)
wlan.scan()
wlan.connect(WlSSID, wlPWD)
while not (wlan.isconnected()):
    pass
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.putstr(f'{wlan.ifconfig()[0]}')
