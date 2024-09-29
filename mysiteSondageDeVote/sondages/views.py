from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index (request):
    return HttpResponse("hello , je suis Django ! bonne change pour nos débuts😘😜😜😜 ")