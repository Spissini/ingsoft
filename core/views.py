from django.http import request
from django.shortcuts import render, redirect
from .models import APORTE

# Create your views here

def home(request):
    return render(request, 'core/home.html')

def log_in(request):
    return render(request, 'core/sesion/log_in.html')

def Aporte(request):
    aportes = APORTE.objects.all()
    contexto = {"Aportes":aportes}    
    return render(request, 'core/MenuBar/Juegos/EquipoAlbion.html', contexto)

