from django.shortcuts import render,redirect
import razorpay
from django.http  import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
import requests


def index(request):
    return render(request,"index.html")

def payment(request):
    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_TOqCWmcFFPZQOB", "Hhm19s6HIdJkH3Huv8qWHZcd"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    
    return JsonResponse(payment)



def email_send(request):

    if request.method=='POST':
        data = request.POST
        to = data.get('to')
        subject = data.get("subject")
        message = data.get("message")

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to],
            fail_silently=False,
        )

        return render(request,"index.html",{"success":"Email sent successfully"})
    
    
def email_html(request):
    subject = "Order Confirmation"

    text_content = """
    Thank you for your order.

    Your order has been successfully placed.
    """

    html_content = """
    <html>
        <body>
            <h1>Order Confirmation</h1>

            <p>Thank you for your order.</p>

            <p>
                Your order has been successfully placed.
            </p>

            <h3>Order Details</h3>

            <ul>
                <li>Order ID: #1001</li>
                <li>Total: ₹2,500</li>
                <li>Status: Confirmed</li>
            </ul>
        </body>
    </html>
    """
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,
        to=['chintan.tops@gmail.com','coderlife6@gmail.com','vivekp7573@gmail.com']
    )

    email.attach_alternative(
        html_content,
        "text/html"
    )
    
    email.send()

    return HttpResponse("Order email sent")

def email_attach(request):
        email = EmailMessage(
        subject="Your Invoice",
        body="""
            Hello,

            Please find your invoice attached.

            Thank you.
            """,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["chintan.tops@gmail.com"],
        )

        # Attach file
        email.attach_file(
            "a.jpg"
        )

        email.send(fail_silently=False)

        return HttpResponse("Email with attachment sent successfully")
    
    
def sms(request):
    data  =request.POST
    number = data.get("number")
    msg = data.get("msg")

    url = f"https://www.fast2sms.com/dev/bulkV2?route=q&message={msg}&numbers={number}"

    headers = {
        "accept": "application/json",
        "Authorization": "APIKEY"
    }

    response = requests.get(url, headers=headers)

    return render(request,"index.html",{"msg":"sms sent successfully"})