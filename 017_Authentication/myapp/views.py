from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get("username")
        password = data.get("password")
        
        u = authenticate(username=uname, password=password)
        if u is not None:
            login(request,u)
            return redirect("home")
        else:
            return render(request,"login.html",{"err":"Invalid username or password"})
    
    if request.user.is_authenticated:
        return redirect("home")
    return render(request,"login.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("firstname")
        lname = data.get("lastname")
        uname = data.get("username")
        password = data.get("password")
        
        if User.objects.filter(username=uname).exists():
             return render(request,"reg.html",{"err":"Username already exist ! "})
        else:
            u = User(first_name=fname, last_name=lname, username=uname)
            u.set_password(password)
            u.save()
        
        return render(request,"reg.html",{"msg":"Registration successfully "})
        
    return render(request,"reg.html")

@login_required(login_url="index")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    logout(request)
    return render(request,"login.html")