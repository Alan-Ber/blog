from django.shortcuts import render
from django.http import HttpResponse
from control_blog.models import Entrada, Usuario, Etiqueta


def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response


def listado_entradas(request):
    contexto = {
        "entrada": Entrada.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='entradas.html',
        context=contexto,
    )
    return http_response
