from django.db import models

# Create your models here.
class Moto(models.Model):
    marca = models.CharField(max_length=50)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='motos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "moto"
        verbose_name_plural = "motos"

    def __str__(self):
        return self.marca