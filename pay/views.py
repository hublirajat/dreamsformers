from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import json
import requests
from .models import UserProfile
from .models import Booking
from .models import Payment
from .forms import BookingCreationForm
import random
from random import randint
import string

# Create your views here.
def index(request):
	form = BookingCreationForm()
	return render(request, 'index.html', {'form': form})

def fb_pay(request):
    print 'test2'
    return render(request, 'fb_pay.html')

def fb_pay_2(request):
    print 'test'
    return render(request, 'fb_pay_2.html')

def fb_pay_3(request):
    print 'test'
    return render(request, 'fb_pay_3.html')

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
			variables = {"bookingRef" : bookingRef, "amount": amount, "pri" : paymentId}
	#return HttpResponse("OK");
	return render_to_response('paymentpage.html',{'variables' : variables})

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))



token = "https://graph.facebook.com/v2.6/me/messages?access_token=CAAXZBFEk62ZAgBAKZC7vjrgSNcHZB1TZB0oiCDcdqUyoUkZAFFBD7w1dHbpz0GkNgIwU99PH06ilC6IwZChD81OV2GCRZBHrZCkKNZBqYllIEy1Gy1VbgpS8nHpj5A4KPZBBSZAUG3oBYV0AIWzpJYUtebGpYDPWHCAQrW44P4vFdHZBZB0tZAe3hbMrLi3jQ3sz6bOZBkPVkMAXYHVA2AZDZD"

def sendResponse(sender, message_text):
    data = {}
    data["message"] = {}
    data["message"]["text"] = message_text
    data["recipient"] = {}
    data["recipient"]["id"] = sender

    print 'Sending:',data

    response = requests.post(token,json=data)
    print 'Response :', response, response.content

def sendResponseImage(sender, image_url):
    data = {}
    data["recipient"] = {}
    data["recipient"]["id"] = sender

    data["message"] = {}
    data["message"]["attachment"] = {}
    data["message"]["attachment"]["type"] = "image"
    data["message"]["attachment"]["payload"] = {}
    data["message"]["attachment"]["payload"]["url"] = "https://dreamsformers.herokuapp.com/static/pay/ReceiveConfirmationPhone.png"
    print 'Sending:',data
    response = requests.post(token,json=data)
    print 'Response :', response, response.content

def handleMessage(sender, message_text):
    if "pay" in message_text.lower():
        sendResponse(sender, "You're flight has been paid!")
        sendResponse(sender, "Here is your boarding pass:")
        sendResponse(sender, "PNR:"+''.join(random.choice('0123456789ABCDEF') for i in range(6)))
        sendResponse(sender, "Ticket Number:"+''.join(random.choice('0123456789') for i in range(11)))
        sendResponseImage(sender,"test")
    else:
        sendResponse(sender, "I don't understand")

@csrf_exempt
def messengerhook(request):
    print request
    if request.method == 'GET':
        if(request.GET.get('hub.verify_token') == 'test'):
            return HttpResponse(request.GET.get('hub.challenge',''))
        else:
            print request.GET.get('hub.challenge','')
            return HttpResponse("OK");
    elif request.method == 'POST':
        try:
            print request.body
            json_data = json.loads(request.body)

            messaging_events = json_data["entry"][0]["messaging"]
            for entry in json_data["entry"]:
                for event in entry["messaging"]:
                    if "message" in event:
                        print event["message"]["text"]
                        handleMessage(event["sender"]["id"],event["message"]["text"])
                    else:
                        if "recipient" in event and "delivery" not in event:
                            print event
                            if "optin" in event:
                                print "here"
                                if "ref" in event["optin"]:
                                    print "here2"
                                    pid = event["optin"]["ref"]
                                    print pid
                                    for payment in Payment.objects.filter(paymentId=pid):
                                        print payment
                                        sendResponse(event["sender"]["id"], "Hello, please pay for your ticket REF#"+pid)
                                        sendResponse(event["sender"]["id"], "Amount: "+payment.amount+" "+payment.currency)
                return HttpResponse("OK")
        except:
            return HttpResponse("OK")
