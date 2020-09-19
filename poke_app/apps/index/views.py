from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from . import ensayo
import json
import os

# Create your views here.

def crearFormulario(form_json, idForm):
  formulario = "<h3>" + form_json['Área de texto 1'] + "</h3>" + "<form action=''>"
  campos = (form_json['campos']).split(';')
  id_etiqueta = 1
  for campo in campos:
    nombre, tipo = campo.split(':')
    label = "<label for='" + idForm + "." + str(id_etiqueta) + "'>" + nombre + "</label><br>"
    entrada = "<input type='" + tipo + "' id='" + idForm + "." + str(id_etiqueta) + "'><br>"
    formulario += label + entrada
    id_etiqueta += 1

  formulario += "<br><input type='submit' value='Enviar'></form>"
  return formulario

def crearBoton(boton_json, idBoton):
  boton = "<button type='button' id='" + idBoton + "'>" + boton_json['Área de texto 1'] + "</button>"
  return boton

def index(request):
  context = {}
  if request.method == 'POST' and request.FILES['myFile']:
    myfile = request.FILES['myFile']    # Este es el archivo que se va a depurar
    fs = FileSystemStorage()

    # Almacena un nuevo archivo y retorna su nombre 
    # Se almacena en la ruta definida en la variable MEDIA_ROOT en el archivo settings.py
    filename = fs.save(myfile.name, myfile)   # fs.save(nombre, contenido)

    ensayo.main(filename)

    ruta_json = os.path.abspath('json.json') 

    mi_json = open(ruta_json, 'r').read()
    mi_json = json.loads(mi_json)
    
    print(mi_json)  

    numForm = 0
    numBoton = 0

    for obj in mi_json:
      if (obj['tipo'] == 'formulario'):
        numForm += 1
        idForm = 'formulario' + str(numForm)
        context[idForm] = crearFormulario(obj, idForm)

      if (obj['tipo'] == "boton"):
        numBoton += 1
        idBoton = 'boton' + str(numBoton)
        context[idBoton] = crearBoton(obj, idBoton)


    print("Num formularios:", numForm)
    print("Num botones:", numBoton)

    # render(request, 'index.html', context)
    # return HttpResponseRedirect("/")

  return render(request, 'index.html', context)