#This file is created by me 
#User urls.py file 

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path ("", views.index, name="user index"),
    path ("about", views.about, name="about"),  
    path ("contact", views.contact, name="Contact Us"),
    path ("track", views.track, name="Track Task"),
    path ("login/signUp", auth_views.LoginView.as_view(), name="Login/Sign Up"),
    # path ("login/signUp", views.login_signUp, name="Login/Sign Up"),
    path ("help", views.help, name="help"),
    path ("Register", views.RegisterView.as_view(), name="Event Registeration"),
    path ("report", views.report, name="report"),
    path ("confirm", views.confirm, name="Confirm Event"),
    path ("Meeting1", views.Meeting1, name="Meeting 1"),
    path ("Meeting2", views.Meeting2, name="Meeting 2"),
    path ("goodluck", views.goodluck, name="Good Luck"),
    path ("bill", views.bill, name="Total Bill"),

]