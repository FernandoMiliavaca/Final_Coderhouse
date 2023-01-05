from django.urls import path
from AppBlog.views import *


urlpatterns = [

path('', inicio, name = 'inicio'),
path('destino', destinos, name='destinos'),
path('nosotros', nosotros, name='nosotros'),
path('contacto', contacto, name='contacto'),
path('destinosForm', destinosFormulario, name='destinosForm'),
path('destinosLeer', destinosLeer, name='destinosLeer'),
path('destinosEliminar/<id>', destinosEliminar, name='destinosEliminar'),
path('destinosEditar/<id>', destinosEditar, name='destinosEditar'),
]

