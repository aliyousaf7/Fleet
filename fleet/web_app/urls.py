
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include

urlpatterns = [
 
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path("", include("accounts.urls"))
]
