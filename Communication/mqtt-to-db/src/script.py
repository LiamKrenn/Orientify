import paho.mqtt.client as mqtt
import os
from datetime import datetime
import random
import json

from calculation import calculate_angle, calculate_timestamps
from db.services import save_angle, save_raw


#   Testdata
DISTANCE = 0.3
T1 = datetime(2024, 12, 17, 10, 0, 0, 0)
T2 = datetime(2024, 12, 17, 10, 0, 0, 500)

random.seed(10)


class MQTTClient:
    def __init__(self, broker, port, topic, username, password):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.username = username
        self.password = password

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc, properties=None):
        print(f"Connected with result code {rc}")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode("utf-8")
        data = json.loads(message)

        #save_angle(calculate_angle(DISTANCE, T1, datetime(2024, 12, 17, 10, 0, 0, random.randint(70, 999))))
        #save_angle(random.randint(0, 360))
        #save_raw(message)
        t1, t2 = calculate_timestamps(data["mikrofon1Daten"], data["mikrofon2Daten"])
        print(calculate_angle(data["abstandMikrofone"], t1, t2))

    def start(self):
        self.client.username_pw_set(username=self.username, password=self.password)
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()


MQTT_BROKER = os.getenv("MQTT_BROKER", "172.31.180.211")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "orientify_data")
MQTT_USER = os.getenv("MQTT_USER", "admin")
MQTT_PWD = os.getenv("MQTT_PWD", "admin")


if __name__ == "__main__":
    client = MQTTClient(MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MQTT_USER, MQTT_PWD)
    client.start()
    