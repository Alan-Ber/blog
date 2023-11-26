from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from control_blog.models import Entrada, Usuario, Etiqueta
from control_blog.forms import EntradaFormulario

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


def acerca_de(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='info.html',
        context=contexto,
    )
    return http_response



def crear_post1(request):
   if request.method == "POST":
       data = request.POST
       nueva_entrada = Entrada(titulo=data['titulo'], subtitulo=data['subtitulo'], cuerpo=data['cuerpo'])
       nueva_entrada.save()
       url_exitosa = reverse('entradas')
       return redirect(url_exitosa)
   else:  # GET
       return render(
           request=request,
           template_name='formulario_post.html',
       )


def crear_post(request):
    if request.method == "POST":
        formulario = EntradaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]

            nueva_entrada = Entrada(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo)
            nueva_entrada.save()

            # Redirecciono al usuario a la lista de entradas
            url_exitosa = reverse('entradas')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = EntradaFormulario()

    return render(
        request=request,
        template_name='formulario_post.html',
        context={'formulario': formulario}
    )

