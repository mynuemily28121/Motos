from django.db import models

# Create your models here.
class CategoriaAcc(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoriaAcc"
        verbose_name_plural = "categoriasAcc"

    def __str__(self):
        return self.nombre

class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaAcc, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="accesorios", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Accesorio"
        verbose_name_plural = "Accesorios"