from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=4)
    descripcion = models.CharField(max_length=20, default='la carta')
    procedencia = models.CharField(max_length=15, default='sin origen')

    def __str__(self):
        return "{} de tipo {}".format(self.nombre, self.precio)
