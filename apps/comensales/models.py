from django.db import models

# Create your models here.
class Comensales(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(max_length=2)
    direccion = models.CharField(max_length=20, default='sin direccion')

    def __str__(self):
        return "{} de tipo {}".format(self.nombre, self.edad)


