from django.db import models

# Create your models here.
class Reading(models.Model):
    location = models.CharField(max_length=100)
    weather = models.CharField(max_length=20)
    wind_str = models.CharField(max_length=100)


    def __str__(self):
        return self.location