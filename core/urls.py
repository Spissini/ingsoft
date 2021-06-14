from django.contrib import admin
from django.urls import path, include
from .views import home, log_in

urlpatterns = [
    path('', home, name='home'),
    path('log_in', log_in, name='log_in'),
]