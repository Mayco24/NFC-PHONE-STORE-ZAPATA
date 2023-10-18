from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Equipos(models.Model):
    titulo = models.CharField(max_length=30)
    marca =  models.CharField(max_length=10)
    modelo = models.CharField(max_length=15)
    estado = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)

    def __str__(self):
        return f"{self.titulo} {self.marca} {self.modelo} {self.estado} {self.precio}"

