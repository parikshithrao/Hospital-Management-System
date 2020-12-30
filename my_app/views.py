from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage, send_mail
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
def docapp(request):
    return render(request,'docapp.html')


def doctorlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Doctor.objects.filter(email = email).first()
        user = authenticate(request,email = email,password = password)

        if user is not None :
            auth.login(request,user)
            return HttpResponseRedirect(reverse("docapp"))

        else:
            messages.info("invalid login credentials")
            return HttpResponseRedirect(reverse("doctorlogin"))



    return render(request,'doctorlogin.html')



def random_num():
    rnum = random.randint(100000,999999) #generates random 6 digt number
    print(rnum)
    return rnum

def register(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        email = request.POST['email']
        code = request.POST['code']
        password = request.POST['password']
        re_password = request.POST['re_password']
        code1 = DoctorRegister.objects.filter(doctor_email = email ).values("confirmation_code")[0]['confirmation_code']
        print(code1)


        if Doctor.objects.filter(email = email).exists() :
            messages.info(request, "Email already exists, Please login")
            return HttpResponseRedirect(reverse("register"))

        elif code1 != code:
            messages.info(request, "Invalid Confirmation code")
            return HttpResponseRedirect(reverse("register"))

        elif password != re_password:
            messages.info(request, "password does not match")
            return HttpResponseRedirect(reverse("register"))

        else:
            user = Doctor.objects.create(fname = fname,lname = lname,gender = gender,email = email)
            user.set_password(password)
            user.save()

            subject = "Account Successfully Created "
            message = "Hello" + fname + "You Were Registered successfully\n" \
                        "Thanks & Regards\n"\
                        "Parikshith & Keerthi vaidyanath"
            reciever = email
            send_mail(subject, message, EMAIL_HOST_USER, [reciever], fail_silently=False)
            return HttpResponseRedirect(reverse("home"))

    else :
        return render(request,'register.html')



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
            'link' : "http://127.0.0.1:8000"+reverse("register")
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

def appointment(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        pmail = request.POST['pmail']
        doc = request.POST['doc']

    else:
        return render(request,'appointment.html')



def pari(request):
    return render(request,'index.html')


