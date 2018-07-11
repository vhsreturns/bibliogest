from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    anoPublicacion = models.DateField()
    sinopsis = models.TextField()
    imgPortada = models.ImageField()
    valoracion = models.FloatField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    codigoPostal = models.IntegerField()
    poblacion = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=120)
    telefono = models.IntegerField()
    fechaNacimiento = models.DateField()
    penalizado = models.BooleanField(default=False)
    fechaRegistro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class LugarPrestamo(models.Model):
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaFin = models.DateTimeField()
    entregado = models.BooleanField(default=False)
    lugar = models.ForeignKey('LugarPrestamo', on_delete=models.CASCADE)

    def __str__(self):
        return 'Préstamo: ' + self.libro.titulo
