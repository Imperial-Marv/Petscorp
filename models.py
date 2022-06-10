from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Producto (models.Model):
    idProd = models.IntegerField(primary_key=True, verbose_name= 'codigo de barra')
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __int__(self):
        return self.idProd


class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    correo= models.EmailField('Correo')
    
    def __str__(self):
        return self.nombre
