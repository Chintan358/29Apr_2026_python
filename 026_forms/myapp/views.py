from django.shortcuts import render,redirect
from myapp.forms import *
from myapp.models import *


def index(request):
    form  = Productform()
    products = Product.objects.all()
    if request.method=='POST':
        product = Productform(request.POST)
        if product.is_valid():
            product.save()
            return redirect("index")
   
    return render(request,"index.html",{"form":form,"products":products})


def delete_product(request):
    id = request.GET['id']
    pro = Product.objects.get(id=id)
    pro.delete()
    return redirect("index")

def update_product(request):
   
    products = Product.objects.all()
    id = request.GET['id']
    pro = Product.objects.get(id=id)
    form  = Productform(instance=pro)
    
    if request.method=='POST':
        product = Productform(request.POST,instance=pro)
        if product.is_valid():
            product.save()
            return redirect("index")
    
    return render(request,"index.html",{"form":form,"products":products})