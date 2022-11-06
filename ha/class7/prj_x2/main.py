from umqtt.simple import MQTTClient
import time
from machine import I2C, Pin, ADC, PWM
from esp8266_i2c_lcd import I2cLcd
from time import sleep
from mcu_def import gpio, mcu_fun
import network

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
f = 1000
d = 0
adc = ADC(0)
RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)
mq_sever = "singularmakers.asuscomm.com"
mq_id = "Fake_Singular"
mq_user = "singular"
mq_pass = "1234"
mqClient0 = MQTTClient(mq_id,
                       mq_sever,
                       user=mq_user,
                       password=mq_pass,
                       keepalive=32768)
try:
    mqClient0.connect()
except Exception as e:
    print(e)
    exit()
finally:
    print("OMG!!!")


def on_massage(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my SUB topic: {topic},msg:{msg}")
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(msg)
    lcd.move_to(0, 1)
    lcd.putstr(topic)
    if msg == "ON":
        GREEN.value(1)
        RED.value(1)
        BLUE.value(1)
    elif msg == "OFF":
        GREEN.value(0)
        RED.value(0)
        BLUE.value(0)


mqClient0.set_callback(on_massage)
mqClient0.subscribe("Fake_Singular")
while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(0.3)