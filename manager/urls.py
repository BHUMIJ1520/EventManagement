#This file is created by me 
#Manager urls.py file 

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="manager index")
]