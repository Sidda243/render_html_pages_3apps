from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def a(request):
    return render(request,'a.html')

def b(request):
    return render(request,'b.html')

def hii(request):
    return HttpResponse('<marquee><h1>This is a string of project9 app</h1></marquee>')