from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
        name = models.CharField(max_length=100)
        userid = models.CharField(max_length=200)
	name = models.CharField(max_length=100)


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
