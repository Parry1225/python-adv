from http import client
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.username_pw_set('singular', '1234')
client.connect('singularmakers.asuscomm.com', 1883, 60)
while True:
    msg = input()
    client.publish("Fake_Singular", msg)
    time.sleep(1)
