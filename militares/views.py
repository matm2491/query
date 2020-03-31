from django.shortcuts import render
from django.http import HttpResponse

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instanciamos el modelo 'Postres' para poder usarlo en nuestras Vistas CRUD
from .models import Soldados_registrado , Soldado

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

def index(request):
    return HttpResponse("Hola bb")

class soldado_registro(ListView):
	model = Soldados_registrado
	#asd = Soldados_registrado.objects.select_related('Soldado','Cuartel', 'Servicio', 'Cuerpos_del_ejercito', 'Compañia')
	asd = Soldados_registrado.objects.select_related('soldado')

def base(request):
    return render(request, 'militares/base.html', {"hola":"good"})