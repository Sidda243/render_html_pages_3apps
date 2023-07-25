from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def e(request):
    return render(request,'e.html')

def f(request):
    return render(request,'f.html')

def hee(request):
    return HttpResponse('<marquee><h1>This is a string of project9 app2</h1></marquee>')

