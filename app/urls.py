from django.urls import path
from app.views import *

urlpatterns = [
    path('a/',a,name='a'),
    path('b/',b,name='b'),
    path('hii/',hii,name='hii'),
]