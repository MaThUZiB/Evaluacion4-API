from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'codigo']

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'email']

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'direccion']

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fileds = ['curso_codigo', 'alumno_rut', 'sucursal_codigo']
    search_fields = ['curso_codigo__nombre', 'alumno_rut__nombre', 'sucursal_codigo__nombre']



