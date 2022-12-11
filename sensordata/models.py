from django.db import models
import datetime

# Create your models here.


class SensorType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):		# new
        return self.name	# new

class Sensor(models.Model):
    type = models.ForeignKey(SensorType, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=300)
    
    def __str__(self):		# new
        return self.name	# new

class Measure(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=True)
    value = models.CharField(max_length=300, blank=True)
    measurement_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):		# new
        return self.value	# new    
        