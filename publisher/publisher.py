import random
import paho.mqtt.client as mqtt
import time

broker="91.121.93.94"
port = 1883
topic = "python/mqtt"
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def publish(msg):
    result = client.publish(topic, msg)
    
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# Κύριο πρόγραμμα
if __name__ == '__main__':    

    client = mqtt.Client()
    client.connect(broker,port,60)
    client.on_connect = on_connect
    client.loop_start()
    
    while True:
        # sent message
        msg = f"temperature: {random.randint(20, 25)}"
        publish(msg)

        # sleep 3 seconds
        time.sleep(1)