from rest_framework import serializers

from sensorESP32.models import SensorReading, Recommadation

class SensorDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorReading
        fields = ['humidity',
                'temperature', 
                'moisture',
                'ph',
                'date_of_reading',
                ]

class cropRecommandationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommadation
        fields = ['recommadate_date',
                  'recommadate_crop',
                ]