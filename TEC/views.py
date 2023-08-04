from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

from TEC.models import *

from TEC.forms import *

def index(request):

    control = ControlE.objects.all()
    
    informacion_template = {'control': control}
    
    return render(request, 'index.html', informacion_template)

def crearControlE(request):
    
    if request.method=='POST':
        formulario = ControlEForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ControlEForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearControlE.html', diccionario)

def crearExpositoresCon(request):
    
    if request.method=='POST':
        formulario = ExpositoresConForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(ponentes)
    else:
        formulario = ExpositoresConForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearExpositoresCon.html', diccionario)


def crearConsecionaria(request):
    
    if request.method=='POST':
        formulario = ConsecionariaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ConsecionariaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearConsecionaria.html', diccionario)

def editarConsecionaria(request, id):
    
    consecionaria = Consecionaria.objects.get(pk=id)
    if request.method=='POST':
        formulario = ConsecionariaForm(request.POST, instance=consecionaria)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ConsecionariaForm(instance=consecionaria)
    diccionario = {'formulario': formulario}

    return render(request, 'editarConsecionaria.html', diccionario)

def eliminarConsecionaria(request, id):
    
    consecionaria = Consecionaria.objects.get(pk=id)
    consecionaria.delete()
    return redirect(index)

def crearPonentes(request):
    
    if request.method=='POST':
        formulario = PonentesForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PonentesForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearExpositoresCon.html', diccionario)

def editarPonentes(request, id):
    
    ponentes = Ponentes.objects.get(pk=id)
    if request.method=='POST':
        formulario = PonentesForm(request.POST, instance=ponentes)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PonentesForm(instance=ponentes)
    diccionario = {'formulario': formulario}

    return render(request, 'editarConsecionaria.html', diccionario)

def eliminarPonentes(request, id):
    
    ponentes = Ponentes.objects.get(pk=id)
    ponentes.delete()
    return redirect(index)

def crearAuto(request):
    
    if request.method=='POST':
        formulario = AutoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = AutoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearAuto.html', diccionario)

def editarAuto(request, id):
    
    auto = Auto.objects.get(pk=id)
    if request.method=='POST':
        formulario = AutoForm(request.POST, instance=auto)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = AutoForm(instance=auto)
    diccionario = {'formulario': formulario}

    return render(request, 'editarAuto.html', diccionario)

def eliminarAuto(request, id):
    
    auto = Auto.objects.get(pk=id)
    auto.delete()
    return redirect(index)

def ponentes(request):
    
    expoC = ExpositoresCon.objects.all()
    ponentes = Ponentes.objects.all()
    
    informacion_template = {'expoC': expoC , 'ponentes': ponentes}
    
    return render(request, 'ponentes.html', informacion_template)

def estadisticas(request):
    return  render(request, 'estadisticas.html')