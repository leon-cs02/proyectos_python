from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('index/', index, name="index"),
]