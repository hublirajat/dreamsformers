from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserProfile
from .models import Booking
from .models import Payment
from .forms import BookingCreationForm
import random
from random import randint
import string

# Create your views here.

# Create your views here.
def index(request):
	form = BookingCreationForm()
	return render(request, 'index.html', {'form': form})

@csrf_exempt
def fbcallback(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print 'Json Data: "%s"' % json_data
        newuser = UserProfile()
        newuser.fbId = json_data["id"]
        print 'FBID:',json_data["id"]
        newuser.firstName = json_data["name"].split(' ')[0]
        newuser.lastName = json_data["name"].split(' ')[1]
        newuser.save()

    return HttpResponse("OK");

@csrf_exempt
def createBooking(request):
        if request.method == 'POST':
		# form is the object for class BookingCreationForm defined in Forms.py
		form = BookingCreationForm(request.POST)
                if form.is_valid():
                        origin = form.cleaned_data['origin']
                        destination = form.cleaned_data['destination']
                        traveldate = form.cleaned_data['traveldate']
			
			# Randomly generate Booking Reference 6 ASCII
			bookingRef = id_generator()

			# Randomly generate Ticket Number 9 digit
			ticketNumber = random_with_N_digits(9)
			print bookingRef

			# Creating a Booking
			booking = Booking.objects.create(bookingRef = bookingRef, ticketNumber = ticketNumber, origin = origin, destination = destination, dateOfTravel = traveldate)
			booking.save()

			# Creating a Payment for the same Booking			
			amount = random_with_N_digits(4)
			currency = "USD"
			paymentId = random_with_N_digits(8)
			payment = Payment.objects.create(bookingRef = booking, amount = amount, currency = currency, paymentId = paymentId)
			payment.save()
	return HttpResponse("OK");

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))



