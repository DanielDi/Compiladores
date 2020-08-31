from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
  if request.method == 'POST' and request.FILES['myFile']:
    myfile = request.FILES['myFile']    # Archivo a procesar
    fs = FileSystemStorage()

    # Almacena un nuevo archivo y retorna su nombre 
    # Se almacena en la ruta definida en la variable MEDIA_ROOT en el archivo settings.py
    filename = fs.save(myfile.name, myfile)   # fs.save(nombre, contenido)
    
    uploaded_file_url = fs.url(filename)
    return render(request, 'index.html', { 'uploaded_file_url': uploaded_file_url })

  else:
    return render(request, 'index.html')