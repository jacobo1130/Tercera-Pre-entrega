from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    #path("alta_curso/<nombre>",views.alta_curso),
    path("alumnos",views.alumnos ,name="alumnos"),
    path("profesores", views.profesores ,name="profesores"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso,name="buscar_curso"),
    path("alta_profesor", views.profesor_formulario),
    path("alta_alumno", views.alumno_formulario),
    path("alta_registro", views.registro_formulario),
    path("buscar", views.buscar),
    path("buscar_alumnos", views.buscar_alumnos),
    path("buscar_profesores", views.buscar_profesores)

]
