from django.db import models

# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=300)
    #measurement_date = models.DateField()
    
    def __str__(self):		# new
        return self.name	# new

        