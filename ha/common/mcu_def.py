import network


class mcu_fun:

    def _init_(self):
        self.ip = None

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
