from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'home', views.home, name = 'home' ),
                url(r'new-create', views.pari, name ='new-create' ),


]
