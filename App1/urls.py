from django.urls import path
from App1.views import *
app_name='Anything'
urlpatterns=[
    path('msd/',msd,name='msd')
]