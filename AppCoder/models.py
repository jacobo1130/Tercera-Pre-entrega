from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#con esto se llena una tabla de la base de datos SQL
class Curso(models.Model):
   nombre = models.CharField(max_length=40)
   camada = models.IntegerField()

   def __str__(self):
        return f"Nombre: {self.nombre}     Camada: {self.camada}"

class Profesores(models.Model):
   nombre = models.CharField(max_length=40)
   camada = models.IntegerField()
   clase=models.CharField(max_length=40)

   def __str__(self):
        return f"Nombre: {self.nombre}     Camada: {self.camada}     Clase: {self.clase}"

class Alumnos(models.Model):
   nombre = models.CharField(max_length=40)
   camada = models.IntegerField()
   clase=models.CharField(max_length=40)
   semestre=models.IntegerField()

   def __str__(self):
        return f"Nombre: {self.nombre}     Camada: {self.camada}     Clase: {self.clase}     Semestre: {self.semestre}"

class Ingreso(models.Model):
   nombre = models.CharField(max_length=40)
   curso=models.CharField(max_length=40)
   celular=models.IntegerField()
   edad=models.IntegerField()