from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from control_blog.models import Entrada, Usuario, Etiqueta
from control_blog.forms import EntradaFormulario


### INICIO ####

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

### LISTADO DE DE ENTRADAS ###


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

### INFO BLOG ####


def acerca_de(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='info.html',
        context=contexto,
    )
    return http_response

### CREAR ENTRADAS ###


@login_required
def crear_post(request):
    if request.method == "POST":
        formulario = EntradaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            titulo = data["titulo"]
            autor = data["autor"]
            cuerpo = data["cuerpo"]

            nueva_entrada = Entrada(titulo=titulo, autor=autor, cuerpo=cuerpo)
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

### BUSCAR ENTRADAS ###


def buscar_entradas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        entradas = Entrada.objects.filter(titulo__icontains=busqueda)
        contexto = {
            "entradas": entradas,
        }
        return render(
            request=request,
            template_name='entradas.html',
            context=contexto,
        )
    else:
        # Manejar el caso en el que no se envió una solicitud POST (opcional)
        return render(
            request=request,
            template_name='formulario_busqueda_entradas.html',
        )

### ELIMINAR ENTRADA ###


@login_required
def eliminar_entrada(request, titulo):
    entrada = Entrada.objects.get(titulo=titulo)
    if request.method == "POST":
        entrada.delete()
        url_exitosa = reverse('entradas')
        return redirect(url_exitosa)

### EDITAR ENTRADA ###


@login_required
def editar_entrada(request, titulo):

    entrada = Entrada.objects.get(titulo=titulo)
    if request.method == "POST":
        formulario = EntradaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            entrada.titulo = data['titulo']
            entrada.autor = data['autor']
            entrada.cuerpo = data['cuerpo']
            entrada.save()
            url_exitosa = reverse('entradas')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': entrada.titulo,
            'comision': entrada.autor,
            'comision': entrada.cuerpo,
        }
        formulario = EntradaFormulario(initial=inicial)
    return render(
        request=request,
        template_name='formulario_post.html',
        context={'formulario': formulario},)

### VER ENTRADAS ###


def ver_entrada(request, titulo):
    entrada = Entrada.objects.get(titulo=titulo)
    contexto = {'entrada': entrada}
    return render(request, 'entradas_cuerpos.html', contexto)
