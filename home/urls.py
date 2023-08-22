from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("contact",views.contact,name='contact'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("services",views.services,name="service"),
    path("home",views.home,name="home"),
]