from django.shortcuts import render, HttpResponse

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')


def fbcallback(request):
    if request.method == 'POST':
        print 'Raw Data: "%s"' % request.body
    return HttpResponse("OK");
