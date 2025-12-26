from django.db import models

# Create your models here.
class Sucursal(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80)
    direccion = models.CharField(max_length=120)
    email = models.CharField(max_length=80)
    fono = models.CharField(max_length=12)

class Matricula(models.Model):
    codigo = models.AutoField(primary_key=True)
    curso_codigo = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    alumno_rut = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='matriculas')
    sucursal_codigo = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='matriculas')
    fecha = models.DateField()