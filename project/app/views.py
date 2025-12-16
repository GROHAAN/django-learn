from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def my_render(req):
    data = {'name': "abhishek",'age': 26, 'gender': "Male"}
    return render(req,'landing.html',data)

def my_httpresponse(req):
    return HttpResponse("<h1>hello this is <i>django</i> </h1>")

def my_redirectext(req):
    return redirect("https://www.google.com")

def my_redirectint(req):
    return redirect('my_redirectint2')

def my_redirectint2(req):
    x= {'x':10,'y':20}

    # return HttpResponse("this is from my side")
    return render(req,'redirect.html',x)



