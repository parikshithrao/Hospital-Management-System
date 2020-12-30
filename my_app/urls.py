from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
                path('', views.home, name = 'home'),
                path('pari', views.pari, name = 'pari'),
                path('adddoc', views.adddoc, name = 'adddoc'),
                path('register',views.register,name = 'register'),
                path('doctorlogin',views.doctorlogin,name = 'doctorlogin'),
                path('docapp',views.docapp,name = 'docapp'),
                path('appointment',views.appointment, name = 'appointment'),

]
