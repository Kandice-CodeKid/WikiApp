from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name=index),
    path('landing', views.landing, name=landing),
    path('edit', views.edit, name=edit),
    path('logIn', views.logIn, nane=logIn),
    path('logOut',views.logOut, name=logOut)

]