from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def saludar(request):
    saludo = "Hola querido usuario"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido/a usuario/a, fecha {hoy.day}/{hoy.month}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

