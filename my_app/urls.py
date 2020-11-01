from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
                path('', views.home, name = 'home'),
                path('pari', views.pari, name = 'pari'),
                path('adddoc', views.adddoc, name = 'adddoc'),

]
