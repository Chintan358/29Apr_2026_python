from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("payment",payment,name="payment"),
    path("emailsend",email_send,name="emailsend"),
    path("htmlemail",email_html,name="htmlemail"),
    path("attachemail",email_attach,name="attachemail"),
    path("sms",sms,name="sms")
]