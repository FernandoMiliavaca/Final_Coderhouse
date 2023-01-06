from django.shortcuts import render
from .models import Cuenta, Perfil
from Accounts.forms import CuentasFormulario, PerfilesFormulario

# Create your views here.

#------------------------------------------------
#------------------Dashboard---------------------
#------------------------------------------------

def dashboard(request):
    return render (request, 'dashboard.html')

#------------------------------------------------
#-------------------Cuentas----------------------
#------------------------------------------------

def cuentas(request):
    return render(request, 'cuentas.html')



#-----------------Crear Cuenta-------------------

def cuentasFormulario(request):
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

#-----------------Editar Cuenta------------------



#------------------------------------------------
#------------------Perfiles----------------------
#------------------------------------------------

#-----------------Crear Perfil-------------------

#------------------Leer Perfil-------------------

#----------------Editar Perfil-------------------