from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_text = {k:'' for k in fields}




# Eliminar lo de abajo: 

#class CuentasFormulario(forms.Form):
    #user = forms.CharField(max_length=50)
    #password = forms.CharField(max_length=50)
    #email = forms.EmailField()

#class PerfilesFormulario(forms.Form):
    #autor = forms.CharField(max_length=50)
    #sitioweb = forms.URLField()
    #descripcion = forms.CharField(max_length=250)