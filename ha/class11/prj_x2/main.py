import json
from mcu_def import gpio, mcu_fun
from machine import Pin, ADC
import time
import dht

mcu = mcu_fun()
RED, BLUE, GREEN = mcu.led_initial(r_gpio=gpio.D5,
                                   g_gpio=gpio.D6,
                                   b_gpio=gpio.D7)


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


mcu.connect_ap("SingularClass0", "Singular#1234")
mcu.mqtt_subscribe(mq_id_input="Fake_Singular", on_massage=on_massage)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
lcd = mcu.lcd_initial(scl_pin=5, sda_pin=4)
msg_json = {}
adc = ADC(0)

while True:
    mcu.mqtt_get_msg(topic_input="Fake_Singular")
    mcu.mqClient0.ping()
    vipx2 = adc.read()
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    lcd.clear()
    lcd.putstr(f"H:{hum:02d}")
    lcd.move_to(0, 1)
    lcd.putstr(f"T:{temp:02d}{'\u00b0'}C")
    msg_json["Humidity"] = hum
    msg_json["Temperture"] = temp
    msg_json["light_sansor"] = vipx2
    mcu.mqtt_put_msg(topic_input="Fake_Singular", msg=json.dumps(msg_json))
    time.sleep(1)
