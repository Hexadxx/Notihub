import paho.mqtt.client as mqtt
from django.conf import settings
from .models import Measure

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('sensor/CO2eq')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    print(f'Received data from sensor on topic: {msg.topic} with payload: {str(msg.payload)}')
    measure_instance = Measure.objects.create(value={str(msg.payload)},measurement_date='2001-12-25',sensor_id=1)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
