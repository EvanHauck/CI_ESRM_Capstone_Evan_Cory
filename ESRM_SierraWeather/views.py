from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

def mainpage(request):
    template = "ESRM_SierraWeather/templates/Main_Page.html"
    return render(request,template)