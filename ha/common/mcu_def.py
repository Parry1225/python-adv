import network
from umqtt.simple import MQTTClient
from machine import I2C, Pin, PWM, UART
from esp8266_i2c_lcd import I2cLcd


class mcu_fun:

    def _init_(self):
        self.ip = None
        self.mqClient0 = None
        self.uart = None

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
            RED.value(0)
            GREEN.value(0)
            BLUE.value(0)
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

    def mqtt_subscribe(self, mq_id_input: str, on_massage=None):
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
        self.mqClient0.set_callback(on_massage)

    def mqtt_get_msg(self, topic_input: str):
        self.mqClient0.subscribe(topic_input)
        self.mqClient0.check_msg()
        self.mqClient0.ping()

    def mqtt_put_msg(self, topic_input: str, msg: str):
        topic_input = topic_input.encode('utf-8')
        msg = msg.encode('utf-8')
        self.mqClient0.publish(topic_input, msg)

    def servo_angle(self, sg, angle):
        if 0 <= angle <= 180:
            sg.duty(int(1023 * (0.5 + angle / 90) / 20))

    def mp3_initial(self):
        self.uart = UART(1, baudrate=9600)
        self.uart.init(9600, bits=8, parity=None, stop=1)

    def mp3_start(self, volume: int = 100, song: int = 1):

        # volume = 0-127
        # song= 1-16
        buf1 = bytearray(5)
        buf1[0] = 0xAA  #聲音
        buf1[1] = 0x13  #聲音
        buf1[2] = 0x01  #聲音
        buf1[3] = volume  #聲音
        buf1[4] = buf1[0] + buf1[1] + buf1[2] + buf1[3]
        self.uart.write(buf1)
        # self.sleep(3)
        buf = bytearray(6)
        buf[0] = 0xAA  #聲音
        buf[1] = 0x07  #聲音
        buf[2] = 0x02  #聲音
        buf[3] = 0x00  #檔名
        buf[4] = song  #檔名
        buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
        self.uart.write(buf)

    def mp3_stop(self):
        buf2 = bytearray(4)  #stop
        buf2[0] = 0xAA  #聲音
        buf2[1] = 0x04  #聲音
        buf2[2] = 0x00  #聲音
        buf2[3] = 0xAE  #聲音
        self.uart.write(buf2)


class gpio:
    D0 = 16
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
