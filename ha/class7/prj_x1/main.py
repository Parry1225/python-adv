from mcu_def import mcu_fun
from umqtt.simple import MQTTClient
import time
from mcu_def import mcu_fun

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")
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


mqClient0.set_callback(on_massage)
mqClient0.subscribe("Fake_Singular")
while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(1)
