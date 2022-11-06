import paho.mqtt.client as mqtt


def on_message(client, userdata, msg):
    print(f"my SUB topic:{msg.topic},msg:{msg.payload.decode('utf-8')}")


def on_connect(client, userdata, flags, rc):
    print("yesss" + str(rc))
    client.subscribe("Fake_Singular")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("singular", "1234")
client.connect("singularmakers.asuscomm.com", 1883, 60)
client.loop_forever()
