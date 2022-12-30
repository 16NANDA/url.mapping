from django.urls import path
from app1.views import *
app_name = 'som'



urlpatterns = [ 
    path('sagar/',sagar,name='sagar'),
]