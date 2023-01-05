from django.db import models

# Create your models here.
class Destino(models.Model):

    titulo = models.CharField(max_length= 50)
    subtitulo = models.CharField(max_length= 50)
    lugar = models.CharField(max_length= 30)
    provincia = models.CharField(max_length= 30)
    fecha = models.DateField()
    cuerpo = models.TextField()
    autor = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='media', null=True)
    tiuloimagen = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo+ ' - ' + self.subtitulo + ' - ' +self.lugar+ ' - '+self.provincia+ ' - ' + str(self.fecha) + ' - ' + self.autor + ' - ' + self.imagen.name + ' - ' + self.tiuloimagen