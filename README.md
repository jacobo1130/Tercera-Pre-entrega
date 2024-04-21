Entrega final Python_54125, Jacobo Vásquez
1.	Para poder ver la aplicación se debe cambiar la ruta de los templates en settings.py en DIRS por la ruta en donde se descargue, copiando la ruta del template en la computadora que se descargue, recordar cambiar los “\” por “/”
 

Ejecutar los comandos python manage.py check AppCoder   , esto para verificar que se encuentre bien y para proceder a crear el servidor local.
 python manage.py runserver

Al correr el servidor se entra a la vista principal
http://127.0.0.1:8000/AppCoder/

Usuarios ya ingresados en la aplicación
Superusuario Jacob

usuario	contraseña	foto
jacob	Coder123	si
prueba1	Coder123	si
test2	Coder123	no

El test2 se probó sin foto puesto que se realizó la lógica para que los usuarios sin foto no rompan las aplicaciones puesto que cada vista se ve el nombre y foto de perfil.

A partir de la preentrega 3 se añadió lo pedido en la cosnigna:

CRUD para los 3 modelos (alumnos, cursos y profesores)
Login y logout
Los usuarios no logeados no pueden editar o borrar cursos
Se añadió el avatar como imagen de perfil en las vistas

Usuario logeado puede editar y borrar alumnos
 
 
Usuario no logeado no puede editar o borrar alumnos

 

De esta manera los usuarios no logeados no pueden acceder a cursos ni tampoco a editar y borrar, esto también aplica para los modelos cursos y profesores.

Al darle a la pestaña ingresar con cualquier usuario se pude logear de igual manera se pueden editar la clave y el correo de este,

 

 
Se puede pasar de vistas y me muestra el usuario en la parte del nav con nombre y foto.
También se puede hacer el logout de cualquiera de los 2 botones.

 
Se pueden añadir avatares a los usuarios creados, por favor ver el video adjunto el cual muestra la explicación del trabajo final.

