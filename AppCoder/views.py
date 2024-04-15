from django.shortcuts import render
from AppCoder.models import Curso, Profesores,Alumnos,Ingreso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario,Profesores_formulario,Alumnos_formulario,Ingreso_formulario
# Create your views here.


def inicio(request):
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
    #retorna toda la lista de cursos
    #creo el dicionario para mostrar los cursos
    dicc = {"cursos":cursos}
    #comunicamos el diccionario al template para que lo vea
    plantilla = loader.get_template("cursos.html")
    #en el render se hace la parte del dinamismo, es todo el proceso 
    documento = plantilla.render(dicc)
    #esto es lo que se retorna, lo que ya se va a mostrar
    return HttpResponse(documento)


def alumnos(request):
    alumnos = Alumnos.objects.all()
    dicc = {"alumnos":alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def profesores(request):
    profesores = Profesores.objects.all()
    dicc = {"profesores":profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


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
            return render(request, "formulario.html")
        
    return render(request , "formulario.html")    

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

        #renderizo la tabla con todos los cursos para no darle actualizar le paso los cursos sin el que borre
        return render(request, "cursos.html", {"cursos":curso})

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

            return render( request , "cursos.html" , {"cursos":curso})


    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre,"camada":curso.camada})

    return render (request, "editar_curso.html",{"mi_formulario":mi_formulario,"curso":curso})

def elimina_alumno(request,id):
        alumnos = Alumnos.objects.get(id=id)
        alumnos.delete()
        #trigo todos los cursos
        alumnos = Alumnos.objects.all()

        #renderizo la tabla con todos los cursos para no darle actualizar le paso los cursos sin el que borre
        return render(request, "alumnos.html", {"alumnos":alumnos})

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

            return render( request , "alumnos.html" , {"alumnos":alumnos})


    else:
        mi_formulario = Alumnos_formulario(initial={"nombre":alumnos.nombre,"camada":alumnos.camada,"clase":alumnos.clase,"semestre":alumnos.semestre})

    return render (request, "editar_alumno.html",{"mi_formulario":mi_formulario,"alumnos":alumnos})

def elimina_profesor(request,id):
        profesores = Profesores.objects.get(id=id)
        profesores.delete()
        #trigo todos los cursos
        profesores = Profesores.objects.all()

        #renderizo la tabla con todos los cursos para no darle actualizar le paso los cursos sin el que borre
        return render(request, "profesores.html", {"profesores":profesores})

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

            return render( request , "profesores.html" , {"profesores":profesores})


    else:
        mi_formulario = Profesores_formulario(initial={"nombre":profesores.nombre,"camada":profesores.camada,"clase":profesores.clase})

    return render (request, "editar_profesor.html",{"mi_formulario":mi_formulario,"profesores":profesores})