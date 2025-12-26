from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'cursos', CursoViewSet)
router.register(r'alumnos', AlumnoViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = router.urls