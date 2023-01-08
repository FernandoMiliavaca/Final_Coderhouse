from django.shortcuts import render

from Accounts.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

#------------------------------------------------
#------------------Dashboard---------------------
#------------------------------------------------

def index(request):
    return render (request, 'index.html')



def bienvenido(request):
    return render (request, 'bienvenido.html')

#------------------------------------------------
#-------------------Registro---------------------
#------------------------------------------------

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            usuario = authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render (request, 'login.html', {'mensaje':f'Bienvenido {usuario}'})
            
            else:
                return render(request, 'login.html', {'mensaje':'Usuario o contraseña incorrecta'})

        else:
            return render (request, 'login.html', {'mensaje':'Usuario o contraseña incorrecta', 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

#------------------------------------------------
#-------------------Registro---------------------
#------------------------------------------------

def register(request):
    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data.get('username')
            form.save()
            return render (request, 'destinosLeer.html', {'mensaje': f'Usuario {username} ha sido creado correctamente'})

        else:
            return render(request, 'register.html', {'form':form, 'mensaje' : 'Error al crear el usuario. Intente nuevamente'})    

    else: 
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form':form})


#------------------------------------------------
#-------------------Cuentas----------------------
#------------------------------------------------

#def cuentas(request):
    return render(request, 'cuentas.html')



#-----------------Crear Cuenta-------------------

#def cuentasFormulario(request):
    if request.method == 'POST':
        form = CuentasFormulario(request.POST)
        print(form)

        if form.is_valid():

            informacion = form.cleaned_data

            user = informacion['user']
            password = informacion['password']
            email = informacion['email']

            cuenta_nueva = Cuenta (user=user, password=password, email=email)
            cuenta_nueva.save()

            return render(request, 'dashboard.html')
    
    else:
        form = CuentasFormulario()
    return render (request, 'cuentasForm.html', {'form':form})

#------------------Leer Cuenta-------------------

#def cuentasLeer(request):
    cuentas = Cuenta.objects.all()

    return render (request, 'cuentasLeer.html', {'cuentas':cuentas})

#-----------------Editar Cuenta------------------

#def cuentasEditar(request, id):
    cuentas=Cuenta.objects.get(id=id)

    if request.method == 'POST':
        form = cuentasFormulario(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            cuentas.user = informacion['user']
            cuentas.password = informacion['informacion']
            cuentas.email = informacion['email']

            cuentas.save()
            return render(request, 'cuentasLeer.html', {'mensaje':'Cuenta editada'})
    
    else:
        form = CuentasFormulario(initial={'user':cuentas.user, 'password':cuentas.password, 'email':cuentas.email})

    return render (request, 'cuentasEditar.html', {'form':form, 'cuentas':cuentas})



#------------------------------------------------
#------------------Perfiles----------------------
#------------------------------------------------

#def perfiles(request):
    return render (request, 'perfiles.html')

#-----------------Crear Perfil-------------------

#def perfilesFormulario(request):
    if request.method == 'POST':
        form = PerfilesFormulario(request.POST)
        print(form)

        if form.is_valid():

            informacion = form.cleaned_data
            autor = informacion['autor']
            sitioweb = informacion['sitioweb']
            descripcion = informacion['descripcion']

            perfil_nuevo = Perfil (autor=autor, sitioweb=sitioweb, descripcion=descripcion)
            perfil_nuevo.save()

            return render(request, 'dashboard.html')
    
    else:
        form = PerfilesFormulario()

    return render (request, 'perfilesForm.html', {'form':form})


#------------------Leer Perfil-------------------

#def perfilLeer(request):
    perfiles = Perfil.objects.all()

    return render (request, 'perfilesLeer.html',{'perfiles':perfiles})

#----------------Editar Perfil-------------------

#def perfilEditar(request, id):
    perfiles = Perfil.objects.get(id=id)

    if request.method == 'POST':
        form = perfilesFormulario(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            perfiles.autor = informacion['autor']
            perfiles.sitioweb = informacion['sitioweb']
            perfiles.descripcion = informacion['descripcion']

            perfiles.save()
            return render(request, 'perfilesLeer.html', {'mensaje':'Perfil Editado'})

    else: 
        form = PerfilesFormulario(initial={'autor':perfiles.autor, 'sitioweb':perfiles.sitioweb, 'descripcion':perfiles.descripcion})

    return render (request, 'perfilesEditar.html', {'form':form, 'perfiles':perfiles})

    