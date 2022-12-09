from django.apps import AppConfig


class SensordataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sensordata'

    def ready(self):
        from . import mqtt
        mqtt.client.loop_start()
