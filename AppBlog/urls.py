from django.urls import path
from AppBlog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('', inicio, name = 'inicio'),
path('destino', destinos, name='destinos'),
path('nosotros', nosotros, name='nosotros'),
path('contacto', contacto, name='contacto'),
path('destinosForm', destinosFormulario, name='destinosForm'),
path('destinosLeer', destinosLeer, name='destinosLeer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)