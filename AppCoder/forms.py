from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}