from django.template import Template, Context
from django.http import HttpResponse
import datetime

def saludar(request):
    saludo = "Bienvenidos a la comisión N° 57810 - Clases de Django"
    return HttpResponse(saludo)

def bienvenido(request, nombre, apellido):
    saludo = f"Te damos la bienvenida a la comisión N° 57810 {nombre} {apellido}"
    return HttpResponse(saludo)

def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    saludo = f"""

    <html>

    <h1> Bienvenidos al curso de Django! </h1>
    <h2> Te damos la bienvenida {nombre} {apellido}</h2>
    <h3> Hoy es {hoy}</h3>


    </html>

    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    with open("C:/Users/Usuario/Desktop/clase_17/Proyecto/Proyecto/plantillas/bienvenido.html") as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)

    return HttpResponse(saludo)