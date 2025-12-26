from rest_framework import serializers
from .models import *


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    cantidad_matriculas = serializers.SerializerMethodField()
    class Meta:
        model = Sucursal
        fields = '__all__'
    def get_cantidad_matriculas(self, obj):
        return Matricula.objects.filter(sucursal_codigo=obj).count()

class MatriculaSerializer(serializers.ModelSerializer):
    alumno_rut = serializers.PrimaryKeyRelatedField(queryset = Alumno.objects.all())
    curso_codigo = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all())
    sucursal_codigo = serializers.PrimaryKeyRelatedField(queryset=Sucursal.objects.all())
    curso_nombre = serializers.CharField(source='curso_codigo.nombre', read_only=True)
    sucursal_nombre = serializers.CharField(source='sucursal_codigo.nombre', read_only=True)
    alumno_nombre = serializers.CharField(source='alumno_rut.nombre',read_only=True)

    class Meta:
        model = Matricula
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    matriculas = MatriculaSerializer(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = '__all__'