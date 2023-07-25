from django.urls import path
from app2.views import *

urlpatterns = [
    path('e/',e,name='e'),
    path('f/',f,name='f'),
    path('hee/',hee,name='hee'),
]