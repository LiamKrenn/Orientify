import asyncio
from websockets.asyncio.client import connect
import paho.mqtt.client as mqtt
import os

from calculation import calculate_angle


class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.connection = None

    async def connect(self):
        async with connect(self.uri) as self.connection:
            print('Connected to websocket server.')

    async def send_message(self, message):
        async with connect(self.uri) as websocket:
            await websocket.send(message)


class MQTTConsumer:
    def __init__(self, broker, port, topic, websocket_client: WebSocketClient, username, password):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.username = username
        self.password = password
        self.websocket_client = websocket_client
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT broker with result code {rc}")
        client.subscribe(self.topic)
        print(f"Subscribed to topic: {self.topic}")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode("utf-8")
        print(f"Received MQTT message: {message}")

        asyncio.run(self.websocket_client.send_message(calculate_angle(message)))


    def start(self):
        self.client.username_pw_set(username=self.username, password=self.password)
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()


MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "orientify_data")
MQTT_USER = os.getenv("MQTT_USER", "admin")
MQTT_PWD = os.getenv("MQTT_PWD", "admin")
WEBSOCKET_URI = os.getenv("WEBSOCKET_URI", "ws://localhost:8765")

websocket_client = WebSocketClient(WEBSOCKET_URI)
print(MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, websocket_client, MQTT_USER, MQTT_PWD)
mqtt_consumer = MQTTConsumer(MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, websocket_client, MQTT_USER, MQTT_PWD)
mqtt_consumer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")