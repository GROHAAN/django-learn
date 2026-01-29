from django.shortcuts import render,redirect
from django.contrib import messages


# Create your views here.

def landing(req):
    messages.info(req, 'Welcome to the landing page')
    return render (req,'landing.html')

def home(req):
    return render(req,'home.html')

def registration(req):
    return render(req,'registration.html')

def login(req):
    return render(req,'login.html')

def dashboard(req):
    return render(req,'dashboard.html')

