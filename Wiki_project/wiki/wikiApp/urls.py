from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('landing/', views.landing, name='landing'),
    path('edit/', views.edit, name='edit'),
    path('logIn/', views.logIn, name='logIn'),
    path('logOut/', views.logOut, name='logOut'),
    path('signUp/', views.signUp, name='signUp')

]