from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        print('hello') 
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            return render(request, "success.html")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def home(request):
    return render(request, "home.html")