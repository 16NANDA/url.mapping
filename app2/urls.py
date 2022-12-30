from django.urls import path
from app2.views import *
app_name = 'thing'

urlpatterns = [ 
    path('gangaraj/',gangaraj,name='gangaraj'),
]