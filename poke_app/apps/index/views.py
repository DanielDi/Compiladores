from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import json
import os
import pandas as pd
from . import ensayo
from . import funciones_html

# Create your views here.

def index(request):
  application = {}
  gateway = {}
  context = {
    'application': application,
    'gateway': gateway 
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
    numForm = 0
    numBoton = 0
    numGateway = 0

    for obj in mi_json:
      if (obj['tipo'] == 'formulario'):
        data = pd.read_json(os.path.abspath('json.json'))
        consul = data[(data['Nombre']=='Gateway') & (obj['Origen'] == data['id'] )]
        if(consul.shape[0]>0):
          numForm += 1
          idForm = 'formulario' + str(numForm) + "Gateway" + str(numGateway)
          application[idForm] = funciones_html.crearFormulario(obj, idForm)
        else:
          numForm += 1
          idForm = 'formulario' + str(numForm)
          application[idForm] = funciones_html.crearFormulario(obj, idForm)

      if (obj['tipo'] == "boton"):
        numBoton += 1
        idBoton = 'boton' + str(numBoton)
        application[idBoton] = funciones_html.crearBoton(obj, idBoton)

      if(obj['tipo'] == 'Gateway'):
        numGateway +=1
        idGateway = "Gateway" + str(numGateway)
        print("Entre gateway")
        gateway[idGateway] = str(obj['expresion'])

      if (obj['Nombre'] == "Almacén de datos"):
        print("ENTRÓ A SQL FN")
        funciones_html.crearSentenciaTablas(obj, mi_json)


    print("Num formularios:", numForm)
    print("Num botones:", numBoton)

    print(len(context['application']))
    print(len(context['gateway']))
    # print(context['application']['formulario2'])
    # render(request, 'index.html', context)
    # return HttpResponseRedirect("/")

  #elif request.method == 'GET':
    #funciones_html.crearSentenciaInsert(request)

  return render(request, 'index.html', context
  )
