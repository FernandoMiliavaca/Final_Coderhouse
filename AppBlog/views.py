from django.shortcuts import render
from .models import Destino
from AppBlog.forms import DestinosFormulario

# --- Inicio: 

def inicio(request):
    return render (request, 'inicio.html')

#------------------------------------------------
#-------------------Destinos---------------------
#------------------------------------------------

def destinos(request):
    return render(request, 'destinos.html')

def destinosFormulario(request):
    if request.method == 'POST':
        form = DestinosFormulario(request.POST, files=request.FILES)
        print(form)

        if form.is_valid():

            informacion = form.cleaned_data
            print(informacion)
            titulo=informacion['titulo']
            subtitulo=informacion['subtitulo']
            lugar=informacion['lugar']
            provincia=informacion['provincia']
            fecha=informacion['fecha']
            cuerpo=informacion['cuerpo']
            autor=informacion['autor']
            imagen=informacion['imagen']
            #tituloimagen=informacion['tituloimagen']

            destino_nuevo = Destino (titulo=titulo, subtitulo=subtitulo, lugar=lugar, provincia=provincia, fecha=fecha, cuerpo=cuerpo, autor=autor, imagen=imagen)
            destino_nuevo.save()

            return render(request, 'inicio.html')

    else: 
        formulario = DestinosFormulario()

    return render (request, 'destinosForm.html', {'form':formulario})
    



def destinosLeer(request):
    destinos = Destino.objects.all()
    
    return render (request, 'destinosLeer.html', {'destinos':destinos})


def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

