from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
  if request.method == 'POST' and request.FILES['myFile']:
    myfile = request.FILES['myFile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    return render(request, 'index.html', { 'uploaded_file_url': uploaded_file_url })

  else:
    return render(request, 'index.html')