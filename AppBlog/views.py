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



#----------------Crear Destinos------------------

def destinosFormulario(request):
    if request.method == 'POST':
        form = DestinosFormulario(request.POST, files=request.FILES)
        print(form)

        if form.is_valid():

            informacion = form.cleaned_data
            
            titulo=informacion['titulo']
            subtitulo=informacion['subtitulo']
            lugar=informacion['lugar']
            provincia=informacion['provincia']
            fecha=informacion['fecha']
            cuerpo=informacion['cuerpo']
            autor=informacion['autor']
            imagen=imagen=request.FILES['imagen']
            tituloimagen=informacion['tituloimagen']

            destino_nuevo = Destino (titulo=titulo, subtitulo=subtitulo, lugar=lugar, provincia=provincia, fecha=fecha, cuerpo=cuerpo, autor=autor, imagen=imagen, tituloimagen=tituloimagen)
            destino_nuevo.save()

            return render(request, 'inicio.html')

    else: 
        form = DestinosFormulario()

    return render (request, 'destinosForm.html', {'form':form})
    


#----------------Leer Destinos------------------

def destinosLeer(request):
    destinos = Destino.objects.all()
    
    return render (request, 'destinosLeer.html', {'destinos':destinos})



#-------------Acutalizar Destinos---------------

def destinosEditar(request, id):
    destinos=Destino.objects.get(id=id)
    if request.method == 'POST':
        form = destinosFormulario(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            destinos.titulo=informacion['titulo']
            destinos.subtitulo=informacion['subtitulo']
            destinos.lugar=informacion['lugar']
            destinos.provincia=informacion['provincia']
            destinos.fecha=informacion['fecha']
            destinos.cuerpo=informacion['cuerpo']
            destinos.autor=informacion['autor']
            destinos.imagen=destinos.imagen=request.FILES['imagen']
            destinos.tiuloimagen=informacion['tituloimagen']
            destinos.save()
            destinos=Destino.objects.all()
            return render(request, 'destinosLeer.html', {'mensaje':'Destino editado correctamente'})

    else:
        formu=DestinosFormulario(initial={'titulo':destinos.titulo, 'subtitulo':destinos.subtitulo, 'lugar':destinos.lugar, 'provincia':destinos.provincia, 'fecha':destinos.fecha, 'cuerpo':destinos.cuerpo, 'autor':destinos.autor, 'imagen':destinos.imagen, 'tituloimagen':destinos.tiuloimagen})

    return render (request, 'destinosEditar.html', {'form':formu, 'destinos':destinos})
#---------------Borrar Destinos-----------------

def destinosEliminar(request, id):
    destinos = Destino.objects.get(id=id)
    destinos.delete()

    destinos=Destino.objects.all()

    return render(request, 'destinosLeer.html', {'destinos':destinos})

#------------------------------------------------
#----------------Sobre Nosotros------------------
#------------------------------------------------

def nosotros(request):
    return render(request, 'nosotros.html')



#------------------------------------------------
#-------------------Contacto---------------------
#------------------------------------------------
def contacto(request):
    return render(request, 'contacto.html')

