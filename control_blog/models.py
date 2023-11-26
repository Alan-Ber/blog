from django.db import models


class Entrada(models.Model):
    titulo = models.CharField(max_length=64, default="ValorPredeterminado")
    autor = models.CharField(max_length=100)
    cuerpo = models.TextField(blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.titulo}"


class Usuario(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido} {self.nombre}"


class Etiqueta(models.Model):
    nombre_tag = models.CharField(max_length=256)
    info_tag = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre_tag}"
