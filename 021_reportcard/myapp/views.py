from django.shortcuts import render,redirect
from myapp.models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string



def index(request):
    students = Student.objects.all()
    paginator = Paginator(students, 5)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"page_obj":page_obj})

def result(request):
    id  =request.GET['id']
    action = request.GET['action']
    data = Marks.objects.filter(student_id=id)
    total = data.aggregate(marks=Sum("mark"))['marks'] or 0
    
    
    
    students =  Student.objects.annotate(total_marks=Sum("marks__mark")).order_by("-total_marks")
    
    rank=0
    for st in students:
        rank+=1
        if st.id==int(id):
            break
    
    
    # total  =0
    # for d in data:
    #     total+=d.mark
        
    per = (total*100)/600
    
    if action=='display':
        return render(request,"result.html",{"data":data,"total":total,"per":round(per,2),"rank":rank})
    elif action=='mail':
        context = {"data":data,"total":total,"per":round(per,2),"rank":rank}

        html_content = render_to_string(
            "result.html",
            context
        )

        email = EmailMultiAlternatives(
            subject="Student Report Card",
            body="Please view this email in an HTML-compatible email client.",
            from_email=settings.EMAIL_HOST_USER,
            to=["chintan.tops@gmail.com"],
        )

        email.attach_alternative(
            html_content,
            "text/html"
        )

        email.send()

        return redirect("index")