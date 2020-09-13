from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from . import ensayo

# Create your views here.

def index(request):
  if request.method == 'POST' and request.FILES['myFile']:
    myfile = request.FILES['myFile']    # Este es el archivo que se va a depurar
    fs = FileSystemStorage()

    # Almacena un nuevo archivo y retorna su nombre 
    # Se almacena en la ruta definida en la variable MEDIA_ROOT en el archivo settings.py
    filename = fs.save(myfile.name, myfile)   # fs.save(nombre, contenido)

    ensayo.main(filename)
    print("Archivo:", filename, " cargado con éxito")
    return HttpResponseRedirect("/")

  # Diccionario que se le envía a la plantilla, para imprimir su valor sobre esta se hace por
  # medio de la clave
  context = {}
  context['titulo'] = "<h1>Mi header</h1>"

  context['formulario'] = """
    <form action="/action_page.php">
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname" value="John"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname" name="lname" value="Doe"><br><br>
    <input type="submit" value="Submit">
  """

  return render(request, 'index.html', context)