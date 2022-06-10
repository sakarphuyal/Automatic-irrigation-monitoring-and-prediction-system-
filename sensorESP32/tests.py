from django.test import Client
import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from sensorESP32.models import SensorReading, Recommadation

c = Client()
class SensorDataTest(TestCase):
    def setUp(self):
        Recommadation.objects.create(
            recommadate_date='2022-04-09T14:55:15.568481Z',
            recommadate_crop = 'Muskmelon(खरबूजा)'
        )
    
    def test_sensor_data(self):
        self.assertEqual(
            Recommadation.objects.last().recommadate_crop,'Muskmelon(खरबूजा)'
        )
        self.assertEqual(
            Recommadation.objects.last().recommadate_date,'2022-04-09T14:55:15.568481Z'
        )
        


  
  