from django.shortcuts import render,redirect
from .models import Aadhar,Student
from django.contrib import messages



def landing(req):
    return render(req,'landing.html')





def aadhar(req):
    if req.method == "POST":
        a = req.POST.get('aadhar')
        c = req.POST.get('created_by')
        print(a, c)
        std = Aadhar.objects.create(aadhar_no=a, created_by=c)
        messages.success(req, 'Aadhar created successfully')
        return redirect('aadhar')
    return render(req, 'aadhar.html')

def  student(req):
    if req.method=="POST" :
        n=req.POST.get('name')
        a=req.POST.get('age')
        aa=req.POST.get('aadhar')
        aadhar_obj = Aadhar.objects.get(id=aa)
        c=req.POST.get('contact')
        print(n,a,aa,c)
        std=Student.objects.create(name=n,age=a,aadhar=aadhar_obj,contact=c)
        messages.success(req,'student created successfully')
        return redirect('student')
    all_aadhar=Aadhar.objects.all()
    return render(req, 'student.html', {'all_aadhar': all_aadhar})