from django.shortcuts import render,redirect
from myapp.models import *
import os

# Create your views here.
def index(request):
    categories = Category.objects.all()
    
    if request.method=='POST':
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        qty = data.get("qty")
        category = Category.objects.get(id=data.get('category'))
        image = request.FILES.get('image')
        
        Product.objects.create(name=name,price=price,qty=qty,image=image,category=category)
    
    
    return render(request,"index.html",{"categories":categories})

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{"products":products})


def delete_product(request):
    id = request.GET['id']
    product = Product.objects.get(id=id)
    os.remove(product.image.path)
    product.delete()
    return redirect("display")
    
    
def test(request):
    # books = Book.objects.all()
    # for book in books:
    #     print(book.name)
    #     print(book.price)
    #     print(book.publisher.address.country)
    #     for au in book.author.all():
    #         print(au.name)
    
    author = Author.objects.all()
    for au in author:
        print(au.name)
        print(au.book.all())
    return redirect("index")