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

def eliminaraporte(request, id):
    aport1 = APORTE.objects.get(idAporte = id)
    aport1.delete()
    messages.success(request, 'Aporte Eliminado')
    return redirect('visualizaraporte')


def editaraporte(request, id):
    ap1 = APORTE.objects.get(idEquipo = id)
    

    contexto = {
        "apor11" : ap1,
        
    }
    return render(request, 'core/editaraporte.html', contexto)


def edaportes(request):
    idAportes = request.POST['iAporte']
    cAportes = request.POST['cAporte']
    rAportes = request.POST['rAporte']
    nAportado = request.POST['nAportador']
    aAportado = request.POST['aAportador']
    nTarjet = request.POST['nTarjeta']

    a1 = APORTE.objects.get(idAporte = idAportes)
    a1.cantAporte = cAportes
    a1.rutAportador = rAportes
    a1.nombAportador = nAportado
    a1.apeAportador = aAportado
    a1.numTarjeta = nTarjet
    a1.save()
    messages.success(request, 'Aporte editado correctamente')
    return redirect('editaraporte')
