from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre+" "+(self.apellido)

class Helado(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Nota(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.nombre+" "+(self.apellido)+" "+str(self.email)