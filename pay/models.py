from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
	#user = models.ForeignKey(User, unique=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=140)
    address = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=5)
    country = models.CharField(max_length=100)
    fbId = models.CharField(max_length=100)
	#ffid = models.CharField(max_length=100)


class Booking(models.Model):
        bookingRef = models.CharField(max_length=100)
        ticketNumber = models.CharField(max_length=200)
        origin = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	dateOfBooking = models.DateTimeField(auto_now_add=True)
	dateOfTravel = models.DateTimeField()


class Payment(models.Model):
        paymentId = models.CharField(max_length=100)
	bookingRef = models.ForeignKey(Booking)
	amount = models.CharField(max_length=200)
	currency =  models.CharField(max_length=200)
	approvalCode = models.CharField(max_length=200)
