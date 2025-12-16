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

        req.session['name']=n
        req.session['email']=e
        req.session['password']=p
        return render(req,'landing.html',{'msg1': "data set successfully"})
    
def get_data(req):
    n = req.session.get('name')
    e = req.session.get('email')
    p = req.session.get('password')
    data = {'name':n,'email':e, 'password': p}
    return render(req,'landing.html',{'data':data},{'msg2':"Get data from session"})

def delete_data(req):
    if req.session.get('name') and req.session.get('email'):
        del req.session['name']
        del req.session['email']
        del req.session['password']
        # req.session.flush()
        return render(req,'landing.html',{'msg3':"data deleted"})
    else:
        return render(req,'landing.htnl',{'msg3': "data not found"})
