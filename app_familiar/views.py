from datetime import datetime
from django.shortcuts import render
from app_familiar.models import Persona
from django.template import Template, Context, loader
from django.http import HttpResponse
# Create your views here.

def persona(request):
    persona = Persona(nombre="Matias" , edad="34",  fecha = datetime.now())
    persona1 = Persona(nombre="Laura" , edad="37",  fecha = datetime.now())
    persona2 = Persona(nombre="Santiago" , edad="6",  fecha = datetime.now())
    persona.save()
    persona1.save()
    persona2.save()
    diccionario = {'nombre': persona.nombre, 'edad': persona.edad, 'fecha': persona.fecha }
    plantilla = loader.get_template('vista.html')
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)