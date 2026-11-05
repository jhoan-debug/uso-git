from django.db import models

# Create your models here.
class Competidor(models.Model):
    nombre = models.CharField(max_length=100)
    centro = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre