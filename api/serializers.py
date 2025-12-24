from rest_framework import serializers
from .models import *


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer(read_only=True)

    class Meta:
        model = Matricula
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    matricula = MatriculaSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    cantidad_matriculas = serializers.SerializerMethodField()

    class Meta:
        model = Sucursal
        fields = '__all__'
    
    def get_cantidad_matriculas(self, obj):
        return Matricula.objects.filter(sucursal=obj).count()

