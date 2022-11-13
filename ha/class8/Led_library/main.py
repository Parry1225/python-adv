from umqtt.simple import MQTTClient
import time
from machine import I2C, Pin, ADC, PWM
from esp8266_i2c_lcd import I2cLcd
from time import sleep
from mcu_def import gpio, mcu_fun
import network

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")

lcd = wlan.lcd_initial(scl_pin=5, sda_pin=4)

adc = ADC(0)
RED, BLUE, GREEN = wlan.led_initial(r_gpio=gpio.D5,
                                    g_gpio=gpio.D6,
                                    b_gpio=gpio.D7)

wlan.mqtt_subscribe(mq_id_input='Fake_Singular')


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


wlan.mqtt_get_msg(on_massage=on_massage, topic_input="Fake_Singular")

while True:
    wlan.mqClient0.check_msg()
    wlan.mqClient0.ping()
    time.sleep(0.3)