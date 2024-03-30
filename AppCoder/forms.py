from django import forms

class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class Alumnos_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    clase = forms.CharField(max_length=30)
    semestre= forms.IntegerField()


class Profesores_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    clase = forms.CharField(max_length=30)

class Ingreso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    curso = forms.CharField(max_length=30)
    celular = forms.IntegerField(max_value=4000000000)
    edad = forms.IntegerField()