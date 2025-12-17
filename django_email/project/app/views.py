from django.shortcuts import render
from random import randint
from django.core.mail import send_mail

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def send_otp(req):
    if req.method =="POST":
        e = req.POST.get('email')
        otp = randint(1111,9999)
        req.session['email'], req.session['otp']= e,otp
        send_mail(
            "my site otp from django",
            f"your generated otp is :- {otp} .",
            "ag871998@gmail.com",
            [e],
            fail_silently=False,
            )
        return render(req,'landing.html',{'msg':"otp send successfully..."})
