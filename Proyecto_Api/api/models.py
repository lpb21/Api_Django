from django.db import models

# Create your models here.
class Departamento(models.Model):
    codigoDep= models.PositiveIntegerField()
    nombre = models.CharField(max_length=50)
    presupuesto = models.PositiveIntegerField()



class Empleado(models.Model):
    codigo = models.PositiveIntegerField()
    nif = models.PositiveIntegerField()
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    codigoDepartamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)

