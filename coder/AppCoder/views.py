from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request,"AppCoder/inicio.html")


def personas(request):
    if request.method=="POST":
        form=PersonaForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            personita=Persona(nombre=nombre,apellido=apellido)
            personita.save()
            return render (request,"AppCoder/inicio.html")
    else:
        formulario=PersonaForm()
        return render (request,"AppCoder/personas.html",{"formulario":formulario})



def helado(request):
    if request.method=="POST":
        form= HeladoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            helados=Helado(nombre=nombre)
            helados.save()
            return render(request,"AppCoder/inicio.html")
    else:
        form=HeladoForm()
    return render(request,"AppCoder/helado.html",{"formulario":form})
    
def notas(request):
    if request.method=="POST":
        form= NotasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            nota=Nota(nombre=nombre,apellido=apellido,email=email)
            nota.save()
            return render(request,"AppCoder/inicio.html")
    else:
        form=NotasForm()
    return render(request,"AppCoder/notas.html",{"formulario":form})
    
def busquedaHelados(request):
    return render(request,"AppCoder/busquedaHelados.html")

def buscar(request):
        nombre=request.GET["nombre"]
        helado=Helado.objects.filter(nombre=nombre)
        return render(request, "AppCoder/resultadosBusqueda.html", {"helados":helado})






