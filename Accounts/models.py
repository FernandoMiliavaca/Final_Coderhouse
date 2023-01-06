from django.db import models

# Create your models here.
class Cuenta(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return 'USUARIO: ' + self.user + ' - PASSWORD: ' + self.password + ' - EMAIL: ' + self.email 
    
class Perfil(models.Model):
    autor = models.CharField(max_length=50)
    sitioweb = models.URLField()
    descripcion = models.CharField(max_length=250)

