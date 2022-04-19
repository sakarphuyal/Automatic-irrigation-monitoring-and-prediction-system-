from django.db import models

# Create your models here.
class SensorReading(models.Model):
    # data_id = models.AutoField(Primary)
    humidity = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    moisture = models.CharField(max_length=50)
    ph = models.CharField(max_length=50)
    date_of_reading = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.date_of_reading}")

class Recommadation(models.Model):
    recommadate_date = models.DateTimeField(auto_now_add=True)
    recommadate_crop = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.recommadate_crop}")