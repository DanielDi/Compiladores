# Compiladores

Para instalar por primera vez:
 - instalar python 
 - abrir cmd: pip3 install pipenv
 - ubicarse en la carpeta del proyecto: pipenv install
 - para verificar que funciona, ejecutar ensayo.py

 Para correr la app web "poke_app":
 - Añadir el archivo secrets.py en la carpeta poke_app/poke_app el cual contiene la clave secreta del proyecto django
 - Ubicarse en la carpeta poke_app
 - Ejecutar el comando: py manage.py runserver
 - Ingresar con el navegador a http://localhost:8000
 - Verificar que aparece la página de bienvenida de django

 Nota:
 Fijarse si es en el ambiente generado por pipenv.
 Si esta usando visual studio code 
 views -> command palette -> python lect interprer -> (el que dice 'Compiladores:pipenv' o similar)
