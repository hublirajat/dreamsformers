from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def fbcallback(request):
    if request.method == 'POST':
        print 'Raw Data: "%s"' % json.loads(request.body)
    return HttpResponse("OK");
