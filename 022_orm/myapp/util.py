from faker import Faker
fake = Faker()
from myapp.models import *
import random
def create():
    depts = Dept.objects.all()
    for i in range(25):
        name = fake.name()
        email = fake.email()
        age = random.randint(20,35)
        dept = depts[random.randint(0,len(depts)-1)]
        
        Student.objects.create(name=name,email=email,age=age,dept=dept)
        print("created")
        

