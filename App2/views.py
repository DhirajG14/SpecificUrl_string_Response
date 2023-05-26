from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def String2(request):
    return HttpResponse('This is mssg from App2!!!')