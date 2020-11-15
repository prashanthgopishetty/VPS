from django.db import models

class ParkingSlot(models.Model):
    slot = models.PositiveIntegerField()
    car_no = models.CharField(max_length=10)