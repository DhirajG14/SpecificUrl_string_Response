App_Name='App2'
from django.urls import path
from App2.views import *
urlpatterns=[
    path('String2/',String2,name='String2')
]