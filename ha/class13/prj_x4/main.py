from machine import UART
from time import sleep

uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1)
buf1 = bytearray(5)
buf1[0] = 0xAA  #聲音
buf1[1] = 0x13  #聲音
buf1[2] = 0x01  #聲音
buf1[3] = 0x7e  #聲音
buf1[4] = buf1[0] + buf1[1] + buf1[2] + buf1[3]
uart.write(buf1)

buf = bytearray(6)
buf[0] = 0xAA  #聲音
buf[1] = 0x07  #聲音
buf[2] = 0x02  #聲音
buf[3] = 0x00  #檔名
buf[4] = 0x01  #檔名
buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
uart.write(buf)
sleep(3)

buf2 = bytearray(4)  #stop
buf2[0] = 0xAA  #聲音
buf2[1] = 0x04  #聲音
buf2[2] = 0x00  #聲音
buf2[3] = 0xAE  #聲音
uart.write(buf2)