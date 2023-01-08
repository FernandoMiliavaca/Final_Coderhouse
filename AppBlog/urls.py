from django.urls import path
from AppBlog.views import *


urlpatterns = [

path('', destinosLeer, name = 'inicio'),
path('destinos', destinos, name='destinos'),
path('nosotros', nosotros, name='nosotros'),
path('destinosForm', destinosFormulario, name='destinosForm'),
path('destinosLeer', destinosLeer, name='destinosLeer'),
path('destinosEliminar/<id>', destinosEliminar, name='destinosEliminar'),
path('destinosEditar/<id>', destinosEditar, name='destinosEditar'),
]

