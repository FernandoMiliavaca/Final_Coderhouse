from django import forms

class DestinosFormulario(forms.Form):

    titulo = forms.CharField(max_length= 50)
    subtitulo = forms.CharField(max_length= 50)
    lugar = forms.CharField(max_length= 30)
    provincia = forms.CharField(max_length= 30)
    cuerpo = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=30)
    imagen = forms.ImageField(label='imagen')
    