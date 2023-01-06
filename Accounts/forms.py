from django import forms

class CuentasFormulario(forms.Form):
    user = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.EmailField()

class PerfilesFormulario(forms.Form):
    sitioweb = forms.URLField()
    descripcion = forms.CharField(max_length=250)