import paho.mqtt.client as mqtt
from django.conf import settings
from .models import Measure
import datetime
#import json

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('sensor/CO2eq')
        mqtt_client.subscribe('sensor/sound')
    else:
        print('Bad connection. Code:', rc)


#When a message arrives
def on_message(mqtt_client, userdata, msg):
    print(f'Received data from sensor on topic: {msg.topic} with payload: {msg.payload}')
    print(msg.topic+" message payload is {}".format(msg.payload.decode("utf-8")))
    
    #console.log("Message arrived: topic=" + msg.destinationName + ", message=" + msg.payloadString);

    strValue = msg.payload.decode("utf-8")

    if msg.topic == "sensor/CO2eq":
        #measure_instance = Measure.objects.create(value=(.format(msg.payload.decode("utf-8"))),sensor_id=1)
        measure_instance = Measure.objects.create(value=strValue.format(msg.payload.decode("utf-8")),sensor_id=1)
    if msg.topic == "sensor/sound": 
        measure_instance = Measure.objects.create(value=strValue.format(msg.payload.decode("utf-8")),sensor_id=2)
  
  

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
