from django.contrib import admin
from django.urls import path, include
from .views import aporte, home, log_in, sign_in, reg_aporte, visualizaraporte, eliminaraporte, editaraporte, edaportes

urlpatterns = [
    path('', home, name='home'),
    path('log_in', log_in, name='log_in'),
    path('sign_in', sign_in, name='sign_in'),
    path('aporte', aporte, name='aporte'),
    path('reg_aporte', reg_aporte, name='reg_aporte'),
    path('visualizaraporte', visualizaraporte, name='visualizaraporte'),
    path('eliminaraporte/<int:id>', eliminaraporte, name='eliminaraporte'),
    path('editaraporte/<int:id>', editaraporte, name='editaraporte'),
    path('edaportes', edaportes, name='edaportes'),
]