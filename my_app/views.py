from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse

from .models import *
from hospital.settings import EMAIL_HOST_USER


def home(request):
    return render(request,'index.html')

def random_num():
    rnum = random.randint(100000,999999) #generates random 6 digt number
    print(rnum)
    return rnum

def adddoc(request):


    if request.method == 'POST':
        email = request.POST['email']
        doctor_name = request.POST['Dname']
        code = random_num()
        print(email)
        print(code)

        if DoctorRegister.objects.filter(doctor_email = email).exists() :
            messages.info(request, "email already exists")
            return HttpResponseRedirect(reverse("adddoc"))



        subject = "please register your details "
        to = [email]
        from_email = EMAIL_HOST_USER

        ctx = {
            'email' : email,
            'code' : code,
        }
        message = render_to_string('email.html',ctx)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)

        msg.content_subtype = 'html'
        msg.send()

        doctor = DoctorRegister()
        doctor.doctor_name = doctor_name
        doctor.doctor_email = email
        doctor.confirmation_code = code
        doctor.save()

        messages.info(request,'Added Successfully')

        return render(request, 'doctor.html')
    else:
        return render(request,'doctor.html')





def pari(request):
    return render(request,'index.html')


