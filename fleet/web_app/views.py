from django.shortcuts import render,redirect
from .models import client_data
from .models import fleet_data
from .models import fleet_location


# Create your views here.

#def index(request):
#    dests = client_data.objects.all
#    dests = fleet_data.objects.all
#    dests = fleet_location.objects.all

def index(request):

    return render(request,"index.html")

def contact(request):

    return render(request,"contact.html")

def about(request):
    
    return render(request,"about.html")

def services(request):
    
    return render(request,"services.html")
