from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion   = models.TextField(max_length = 100)
    stock         = models.IntegerField()
    precioCosto   = models.IntegerField()
    precioVenta   = models.IntegerField()


    def __str__(self):
        return self.descripcion
        