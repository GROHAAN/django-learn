from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html', {'name':"this side rohaan"})

def home(req):
    return render(req,'home')

def contact(req):
    return render(req, 'contact.html')