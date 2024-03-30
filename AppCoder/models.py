from django.db import models

# Create your models here.

#con esto se llena una tabla de la base de datos SQL
class Curso(models.Model):
   nombre = models.CharField(max_length=40)
   camada = models.IntegerField()

class Profesores(models.Model):
   nombre = models.CharField(max_length=40)
   camada = models.IntegerField()
   clase=models.CharField(max_length=40)

class Alumnos(models.Model):
   nombre = models.CharField(max_length=40)
   camada = models.IntegerField()
   clase=models.CharField(max_length=40)
   semestre=models.IntegerField()

class Ingreso(models.Model):
   nombre = models.CharField(max_length=40)
   curso=models.CharField(max_length=40)
   celular=models.IntegerField()
   edad=models.IntegerField()