from django.contrib import admin
from . import models

admin.site.register(models.Sensor)
admin.site.register(models.SensorType)

class MeasureAdmin(admin.ModelAdmin):
    readonly_fields = ('measurement_date',)

admin.site.register(models.Measure, MeasureAdmin)
