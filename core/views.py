from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect
from .models import APORTE, residente, ingresos
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserForm

 
# Create your views here

def home(request):
    return render(request, 'core/home.html')

def log_in(request):
    return render(request, 'core/sesion/log_in.html')

#def sign_in(request):
#    return render(request, 'core/sesion/sign_in.html')

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
    ap1 = APORTE.objects.get(idAporte = id)
    
    contexto = {
        "apor11" : ap1
        
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
    return redirect('visualizaraporte')


def ini_sesion(request):
    u = request.POST['username']
    p = request.POST['password']
    user = authenticate(username = u, password = p)

    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario Inactivo')
    else:
        messages.error(request, 'Usuario o Contraseña Incorrecta')
    return redirect('login')

def cerr_sesion(request):
    logout(request)
    return redirect('home')

def registro_usuario(request):
    data = {
        'form':CustomUserForm()

    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    return render(request, 'core/sesion/sign_in.html', data)

def regis_resident(request):
    rutresident = request.POST['rut_res']
    nombsresident = request.POST['nomb_res']
    edadresident = request.POST['edad_res']
    tutorresi = request.POST['tutor']
    medicaresident = request.POST['medic_res']
    saludresident = request.POST['salud_res']
    cuidadresident = request.POST['cuida_res']
    ficharesidente = request.FILES['ficha_res']

    residente.objects.create(rutResident = rutresident, nombsResident = nombsresident, edadResident = edadresident ,tutorResi = tutorresi, medicaResident = medicaresident, \
        saludResident = saludresident, cuidadResident = cuidadresident, fichaResidente = ficharesidente)

    messages.success(request,'Residente registrado')
    return redirect('agregar_res')

def agregar_res(request):

    return render(request, 'core/agregarres.html')

def regis_ingreso(request):
    aa1 = request.POST['cod_ingr']
    salida_res = request.POST['sali_res']
    ingreso_res = request.POST['ing_res']
    rut_res1 = request.POST['rut_resi']
    rut_res2 = residente.objects.get(rutResident = rut_res1)

    ingresos.objects.create(idIngreso = aa1, salidaRes = salida_res, ingresoRes = ingreso_res , Residente = rut_res2)

    messages.success(request,'Equipamiento registrado')
    return redirect('regsalida')

def regsalida(request):
    hehe = residente.objects.all()
    contexto = {"rut": hehe}
    return render(request, 'core/supervisor/regingreso.html', contexto)

def visingreso(request):
    vis = ingresos.objects.all()
    contexto = {"Vising":vis }

    return render(request, 'core/supervisor/visingreso.html', contexto) 


def visresidente(request):
    vre = residente.objects.all()
    contexto = {"Vistares":vre }

    return render(request, 'core/supervisor/visresidente.html', contexto)

def eliminaresidente(request, id):
    reside1 = residente.objects.get(rutResident = id)
    reside1.delete()
    messages.success(request, 'Residente Eliminado')
    return redirect('visresidente')

def editaresidente(request, id):
    er1 = residente.objects.get(rutResident = id)
    contexto = {
        "eres11" : er1
    }
    return render(request, 'core/editar_residente.html', contexto)
    
def edresidente(request):
    rutresident2 = request.POST['ole1']
    nombsresident2 = request.POST['ole2']
    edadresident2 = request.POST['ole3']
    tutorresi2 = request.POST['ole4']
    medicaresident2 = request.POST['ole5']
    saludresident2 = request.POST['ole6']
    cuidadresident2 = request.POST['ole7']

    a2 = residente.objects.get(rutResident = rutresident2)
    a2.cantAporte = nombsresident2
    a2.rutAportador = edadresident2
    a2.nombAportador = tutorresi2
    a2.apeAportador = medicaresident2
    a2.numTarjeta = saludresident2
    a2.numTarjeta = cuidadresident2
    a2.save()
    messages.success(request, 'Residente editado correctamente')
    return redirect('visresidente')

def visresidenf(request):
    vrenf = residente.objects.all()
    contexto = {"Vistares":vrenf }
    return render(request, 'core/visresidenf.html', contexto)


def editaresidenf(request, id):
    erf1 = residente.objects.get(rutResident = id)
    contexto = {
        "eres13" : erf1
    }
    return render(request, 'core/supervisor/editaresidenf.html')

def edresidenf(request):
    rutresident3 = request.POST['oleo1']
    nombsresident3 = request.POST['oleo2']
    edadresident3 = request.POST['oleo3']
    tutorresi3 = request.POST['oleo4']
    medicaresident3 = request.POST['oleo5']
    saludresident3 = request.POST['oleo6']
    cuidadresident3 = request.POST['oleo7']

    a2 = residente.objects.get(rutResident = rutresident3)
    a2.cantAporte = nombsresident3
    a2.rutAportador = edadresident3
    a2.nombAportador = tutorresi3
    a2.apeAportador = medicaresident3
    a2.numTarjeta = saludresident3
    a2.numTarjeta = cuidadresident3
    a2.save()
    messages.success(request, 'Residente editado correctamente')
    return redirect('visresidenf')

def menu(request):
    return render(request, 'core/menuadmin.html')
