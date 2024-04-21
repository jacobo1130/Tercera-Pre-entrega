Trabajo final python, Jacobo Vásquez
1.	Para poder ver la aplicación se debe cambiar la ruta de los templates en settings.py en DIRS por la ruta en donde se descargue, copiando la ruta del template en la computadora que se descargue, recordar cambiar los “\” por “/”
 

Ejecutar los comandos python manage.py check AppCoder   , esto para verificar que se encuentre bien y para proceder a crear el servidor local.
 python manage.py runserver

Al correr el servidor se entra a la vista principal
http://127.0.0.1:8000/AppCoder/

 


Para esta preentrega se anexo lo siguiente al código
1.	Se crearon 3 nuevos modelos adicionales y se migraron al proyecto las cuales son:
Profesores, esta consta de los profesores inscritos los cuales dictan los cursos, sus campos son: nombre, camada (número del curso) y clase (nombre de la asignatura).
 Alumnos: esta consta de los alumnos que cursan las asignaturas, sus campos son nombre, camada (número del curso), clase (nombre de la asignatura), semestre (el nivel en que está en la universidad).
Ingreso, consta de la gente que se quiere inscribir a un curso, que necesita una orientación tiene los siguientes campos nombre, curso (en el que está interesado inscribirse), celular y edad.
 
 
2.	Se añadieron otros 3 formularios para llenar las bases de datos anteriormente mostradas las cuales se encuentran en la pestaña regístrate.
http://127.0.0.1:8000/AppCoder/alta_curso
 
 

3.	Se completo más el template de alumnos para mostrar los alumnos inscritos en una tabla la cual se le realizo el método “alumnos” el cual recorre la base de datos para armar un diccionario el cual luego se muestra en la pantalla de alumnos.
http://127.0.0.1:8000/AppCoder/alumnos 
 
4.	 template adicional que es profesores.html, el cual muestra las imágenes de los profesores y una tabla que nos indica cuales hay en los cursos, para hacer esto se creo una base de datos la cual es Profesores y consta del nombre, camada (código del curso) y clase (nombre de la asignatura).
http://127.0.0.1:8000/AppCoder/profesores
 


5.	Se añadieron 2 nuevas casillas de búsqueda para buscar en las bases de datos de alumnos y profesores.
http://127.0.0.1:8000/AppCoder/buscar_curso
 
Al buscar algún registro se añade botón para volver a las opciones de búsqueda
 

Para todos los botones se añadieron redirecciones por lo cual hace más facil la navegación por la aplicación, también se crearon 7 nuevos métodos los cuales son los siguientes:
 

Alumnos: obtiene todos los registros de la BD de alumnos para luego pasarlos como un diccionario al template para que los recorra, de igual manera lo hace el método profesores.

Alumno_formulario, profesor_formulario, registro_formulario: obtiene la data del formulario de profesores o alumnos para cual sea el caso, la limpia y luego guarda en la BD estos datos.

Buscar_alumnos y buscar_profesores: busca por medio del método GET si el nombre del alumno o profesor se encuentra en la respectiva BD, si la encuentra nos muestra los resultados de lo contrario nos muestra que no se pudo encontrar registros.
