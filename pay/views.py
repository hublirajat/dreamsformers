from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserProfile
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
