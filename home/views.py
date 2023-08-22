from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse("adsda")
    context={
        'variable':"this is the end"
    }
    
    return render(request,"index.html",context)

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Request has been updated for order')
    return render(request,"contact.html") 

def aboutus(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html") 

def home(request):
    
    return render(request,"index.html")