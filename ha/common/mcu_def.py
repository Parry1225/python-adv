import network
from umqtt.simple import MQTTClient
from machine import I2C, Pin, PWM
from esp8266_i2c_lcd import I2cLcd


class mcu_fun:

    def _init_(self):
        self.ip = None
        self.mqClient0 = None

    def connect_ap(self, ssid, pwd):
        wlan = network.WLAN(network.STA_IF)
        ap = network.WLAN(network.AP_IF)
        ap.active(False)
        wlan.active(True)
        wlan.scan()
        wlan.connect(ssid, pwd)
        while not (wlan.isconnected()):
            pass
        print('haha :L', wlan.ifconfig())
        self.ip = wlan.ifconfig()[0]

    def led_initial(self, r_gpio, g_gpio, b_gpio, mode_pwm: bool = False):
        if mode_pwm == False:
            RED = Pin(r_gpio, Pin.OUT)
            GREEN = Pin(g_gpio, Pin.OUT)
            BLUE = Pin(b_gpio, Pin.OUT)
            RED2 = RED.value(0)
            RED2 = RED.value(0)
            RED2 = RED.value(0)
        else:
            f = 1000
            d = 0
            RED = PWM(Pin(r_gpio), freq=f, duty=d)
            GREEN = PWM(Pin(g_gpio), freq=f, duty=d)
            BLUE = PWM(Pin(b_gpio), freq=f, duty=d)
        return (RED, BLUE, GREEN)

    def lcd_initial(self, scl_pin, sda_pin):
        i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
        lcd = I2cLcd(i2c, 0x27, 2, 16)

        return lcd

    def mqtt_subscribe(self, mq_id_input: str):
        mq_sever = "singularmakers.asuscomm.com"
        mq_id = mq_id_input
        mq_user = "singular"
        mq_pass = "1234"
        self.mqClient0 = MQTTClient(mq_id,
                                    mq_sever,
                                    user=mq_user,
                                    password=mq_pass,
                                    keepalive=32768)
        try:
            self.mqClient0.connect()
        except Exception as e:
            print(e)
            exit()
        finally:
            print("OMG!!!")

    def mqtt_get_msg(self, on_massage, topic_input: str):
        self.mqClient0.set_callback(on_massage)
        self.mqClient0.subscribe(topic_input)


class gpio:
    D1 = 16
    D1 = 5
    D2 = 4
    D3 = 0
    D4 = 2
    D5 = 14
    D6 = 12
    D7 = 13
    D8 = 15
    SDD3 = 10
    SDD2 = 9
