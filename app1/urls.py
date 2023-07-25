from django.urls import path
from app1.views import *

urlpatterns = [
    path('c/',c,name='c'),
    path('d/',d,name='d'),
    path('hello/',hello,name='hello'),
]