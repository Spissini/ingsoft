from django.contrib import admin
from django.urls import path, include
from .views import aporte, home, ini_sesion , registro_usuario ,cerr_sesion, reg_aporte, visualizaraporte, eliminaraporte, editaraporte, edaportes, agregar_res, regis_resident, \
    regis_ingreso, regsalida, visresidente, editaresidente, edresidente, eliminaresidente
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', home, name='home'),
    # path('sign_in', sign_in, name='sign_in'),
    path('aporte', aporte, name='aporte'),
    path('reg_aporte', reg_aporte, name='reg_aporte'),
    path('visualizaraporte', visualizaraporte, name='visualizaraporte'),
    path('eliminaraporte/<int:id>', eliminaraporte, name='eliminaraporte'),
    path('editaraporte/<int:id>', editaraporte, name='editaraporte'),
    path('edaportes', edaportes, name='edaportes'),

    path('login/', LoginView.as_view(template_name='core/sesion/log_in.html'),name='login'),
    path('sesion', ini_sesion, name='sesion'),
    path('logout', cerr_sesion, name='logout'),

    path('registro/', registro_usuario, name= 'registro_usuario'),

    path('agregar_res', agregar_res, name='agregar_res'),
    path('regis_resident', regis_resident, name='regis_resident'),

    path('regis_ingreso', regis_ingreso, name='regis_ingreso'),
    path('regsalida', regsalida, name='regsalida'),

    path('visresidente', visresidente, name='visresidente'),
    path('editaresidente/<int:id>', editaresidente, name='editaresidente'),
    path('edresidente', edresidente, name='edresidente'),
    path('eliminaresidente/<int:id>', eliminaresidente, name='eliminaresidente'),
]