from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee as emp

# Create your views here.

def landing(req):
    return render(req, 'landing.html')

def register(req):

    print(req.method)
    print(req.POST)
    print(req.FILES)
    if req.method =='POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        q = req.POST.get('qualification[]')
        g = req.POST.get('gender')
        s = req.POST.get('state')
        i = req.FILES.get('image')
        a = req.FILES.get('audio')
        v = req.FILES.get('video')
        d = req.FILES.get('document')

        Employee.object.create(name =n, email = e, contact = c, qualification= q, gender= g, state= s, image= i, audio= a, video= v,document=d)

        return HttpResponse("Registration Successfully")
        
        
        

    else:
        return render(req, 'register.html')
    

def show_data(req):

    # query that work for single object


    # data= emp.objects.get(id=1)
    # data = emp.objects.first()
    # data = emp.objects.last()
    # data = emp.objects.latest('name')
    # data= emp.objects.earliest('name')
    # data = emp.objects.create(column1 = value,column2= value)
    # print(data.name,data.email,data.contact)

    # query that work for multiple object
    # data = emp.objects.all()
    # data = emp.objects.filter(gender="Female")
    # data = emp.objects.exclude(gender="Female")
    # data = emp.objects.order_by('name') # for ascending order
    # data= emp.objects.order_by('-name') #for descending order
    print(data)
    for i in data:
        print(i.name,i.email,i.contact)
    return render(req,'data.html',{'data':data})


