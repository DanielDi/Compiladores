from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import json
import os
from . import ensayo
from . import funciones_html

# Create your views here.

def index(request):
  application = {}
  context = {
    'application': application 
  }
  
  if request.method == 'POST' and request.FILES['myFile']:
    myfile = request.FILES['myFile']
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
        application[idForm] = funciones_html.crearFormulario(obj, idForm, mi_json)

      if (obj['tipo'] == "boton"):
        numBoton += 1
        idBoton = 'boton' + str(numBoton)
        application[idBoton] = funciones_html.crearBoton(obj, idBoton)

      if (obj['Nombre'] == "Almacén de datos"):
        funciones_html.crearSentenciaTablas(obj, mi_json)


    print("Num formularios:", numForm)
    print("Num botones:", numBoton)

    print(len(context['application']))
    print(context['application']['formulario2'])
    # render(request, 'index.html', context)
    # return HttpResponseRedirect("/")

  #elif request.method == 'GET':
    #funciones_html.crearSentenciaInsert(request)

  return render(request, 'index.html', context)
