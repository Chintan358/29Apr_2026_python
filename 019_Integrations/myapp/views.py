from django.shortcuts import render,redirect
import razorpay
from django.http  import JsonResponse


def index(request):
    return render(request,"index.html")

def payment(request):
    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_TOqCWmcFFPZQOB", "Hhm19s6HIdJkH3Huv8qWHZcd"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    
    return JsonResponse(payment)