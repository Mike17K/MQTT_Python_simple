from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt

broker = '91.121.93.94'
port = 1883
topic = "python/mqtt"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

client = mqtt.Client()
client.connect(broker,port,60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()