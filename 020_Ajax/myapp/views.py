from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def test(request):
    q = request.GET['q']
    
    r = ""
    # if q=='electric':
    #     r+="<ol><li>Fan</li><li>Fridge</li><li>TV</li></ol>"
    # elif q=='cloths':
    #         r+="<ul><li>Shirt</li><li>Tshirt</li><li>Cap</li></ul>"
    # else:
    #     r="No Data found"
    
    r+="<ul>"
    products = Product.objects.filter(name__startswith=q)
    for product in products:
        r+=f"<li>{product.name}</li>"
    r+="</ul>"
    
    return HttpResponse(r)

def countries(request):
    countries = Country.objects.all()
    return JsonResponse({"data":list(countries.values())})

def states(request):
    cid = request.GET['cid']
    states = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(states.values())})

def cities(request):
    sid = request.GET['sid']
    cities = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(cities.values())})