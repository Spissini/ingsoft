from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect
from .models import APORTE
 
# Create your views here

def home(request):
    return render(request, 'core/home.html')

def log_in(request):
    return render(request, 'core/sesion/log_in.html')

def aporte(request):
    return render(request, 'core/aporte.html')

def reg_aporte(request):
    codApo = request.POST['cod_apor']
    cantApo = request.POST['can_apor']
    rutAport = request.POST['rut_aporta']
    nomAport = request.POST['nom_aporta']
    apeAport = request.POST['ap_aporta']
    numTarj = request.POST['num_tar']

    APORTE.objects.create(idAporte = codApo, cantAporte = cantApo, rutAportador = rutAport, nombAportador = nomAport, apeAportador = apeAport, numTarjeta = numTarj)

    messages.success(request,'Aporte Registrado')
    return redirect('aporte')

def visualizaraporte(request):
    visaporte = APORTE.objects.all()
    contexto = {"VisuAporte": visaporte}
    return render(request, 'core/visualizaraporte.html', contexto)