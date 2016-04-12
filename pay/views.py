from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserProfile
from random import randint
import string

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def fbcallback(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print 'Json Data: "%s"' % json_data
        newuser = UserProfile()
        newuser.fbid = str(json_data["id"])
        newuser.firstName = json_data["name"].split(' ')[0]
        newuser.lastName = json_data["name"].split(' ')[1]
        newuser.save()

    return HttpResponse("OK");

def createBooking(request):
        if request.method == 'POST':
                form = EventCreationForm(request.POST)
                if form.is_valid():

			bookingRef = id_generator()
		        ticketNumber = random_with_N_digits(9)
		        origin = form.cleaned_data['fromcity']
			destination = form.cleaned_data['tocity']
			dateOfTravel = form.cleaned_data['datepickerstart']

			# Creating a Booking
			booking = Booking.objects.create(bookingRef = bookingRef, ticketNumber = ticketNumber, origin = origin, destination = destination, dateOfTravel = dateOfTravel)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))



