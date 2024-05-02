from django.shortcuts import render
from AppCoder.models import Curso, Profesores,Alumnos,Ingreso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario,Profesores_formulario,Alumnos_formulario,Ingreso_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppCoder.models import Curso, Avatar


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if avatares.exists():
        return render(request, "padre.html", {'url':avatares[0].imagen.url})
    else:
        return render(request,"padre.html")


def alta_curso(request,nombre):
    curso = Curso(nombre=nombre,camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    #curso metodo de la clase curso
    #traeme todo los ojetos de tipo curso los obtiene de la BD
    cursos = Curso.objects.all()
    avatares= Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "cursos.html",{"cursos":cursos,"url":avatares[0].imagen.url})
    else:
        return render(request,"cursos.html")


def alumnos(request):
    alumnos = Alumnos.objects.all()
    avatares= Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "alumnos.html",{"alumnos":alumnos,"url":avatares[0].imagen.url})
    else:
        return render(request, "alumnos.html",{"alumnos":alumnos})
    

def profesores(request):
    profesores = Profesores.objects.all()
    avatares= Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "profesores.html",{"profesores":profesores,"url":avatares[0].imagen.url})
    else:
        return render(request, "profesores.html",{"profesores":profesores})

def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario.html")

    return render(request , "formulario.html")

def buscar_curso(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request, "buscar_curso.html",{"url":avatares[0].imagen.url})
    else:
        return render(request, "buscar_curso.html")

def buscar(request):
     
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        cursos=Curso.objects.filter(nombre__icontains=nombre)
        return render( request ,"resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre de curso")

def alumno_formulario(request):
    if request.method == "POST":

        mi_formulario = Alumnos_formulario( request.POST )

        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            alumno = Alumnos( nombre=datos["nombre"], camada=datos["camada"], clase=datos["clase"], semestre=datos["semestre"])
            alumno.save()
            return render(request, "formulario.html")
        
    return render(request , "formulario.html")

def profesor_formulario(request):
    if request.method == "POST":

        mi_formulario = Profesores_formulario( request.POST )

        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            profesor = Profesores( nombre=datos["nombre"], camada=datos["camada"], clase=datos["clase"])
            profesor.save()
            return render(request, "formulario.html")
        
    return render(request , "formulario.html")    

def registro_formulario(request):
    if request.method == "POST":

        mi_formulario = Ingreso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos= mi_formulario.cleaned_data
            ingreso = Ingreso( nombre=datos["nombre"], curso=datos["curso"], celular=datos["celular"], edad=datos["edad"])
            ingreso.save()
            avatares= Avatar.objects.filter(user=request.user.id)
            return render(request, "formulario.html",{"url":avatares[0].imagen.url})
    avatares= Avatar.objects.filter(user=request.user.id)    
    return render(request , "formulario.html",{"url":avatares[0].imagen.url})    

def buscar_alumnos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        cursos=Alumnos.objects.filter(nombre__icontains=nombre)
        return render( request ,"resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre de curso")

def buscar_profesores(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        cursos=Profesores.objects.filter(nombre__icontains=nombre)
        return render( request ,"resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre de curso")
    
def elimina_curso(request,id):
        curso = Curso.objects.get(id=id)
        curso.delete()
        #trigo todos los cursos
        curso = Curso.objects.all()
        avatares= Avatar.objects.filter(user=request.user.id)
        #renderizo la tabla con todos los cursos para no darle actualizar le paso los cursos sin el que borre
        return render(request, "cursos.html", {"cursos":curso,"url":avatares[0].imagen.url})

def editar(request,id):

    curso=Curso.objects.get(id=id)
    
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada= datos["camada"]
            curso.save()

            curso=Curso.objects.all()
            avatares= Avatar.objects.filter(user=request.user.id)
            return render( request , "cursos.html" , {"cursos":curso,"url":avatares[0].imagen.url})


    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre,"camada":curso.camada})
    avatares= Avatar.objects.filter(user=request.user.id)
    return render (request, "editar_curso.html",{"mi_formulario":mi_formulario,"curso":curso,"url":avatares[0].imagen.url})

