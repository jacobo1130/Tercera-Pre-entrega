from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

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
    path("buscar_profesores", views.buscar_profesores),
    path("eliminar_curso/<int:id>",views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path("eliminar_alumno/<int:id>",views.elimina_alumno, name="elimina_alumno"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path("eliminar_profesor/<int:id>",views.elimina_profesor, name="elimina_profesor"),
    path("editar_profesor/<int:id>", views.editar_profesor, name="editar_profesor"),
    path("login",views.login_request,name="Login"),
    path("register", views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")

]
