"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog.views import saludar_con_html, listado_entradas, acerca_de, crear_post, buscar_entradas, eliminar_entrada, editar_entrada, ver_entrada

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("aaa/", include("control_blog.urls")),
    # path("saludar-usuario/", saludar),
    path("", saludar_con_html, name="inicio"),
    path("entradas/", listado_entradas, name="entradas"),
    path("info/", acerca_de, name="acerca_de"),
    path("crear-post/", crear_post, name="crear_post"),
    path("buscar-entradas/", buscar_entradas, name="buscar_entradas"),
    path("eliminar-entrada/<str:titulo>/",
         eliminar_entrada, name="eliminar_entrada"),
    path("editar-entrada/<str:titulo>/", editar_entrada, name="editar_entrada"),
    path("ver-entrada/<str:titulo>/", ver_entrada, name="ver_entrada"),
    path("perfiles/", include("perfiles.urls")),

]
