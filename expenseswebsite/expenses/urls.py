from django.contrib import admin
from django.urls import path, include
from .views import index,addexpenses



urlpatterns = [
    path('',index,name='home'),
    path('add-expenses',addexpenses,name='addexpenses'),
]
