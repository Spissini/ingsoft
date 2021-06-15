from django.contrib import admin
from django.urls import path, include
from .views import aporte, home, log_in, reg_aporte, visualizaraporte

urlpatterns = [
    path('', home, name='home'),
    path('log_in', log_in, name='log_in'),
    path('aporte', aporte, name='aporte'),
    path('reg_aporte', reg_aporte, name='reg_aporte'),
    path('visualizaraporte', visualizaraporte, name='visualizaraporte'),
]