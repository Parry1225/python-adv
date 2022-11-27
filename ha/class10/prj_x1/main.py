from mcu_def import gpio, mcu_fun
from machine import Pin
import time
import dht

mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")
mcu.mqtt_subscribe(mq_id_input="Fake_Singular")
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
lcd = mcu.lcd_initial(scl_pin=5, sda_pin=4)

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    lcd.clear()
    lcd.putstr(f"H:{hum:02d}")
    lcd.move_to(0, 1)
    lcd.putstr(str(f"T:{temp:02d}{'\u00b0'}C"))
    print(f"Humidity:{hum:02d},Temperture:{temp:02d}{'\u00b0'}C")
    mcu.mqtt_put_msg(
        topic_input="Fake_Singular",
        msg=f"Humidity:{hum:02d},Temperture:{temp:02d}{'\u00b0'}C")
    time.sleep(1)