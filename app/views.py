from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Cool(request):
    return HttpResponse('its not cool')

def anjali(request):
    return HttpResponse('<h1><marque>who is this anjali</marque></h1>')