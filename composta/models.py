from django.db import models


class Residuo(models.Model):
    CATEGORIAS = [
        ('VERDE', 'Material Verde (Nitrógeno)'),
        ('MARRON', 'Material Marrón (Carbono)'),
        ('PROHIBIDO', 'No Compostable'),
    ]
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=15, choices=CATEGORIAS)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"


class Guia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
# Create your models here.