def elimina_alumno(request,id):
        alumnos = Alumnos.objects.get(id=id)
        alumnos.delete()
        #trigo todos los cursos
        alumnos = Alumnos.objects.all()
        avatares= Avatar.objects.filter(user=request.user.id)
        #renderizo la tabla con todos los cursos para no darle actualizar le paso los cursos sin el que borre
        return render(request, "alumnos.html", {"alumnos":alumnos,"url":avatares[0].imagen.url})

def editar_alumno(request,id):

    alumnos=Alumnos.objects.get(id=id)
    
    if request.method == "POST":
        mi_formulario = Alumnos_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumnos.nombre = datos["nombre"]
            alumnos.camada= datos["camada"]
            alumnos.clase= datos["clase"]
            alumnos.semestre= datos["semestre"]

            alumnos.save()

            alumnos=Alumnos.objects.all()
            avatares= Avatar.objects.filter(user=request.user.id)
            return render( request , "alumnos.html" , {"alumnos":alumnos,"url":avatares[0].imagen.url})


    else:
        mi_formulario = Alumnos_formulario(initial={"nombre":alumnos.nombre,"camada":alumnos.camada,"clase":alumnos.clase,"semestre":alumnos.semestre})
    avatares= Avatar.objects.filter(user=request.user.id)
    return render (request, "editar_alumno.html",{"mi_formulario":mi_formulario,"alumnos":alumnos,"url":avatares[0].imagen.url})

def elimina_profesor(request,id):
        profesores = Profesores.objects.get(id=id)
        profesores.delete()
        #trigo todos los cursos
        profesores = Profesores.objects.all()

        avatares= Avatar.objects.filter(user=request.user.id)
        return render(request, "profesores.html", {"profesores":profesores,"url":avatares[0].imagen.url})

def editar_profesor(request,id):

    profesores=Profesores.objects.get(id=id)
    
    if request.method == "POST":
        mi_formulario = Profesores_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesores.nombre = datos["nombre"]
            profesores.camada= datos["camada"]
            profesores.clase= datos["clase"]
            
            profesores.save()

            profesores=Profesores.objects.all()
            avatares= Avatar.objects.filter(user=request.user.id)
            return render( request , "profesores.html" , {"profesores":profesores,"url":avatares[0].imagen.url})


    else:
        mi_formulario = Profesores_formulario(initial={"nombre":profesores.nombre,"camada":profesores.camada,"clase":profesores.clase})
    avatares= Avatar.objects.filter(user=request.user.id)
    return render (request, "editar_profesor.html",{"mi_formulario":mi_formulario,"profesores":profesores,"url":avatares[0].imagen.url})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user )
                avatares= Avatar.objects.filter(user=request.user.id)

                if avatares.exists():
                    return render( request , "inicio.html" , {"url":avatares[0].imagen.url, "mensaje":f"Bienvenido/a {usuario}", "usuario":usuario})
                else:
                    return render( request , "inicio.html",{"mensaje":f"Bienvenido/a {usuario}", "usuario":usuario})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})


def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")     
    else:
        form = UserCreationForm()
    avatares= Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render(request , "registro.html" , {"form":form,"url":avatares[0].imagen.url})
    else:
        return render(request , "registro.html" , {"form":form})

def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            avatares= Avatar.objects.filter(user=request.user.id)
            if avatares.exists():
                return render(request , "inicio.html",{"usuario":usuario,"url":avatares[0].imagen.url})
            else:
                return render(request , "inicio.html")
    else:
    
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    avatares= Avatar.objects.filter(user=request.user.id)
    if avatares.exists():
        return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario,"url":avatares[0].imagen.url})
    else:
        return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

