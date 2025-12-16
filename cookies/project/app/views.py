from django.shortcuts import render

# Create your views here.


def landing(req):
    return render(req,'landing.html')


def set(req):
    return render(req,'set.html')



def set_data(req):
    if req.method=='POST':
        n= req.POST.get('name')
        e= req.POST.get('email')
        p= req.POST.get('password')
        print(n,e)

        response= render(req,'landing.html',{'msg': "cookies set"})
        response.set_cookie('name',n ,) # max_age=60*2 used for timer for cookies store
        response.set_cookie('email',e)
        response.set_cookie('password',p)
        return response
    

    
def get_data(req):
    if req.COOKIES.get('name') and req.COOKIES.get('email') and req.COOKIES.get('password'):
        n= req.COOKIES.get('name')
        e= req.COOKIES.get('email')
        p= req.COOKIES.get('password')
        data= {'name':n, 'email':e, 'password':p}
        return render(req,'get.html',{"data":data})
    return render(req,'landing.html',{'msg':"cookies not found"})


def delete_cookies(req):
    if req.COOKIES.get('name') and req.COOKIES.get('email'):
        response= render(req,'landing.html',{'msg': "cookies deleted"})
        response.delete_cookie('name')
        response.delete_cookie('email')
        response.delete_cookie('password')
        return response
    return render(req,'landing.html',{'msg': "do not found cookies"})