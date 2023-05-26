App_Name='App1'
from django.urls import path
from App1.views import *
urlpatterns=[
    path('String1/',String1,name='String1')
]