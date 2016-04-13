from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import UserProfile
import random
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
        newuser.fbId = json_data["id"]
        print 'FBID:',json_data["id"]
        newuser.firstName = json_data["name"].split(' ')[0]
        newuser.lastName = json_data["name"].split(' ')[1]
        newuser.save()

    return HttpResponse("OK");

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

def handleMessage(sender, message_text):
    if "pay" in message_text.lower():
        sendResponse(sender, "You're flight has been paid!")
        sendResponse(sender, "Here is your boarding pass:")
        sendResponse(sender, "PNR:"+''.join(random.choice('0123456789ABCDEF') for i in range(6)))
        sendResponse(sender, "Ticket Number:"+''.join(random.choice('0123456789') for i in range(11)))
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
                        if "recipient" in event:
                            pass
                            #sendResponse(event["sender"]["id"], "Hello, please pay for your ticket")
                return HttpResponse("OK")
        except:
            return HttpResponse("OK")
