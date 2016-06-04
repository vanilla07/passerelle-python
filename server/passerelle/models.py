from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    """ Rooms available for booking."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    capacity = models.IntegerField(default=2)

class Booking(models.Model):
    """ Booking for one room."""
    room = models.ForeignKey('Room', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    guests_number = models.IntegerField()
    date_in =  models.DateTimeField()
    date_out = models.DateTimeField()
    date_reservation = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()
    notes = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=50)
    channel = models.IntegerField()


class Closure(models.Model):
    """ Dates when rooms are closed."""
    label = models.CharField(max_length=100)
    date_start =  models.DateTimeField()
    date_end = models.DateTimeField()
    notes = models.CharField(max_length=1000)

class ClosureRoom(models.Model):
    """ Joint table between rooms and closures."""
    room = models.ForeignKey('Room', on_delete=models.PROTECT)
    closure = models.ForeignKey('Closure', on_delete=models.CASCADE)


