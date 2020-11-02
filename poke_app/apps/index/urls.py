from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('data/', views.datos)
]

# Ruta para acceder a los diagramas de la app desde el navegador
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)