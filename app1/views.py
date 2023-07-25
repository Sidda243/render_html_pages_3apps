from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def c(request):
    return render(request,'c.html')

def d(request):
    return render(request,'d.html')

def hello(request):
    return HttpResponse('<marquee><h1>This is a string of project9 app1</h1></marquee>')
