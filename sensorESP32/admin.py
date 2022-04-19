from django.contrib import admin

from sensorESP32.models import SensorReading
from sensorESP32.models import Recommadation

# Register your models here.
admin.site.register(SensorReading)
admin.site.register(Recommadation)